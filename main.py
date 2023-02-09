#!/usr/bin/env python3

import http.server
import json
import socketserver
import xml.etree.ElementTree as ET

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def filterURL(s):
    return s.replace('%s', '{searchTerms}')

with open('searches.json') as f:
    searches = json.load(f)

index = open('index.html', 'w')
index.write('<head>\n')

for i, s in enumerate(searches):
    tree = ET.parse('template/template.xml')
    root = tree.getroot()
    root.find('{http://a9.com/-/spec/opensearch/1.1/}ShortName').text = s['name']
    root.find('{http://a9.com/-/spec/opensearch/1.1/}Image').text = s['icon']
    root.find('{http://a9.com/-/spec/opensearch/1.1/}Url').set('template', filterURL(s['URL']))
    tree.write(str(i) + '.xml')

    index.write("""<link
  rel="search"
  type="application/opensearchdescription+xml"
  title="%s"
  href="/%s" />\n""" % (s['name'], str(i) + '.xml'))

index.write('</head>')
index.close()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
