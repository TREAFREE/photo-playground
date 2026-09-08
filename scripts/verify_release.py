"""Verify recorded assets, links, and the installable Skill archive; no network."""
from pathlib import Path
import hashlib
import json
import re
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def check():
    sources = json.loads((ROOT / "examples/sources/manifest.json").read_text())
    results = json.loads((ROOT / "evals/results-manifest.json").read_text())
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
        if row["selected"]:
            assert width * 4 == height * 3, f"Selected image must be portrait 3:4: {path}"
    missing = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "experiments" in path.parts:
            continue
        for link in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if "://" not in link and not link.startswith("#"):
                if not (path.parent / link.split("#")[0]).exists():
                    missing.append((str(path.relative_to(ROOT)), link))
    assert not missing, missing
    skill = ROOT / "skills/small-news-daily"
    with zipfile.ZipFile(ROOT / "dist/small-news-daily.zip") as archive:
        assert archive.testzip() is None
        expected = {
            str(path.relative_to(skill.parent)): path.read_bytes()
            for path in skill.rglob("*") if path.is_file()
        }
        assert set(archive.namelist()) == set(expected), "Archive file set differs from Skill"
        for name, data in expected.items():
            assert archive.read(name) == data, f"Stale archive: {name}"
    print(f"PASS: {len(sources)} sources, {len(results)} results, local links, exact Skill ZIP")


if __name__ == "__main__":
    check()
