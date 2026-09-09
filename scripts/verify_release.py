"""Verify recorded assets, links, and the installable Skill archive; no network."""
from pathlib import Path
import hashlib
import json
import re
import struct
import zipfile
from pack_skill import check_boundary

ROOT = Path(__file__).resolve().parents[1]


def check():
    sources = json.loads((ROOT / "examples/sources/manifest.json").read_text())
    results = json.loads((ROOT / "evals/results-manifest.json").read_text())
    for manifest in sorted((ROOT / "evals").glob("*/results-manifest.json")):
        results.extend(json.loads(manifest.read_text()))
    for row in sources:
        path = ROOT / "examples/sources" / row["file"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], path
        assert row["author"] and row["license"] and row["page"], path
    for row in results:
        path = ROOT / row["file"]
        data = path.read_bytes()
        assert data[:8] == b"\x89PNG\r\n\x1a\n", path
        width, height = struct.unpack(">II", data[16:24])
        assert (width, height) == (row["width"], row["height"]), path
        assert hashlib.sha256(data).hexdigest() == row["sha256"], path
        assert (ROOT / row["prompt"]).is_file(), path
        if "source" in row:
            assert (ROOT / row["source"]).is_file(), path
        for reference in row.get("reference_images", []):
            assert (ROOT / reference).is_file(), (path, reference)
        if row["selected"]:
            # Default stays exact. A recorded rounding allowance is bounded to 2 px.
            tolerance = row.get("aspect_tolerance_px", 0)
            assert isinstance(tolerance, int) and 0 <= tolerance <= 2, path
            aspect = row.get("expected_aspect", [3, 4])
            assert len(aspect) == 2 and all(type(n) is int and 0 < n <= 10000 for n in aspect), path
            horizontal, vertical = aspect
            relative = row.get("aspect_tolerance_relative", 0)
            assert isinstance(relative, (int, float)) and 0 <= relative <= 0.005, path
            allowed = max(tolerance * vertical, height * horizontal * relative)
            assert abs(width * vertical - height * horizontal) <= allowed, f"Image differs from its recorded aspect: {path}"
    missing = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "experiments" in path.parts:
            continue
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" not in link and not link.startswith("#"):
                if not (path.parent / link.split("#")[0]).exists():
                    missing.append((str(path.relative_to(ROOT)), link))
    assert not missing, missing
    skills = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    checksums = {}
    for line in (ROOT / "dist/SHA256SUMS").read_text().splitlines():
        digest, name = line.split()
        checksums[name] = digest
    assert set(checksums) == {f"{skill.name}.zip" for skill in skills}
    for skill in skills:
        check_boundary(skill)
        archive_path = ROOT / "dist" / f"{skill.name}.zip"
        assert hashlib.sha256(archive_path.read_bytes()).hexdigest() == checksums[archive_path.name]
        with zipfile.ZipFile(archive_path) as archive:
            assert archive.testzip() is None
            expected = {
                str(path.relative_to(skill.parent)): path.read_bytes()
                for path in skill.rglob("*") if path.is_file()
            }
            assert set(archive.namelist()) == set(expected), f"Archive file set differs: {skill.name}"
            for name, data in expected.items():
                assert archive.read(name) == data, f"Stale archive: {name}"
    print(f"PASS: {len(sources)} sources, {len(results)} results, local links, {len(skills)} exact Skill ZIPs and checksums")



if __name__ == "__main__":
    check()
