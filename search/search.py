import os
import re
import urllib.request
import webbrowser
from os import listdir
from os.path import isfile, join


QUERY_URL = 'https://pixabay.com/en/photos/?q={0}&pagi={1}'

HTML = """
<html>
<body>
{0}
</body>
</html>
"""


def query(s, p):
    """Devuelve la query a partir de unas palabras"""
    q = '+'.join(s.split(' '))
    return QUERY_URL.format(q, p)


def httpget(url):
    """De webclient.py. NO se pasa a string porque a veces nos interesa tener los datos binarios"""
    f = urllib.request.urlopen(url)
    return f.read()


def getlinks_parser(s, n):
    pass


def save(key, l):
    pass


def open_html(key):
    pass


def do_search(key, num):
    pass
