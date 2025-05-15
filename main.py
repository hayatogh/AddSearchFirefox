#!/usr/bin/env python3
from pathlib import Path
from string import Template
import http.server
import shutil
import socketserver
import sys
import threading
import tomllib

GenDir = Path('generated')


def clean():
    if GenDir.is_dir():
        shutil.rmtree(GenDir)


def gen():

    def filterURL(s):
        return s.replace('%s', '{searchTerms}').replace('&', '&amp;')

    TemplateDir = Path('template')

    with open('searches.toml', 'rb') as f:
        searches = tomllib.load(f)
    with open(TemplateDir / 'search.xml') as f:
        search = f.read()
    with open(TemplateDir / 'link.html') as f:
        link = f.read()
    with open(TemplateDir / 'index.html') as f:
        index = f.read()

    GenDir.mkdir()
    links = ""

    for i, (k, v) in enumerate(searches.items()):
        f = str(i) + '.xml'
        url = filterURL(v['URL'])
        s = Template(search).substitute(name=k, icon=v['icon'], URL=url)
        print(s, file=open(GenDir / f, 'w'))
        l = Template(link).substitute(name=k, path=f)
        links += l

    ind = Template(index).substitute(links=links)
    print(ind, file=open(GenDir / 'index.html', 'w'))


def serve():

    class GeneratedDirHandler(http.server.SimpleHTTPRequestHandler):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs, directory=GenDir)

    server = socketserver.TCPServer(("localhost", 0), GeneratedDirHandler)
    _, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)

    server_thread.start()
    input("Serving at http://localhost:" + str(port) + "\nPress Enter to Exit.\n")
    server.shutdown()


def main():
    clean()
    if len(sys.argv) == 2 and sys.argv[1] == 'clean':
        return
    gen()
    serve()


if __name__ == '__main__':
    main()
