#!/usr/bin/env python3
"""Render plain HTML for GitHub Pages. No third-party dependencies or runtime JS."""
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'site-src'
TOKEN = re.compile(r'{{\s*([\w:-]+)\s*}}')

def render(text, settings, stack=()):
    def substitute(match):
        key = match[1]
        if key.startswith('include:'):
            name = key.split(':', 1)[1]
            if name in stack:
                raise ValueError('Circular include: ' + name)
            return render((SOURCE / 'partials' / (name + '.html')).read_text(), settings, stack + (name,)).rstrip()
        if key not in settings:
            raise ValueError('Unknown setting: ' + key)
        return str(settings[key])
    return TOKEN.sub(substitute, text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if committed HTML differs from its source')
    args = parser.parse_args()
    settings = json.loads((SOURCE / 'settings.json').read_text())
    stale = []
    for source in sorted((SOURCE / 'pages').glob('*.html')):
        output = render(source.read_text(), settings)
        if '{{' in output:
            raise ValueError('Unresolved template in ' + source.name)
        target = ROOT / source.name
        if args.check:
            if not target.exists() or target.read_text() != output:
                stale.append(source.name)
        else:
            target.write_text(output)
    if stale:
        print('Run python3 scripts/build.py; stale HTML: ' + ', '.join(stale))
        return 1
    print('HTML is up to date.' if args.check else 'Static HTML generated.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
