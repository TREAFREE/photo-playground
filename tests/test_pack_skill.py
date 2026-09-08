import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('pack_skill', Path(__file__).resolve().parents[1] / 'scripts/pack_skill.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class IsolationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ['alpha', 'beta']:
            skill = self.root / 'skills' / name
            skill.mkdir(parents=True)
            (skill / 'SKILL.md').write_text(f'# {name}\n[Reference](direction.md)\n')
            (skill / 'direction.md').write_text(name)

    def test_edit_and_package_does_not_change_other_skill(self):
        beta = module.build(self.root, 'beta')
        before_zip = beta.read_bytes()
        before_source = (self.root / 'skills/beta/direction.md').read_bytes()
        (self.root / 'skills/alpha/direction.md').write_text('new art direction')
        alpha = module.build(self.root, 'alpha')
        self.assertEqual(before_zip, beta.read_bytes())
        self.assertEqual(before_source, (self.root / 'skills/beta/direction.md').read_bytes())
        with zipfile.ZipFile(alpha) as archive:
            self.assertEqual(set(archive.namelist()), {'alpha/SKILL.md', 'alpha/direction.md'})
            self.assertEqual(archive.read('alpha/direction.md'), b'new art direction')

    def test_cross_skill_reference_rejected(self):
        (self.root / 'skills/alpha/SKILL.md').write_text('[Shared](../beta/direction.md)')
        with self.assertRaisesRegex(ValueError, 'cross-boundary'):
            module.build(self.root, 'alpha')
        self.assertFalse((self.root / 'dist/alpha.zip').exists())

    def test_symlink_rejected(self):
        (self.root / 'skills/alpha/shared.md').symlink_to(self.root / 'skills/beta/direction.md')
        with self.assertRaisesRegex(ValueError, 'Symlinks'):
            module.build(self.root, 'alpha')

    def test_same_content_same_package(self):
        first = module.build(self.root, 'alpha').read_bytes()
        self.assertEqual(first, module.build(self.root, 'alpha').read_bytes())


if __name__ == '__main__':
    unittest.main()
