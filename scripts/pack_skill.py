"""Build one self-contained Skill ZIP without repacking its siblings."""
from pathlib import Path
import argparse
import hashlib
import re
import zipfile


def check_boundary(skill):
    if skill.is_symlink() or not (skill / 'SKILL.md').is_file():
        raise ValueError(f'Invalid Skill directory: {skill}')
    boundary = skill.resolve()
    files = []
    for path in sorted(skill.rglob('*')):
        if path.is_symlink():
            raise ValueError(f'Symlinks are not portable Skill resources: {path}')
        if not path.is_file():
            continue
        if path.suffix == '.md':
            for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if link.startswith(('https://', 'http://', 'mailto:', '#')):
                    continue
                target = (path.parent / link.split('#')[0]).resolve()
                if not target.is_relative_to(boundary) or not target.exists():
                    raise ValueError(f'Missing or cross-boundary reference: {path}: {link}')
        files.append(path)
    return files


def build(root, name):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise ValueError('Use a single Skill directory name')
    skill = root / 'skills' / name
    files = check_boundary(skill)
    destination = root / 'dist'
    destination.mkdir(exist_ok=True)
    archive = destination / f'{name}.zip'
    temporary = destination / f'{name}.zip.tmp'
    try:
        with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as output:
            for path in files:
                info = zipfile.ZipInfo(str(path.relative_to(skill.parent)), (2020, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = (0o100755 if path.stat().st_mode & 0o111 else 0o100644) << 16
                output.writestr(info, path.read_bytes())
        temporary.replace(archive)
    finally:
        temporary.unlink(missing_ok=True)
    (destination / f"{name}.sha256").write_text(hashlib.sha256(archive.read_bytes()).hexdigest() + "  " + archive.name + "\n")
    # Only the selected ZIP is written. This index reads existing sibling ZIPs.
    checksums = ''.join(
        hashlib.sha256(path.read_bytes()).hexdigest() + '  ' + path.name + '\n'
        for path in sorted(destination.glob('*.zip'))
    )
    (destination / 'SHA256SUMS').write_text(checksums)
    return archive


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill', help='Only this Skill will be packaged')
    args = parser.parse_args()
    print(build(Path(__file__).resolve().parents[1], args.skill))
