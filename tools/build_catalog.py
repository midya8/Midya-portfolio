#!/usr/bin/env python3
"""Build a deterministic discovery index without changing any source case study."""
import argparse
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'README.md', 'CONTINUED.md'}

def blocks(text):
    """Ignore fenced examples so shell comments cannot become project titles."""
    fence = None
    current = []
    for line in text.splitlines():
        mark = re.match(r'^\s*(`{3,}|~{3,})', line)
        if mark:
            if fence is None:
                fence = mark[1][0]
            elif mark[1][0] == fence:
                fence = None
            if current:
                yield '\n'.join(current)
                current = []
            continue
        if fence:
            continue
        if not line.strip():
            if current:
                yield '\n'.join(current)
                current = []
        else:
            current.append(line)
    if current:
        yield '\n'.join(current)

def plain(text):
    text = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'<[^>]*>', '', text)
    text = text.replace('`', '').replace('**', '').replace('__', '')
    return ' '.join(html.unescape(text).split())

def extract(path, data):
    text = data.decode('utf-8')
    units = list(blocks(text))
    headings = []
    for block in units:
        for line in block.splitlines():
            m = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
            if m:
                headings.append(plain(m[1]))
    if not headings:
        raise ValueError('No title: ' + str(path))
    excerpt = ''
    for block in units:
        if re.match(r'^(#{1,6}\s|[-*]\s|\||>|<)', block):
            continue
        # A row of links is navigation, not a project description.
        without_links = re.sub(r'\[[^\]]*\]\([^)]*\)', '', block)
        if len(re.sub(r'[^\w]', '', without_links)) < 35:
            continue
        excerpt = plain(block)
        break
    if not excerpt:
        raise ValueError('No prose: ' + str(path))
    if len(excerpt) > 360:
        stops = list(re.finditer(r'[.!?](?:\s|$)', excerpt[:361]))
        end = stops[-1].start() + 1 if stops and stops[-1].start() >= 60 else 0
        excerpt = excerpt[:end] if end else excerpt[:360].rsplit(' ', 1)[0] + '...'
    return {'id': path.stem, 'title': headings[0], 'excerpt': excerpt,
            'headings': headings, 'terms': sorted(set(re.findall(r'[a-z0-9]+', ''.join(c for c in unicodedata.normalize('NFKD', plain(' '.join(units))) if not unicodedata.combining(c)).lower()))), 'path': path.as_posix(),
            'source_url': 'https://github.com/midya8/Midya-portfolio/blob/main/' + path.as_posix(),
            'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data)}

def catalog(root=ROOT):
    records = []
    for path in sorted((root / 'projects').glob('*.md')):
        if path.name in EXCLUDED:
            continue
        if path.is_symlink() or not re.fullmatch(r'[a-z0-9-]+\.md', path.name):
            raise ValueError('Unsupported project path: ' + str(path))
        records.append(extract(path.relative_to(root), path.read_bytes()))
    if not records:
        raise ValueError('No case studies')
    return {'schema': 'portfolio-catalog/v1', 'scope': 'Title, opening prose excerpt, section headings and deduplicated noncode source-prose terms from public project case studies. Not a fresh test or product-status report.', 'projects': records}

def render(data):
    esc = html.escape
    cards = []
    for p in data['projects']:
        cards.append(f'<article class="project" data-id="{esc(p["id"], quote=True)}"><p class="slug">{esc(p["id"])}</p><h2>{esc(p["title"])}</h2><p>{esc(p["excerpt"])}</p><a class="source" href="{esc(p["source_url"], quote=True)}">Read case study <span aria-hidden="true">↗</span><span class="sr">: {esc(p["id"])}</span></a></article>')
    script_tags = ''.join(f'<script defer src="catalog-data-{i}.js"></script>' for i in range((len(data['projects']) + 19) // 20))
    return '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Search Midya Rahmani's public AI and software case studies, with source-linked excerpts and a reproducible catalog."><title>Midya Rahmani | Project index</title><link rel="stylesheet" href="catalog.css"><script defer src="catalog-engine.js"></script>''' + script_tags + '''<script defer src="catalog-app.js"></script></head>
<body><a class="skip" href="#projects">Skip to projects</a><header><a href="https://github.com/midya8">MIDYA RAHMANI</a><a href="https://github.com/midya8/Midya-portfolio">Portfolio source ↗</a></header><main><section class="intro"><p class="eyebrow">A working collection / AI &amp; software</p><h1>Find the idea.<br>Then inspect the work.</h1><p class="lead">Small systems that make their reasoning visible. Search the public case studies, from exact inference and model checking to language-model tooling.</p><p class="boundary">This is a discovery index, not a new evaluation. Titles, opening excerpts, section headings and searchable prose terms come from the linked case studies. Open a case study for its scope, checks and limits. Excerpts may be shortened.</p></section>
<section class="search" aria-label="Find a project"><form id="search-form" hidden><label for="query">Search the case studies</label><div class="search-row"><input id="query" type="search" maxlength="256" autocomplete="off" placeholder="Try: CTC, fairness, retrieval"><button id="clear" type="button">Clear</button></div><p class="hint">Words match together, in any order. Case and accents do not matter. Matches include source prose beyond the short excerpts. No quality ranking.</p></form><p id="count" role="status" aria-live="polite">''' + str(len(data['projects'])) + ''' case studies, in project ID order.</p><p id="empty" hidden>No matching case studies. Try fewer words or clear the search.</p><noscript><p>JavaScript is off. Every case study is listed below; your browser's Find command still works.</p></noscript></section>
<section id="projects" class="projects" aria-label="Public case studies">''' + '\n'.join(cards) + '''</section><footer><h2>Evidence stays at the source.</h2><p>The index does not combine test counts, infer freshness or turn development controls into benchmarks. Existing case studies and their history are preserved.</p><p><a href="catalog.json">Download source-hash manifest</a> · <a href="https://github.com/midya8/Midya-portfolio/blob/main/CATALOG.md">Build contract and limits</a></p></footer></main></body></html>
'''

def outputs(root=ROOT):
    data = catalog(root)
    groups = [data['projects'][i:i + 20] for i in range(0, len(data['projects']), 20)]
    result = {'docs/index.html': render(data)}
    manifest = {k: v for k, v in data.items() if k != 'projects'}
    manifest['count'] = len(data['projects'])
    manifest['shards'] = [f'catalog-{i}.json' for i in range(len(groups))]
    result['docs/catalog.json'] = json.dumps(manifest, ensure_ascii=True, separators=(',', ':')) + '\n'
    for i, group in enumerate(groups):
        serialized = json.dumps(group, ensure_ascii=True, separators=(',', ':'))
        result[f'docs/catalog-{i}.json'] = serialized + '\n'
        prelude = 'globalThis.PORTFOLIO_CATALOG={projects:[]};\n' if i == 0 else ''
        result[f'docs/catalog-data-{i}.js'] = prelude + 'globalThis.PORTFOLIO_CATALOG.projects.push(...' + serialized + ');\n'
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    generated = outputs()
    stale = sorted(p for pattern in ('catalog-[0-9]*.json', 'catalog-data-[0-9]*.js') for p in (ROOT / 'docs').glob(pattern) if p.relative_to(ROOT).as_posix() not in generated)
    if args.check and stale:
        raise SystemExit('Stale generated output: ' + str(stale[0]))
    for path in stale:
        path.unlink()
    for name, value in generated.items():
        dest = ROOT / name
        if args.check:
            if not dest.exists() or dest.read_text() != value:
                raise SystemExit('Generated output differs: ' + name)
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(value)
    print('catalog verified' if args.check else 'catalog built')

if __name__ == '__main__':
    main()
