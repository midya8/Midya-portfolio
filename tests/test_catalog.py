import importlib.util
import json
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

spec = importlib.util.spec_from_file_location('builder', Path(__file__).resolve().parents[1] / 'tools/build_catalog.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []
        self.articles = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and attrs.get('class') == 'source':
            self.sources.append(attrs['href'])
        if tag == 'article':
            self.articles.append(attrs['data-id'])

class CatalogTests(unittest.TestCase):
    def test_all_source_files_exact(self):
        data = builder.catalog()
        paths = sorted(p for p in (builder.ROOT / 'projects').glob('*.md') if p.name not in builder.EXCLUDED)
        self.assertEqual([p.relative_to(builder.ROOT).as_posix() for p in paths], [p['path'] for p in data['projects']])
        self.assertEqual(len({p['id'] for p in data['projects']}), len(paths))
        for record, path in zip(data['projects'], paths):
            self.assertEqual(record, builder.extract(path.relative_to(builder.ROOT), path.read_bytes()))
            self.assertLessEqual(len(record['excerpt']), 363)
    def test_generated_outputs(self):
        for name, expected in builder.outputs().items():
            self.assertEqual((builder.ROOT / name).read_text(), expected, name)
    def test_static_cards_are_complete(self):
        data = builder.catalog()
        parser = Links()
        parser.feed(builder.render(data))
        self.assertEqual(parser.articles, [p['id'] for p in data['projects']])
        self.assertEqual(parser.sources, [p['source_url'] for p in data['projects']])
    def test_fenced_comments_not_headings(self):
        text = '# Real\n\n```sh\n# False title\n```\n\nActual description has enough words to count as meaningful source prose.\n\n## Feature\n'
        p = builder.extract(Path('projects/a.md'), text.encode())
        self.assertEqual(p['headings'], ['Real', 'Feature'])
        self.assertTrue(p['excerpt'].startswith('Actual description'))
    def test_bold_opening_not_ignored(self):
        text = '# Demo\n\n**Real opening.** This is the actual introduction and must not be replaced by installation instructions.\n\n## Run\n\nOr install something here.\n'
        p = builder.extract(Path('projects/a.md'), text.encode())
        self.assertTrue(p['excerpt'].startswith('Real opening.'))
    def test_navigation_not_description(self):
        text = '## Demo\n\n[Live](https://example.invalid/) | [Source](https://example.invalid/source)\n\nThis supplied prose is long enough to describe the actual project.\n'
        self.assertTrue(builder.extract(Path('projects/a.md'), text.encode())['excerpt'].startswith('This supplied'))
    def test_escape_external_markup(self):
        p = builder.extract(Path('projects/a.md'), b'# <script>title</script>\n\nA description with <img src=x onerror=alert(1)> markup and enough words to pass the prose rule.\n')
        self.assertNotIn('<', p['title'])
        data = {'projects': [dict(p, title='<script>alert(1)</script>', excerpt='"&<evil>')]}
        rendered = builder.render(data)
        self.assertNotIn('<script>alert(1)</script>', rendered)
        self.assertIn('&lt;script&gt;', rendered)
    def test_missing_source_refused(self):
        with self.assertRaises(ValueError):
            builder.extract(Path('projects/a.md'), b'# Title\n')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'projects').mkdir()
            with self.assertRaises(ValueError):
                builder.catalog(root)
    def test_stable_digest(self):
        text = b'# Test\n\nA description containing enough ordinary words to qualify as opening prose.\n'
        a = builder.extract(Path('projects/a.md'), text)
        b = builder.extract(Path('projects/a.md'), text + b'\n')
        self.assertNotEqual(a['sha256'], b['sha256'])
        self.assertEqual(a['excerpt'], b['excerpt'])
    def test_dynamic_shards_beyond_one_hundred(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'projects').mkdir()
            for i in range(101):
                (root / 'projects' / f'p-{i:03}.md').write_text('# Project\n\nThis is enough opening prose to describe a source-backed index fixture.\n')
            out = builder.outputs(root)
            manifest = json.loads(out['docs/catalog.json'])
            self.assertEqual(manifest['count'], 101)
            self.assertEqual(len(manifest['shards']), 6)
            self.assertIn('catalog-data-5.js', out['docs/index.html'])
            self.assertEqual(len(json.loads(out['docs/catalog-5.json'])), 1)
    def test_accented_terms_preserved_as_normalized_words(self):
        text = '# Sample\n\nA long enough description introducing our caf' + chr(233) + ' and its implementation in prose.\n'
        self.assertIn('cafe', builder.extract(Path('projects/a.md'), text.encode())['terms'])
    def test_contract_and_json(self):
        data = json.loads(builder.outputs()['docs/catalog.json'])
        self.assertEqual(data['schema'], 'portfolio-catalog/v1')
        self.assertIn('Not a fresh test', data['scope'])
        self.assertNotIn('test_count', builder.catalog()['projects'][0])
        self.assertEqual(data['count'], len(builder.catalog()['projects']))
        actual = []
        for shard in data['shards']:
            actual.extend(json.loads(builder.outputs()['docs/' + shard]))
        self.assertEqual(actual, builder.catalog()['projects'])

if __name__ == '__main__':
    unittest.main()
