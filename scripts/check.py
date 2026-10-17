#!/usr/bin/env python3
"""Check real crawl paths, metadata, structured data, assets and fragment links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import collections
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids=[]; self.links=[]; self.h1=0; self.canon=[]; self.desc=[]; self.noindex=False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag=='h1': self.h1+=1
        if tag in ('a','link') and a.get('href'): self.links.append(a['href'])
        if tag in ('img','script') and a.get('src'): self.links.append(a['src'])
        if tag=='link' and a.get('rel')=='canonical': self.canon.append(a['href'])
        if tag=='meta' and a.get('name')=='description': self.desc.append(a.get('content',''))
        if tag=='meta' and a.get('name')=='robots' and 'noindex' in a.get('content',''): self.noindex=True

def path_file(path):
    if path in ('','/'): return ROOT/'index.html'
    p=ROOT/unquote(path).lstrip('/')
    if not p.suffix: p=p.with_suffix('.html')
    return p

def main():
    errors=[]; pages={}; titles=[]
    for p in ROOT.glob('*.html'):
        text=p.read_text(); page=Page(text); pages[p]=page
        if p.name!='kontakt.html':
            if page.h1!=1: errors.append(f'{p.name}: {page.h1} H1 headings')
            if not page.noindex and len(page.desc)!=1: errors.append(f'{p.name}: description')
            if not page.noindex:
                expected='https://biurobil.pl/'+('' if p.name=='index.html' else p.stem)
                if page.canon!=[expected]: errors.append(f'{p.name}: canonical {page.canon}')
            title=re.search(r'<title>(.*?)</title>',text,re.S)
            if not title: errors.append(f'{p.name}: missing title')
            else: titles.append(title[1])
        if len(page.ids)!=len(set(page.ids)): errors.append(f'{p.name}: duplicate IDs')
        for data in re.findall(r'<script type="application/ld\+json">(.*?)</script>',text,re.S):
            try: json.loads(data)
            except ValueError: errors.append(f'{p.name}: invalid JSON-LD')
    for p,page in pages.items():
        for url in page.links:
            parts=urlsplit(url)
            if parts.scheme in ('mailto','tel','data'): continue
            if parts.netloc and parts.netloc!='biurobil.pl': continue
            target=p if not parts.path else path_file(parts.path)
            if not target.exists(): errors.append(f'{p.name}: broken link {url}')
            elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                errors.append(f'{p.name}: missing anchor {url}')
    for title,count in collections.Counter(titles).items():
        if count>1: errors.append(f'Duplicate title: {title}')
    for loc in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        p=path_file(urlsplit(loc.text).path)
        if p not in pages or pages[p].noindex: errors.append('Bad sitemap URL '+loc.text)
    assert not errors, '\n'.join(errors)
    print(f'PASS: {len(pages)} pages; local links, anchors, titles, H1, canonicals, JSON-LD and sitemap.')

if __name__=='__main__': main()
