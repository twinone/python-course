import urllib.request
import webbrowser
import re
import os


QUERY_URL = 'https://pixabay.com/en/photos/?q={0}&pagi={1}'


def query(s, p):
    """Devuelve la query a partir de unas palabras"""
    q = '+'.join(s.split(' '))
    return QUERY_URL.format(q, p)

def httpget(url):
    """De webclient.py. NO se pasa a string porque a veces nos interesa tener los datos binarios"""
    f = urllib.request.urlopen(url)
    return f.read()


def getlinks_parser(s, n):
    """
    Dada una query devuelve los n links de las imagenes mas cercanas
    Parser es menos eficiente que regex, pero siempre es correcto
    """

    p = 0
    res = []
    while len(res) < n:

        p += 1
        print("Getting page", n)
        q = query(s, p)
        data = str(httpget(q))

        """
        dom = lxml.html.fromstring(data)
        res += [l for l in  dom.xpath('//img/@src')
                if re.findall('https.*png', l)
                or re.findall('https.*jpg', l)]
        """
        res += re.findall('<img.*?src="(https:\S*?\.jpg|https:\S*? \.png)".*?>', data)


    return res[:n]

def save(key, l):
    """Guarda las imagenes de una query"""
    # 1. Crear carpeta llamada q
    # 2. guardar las imagenes como q01.png/jpg
    for i, x in enumerate(l):
        name = key + str(i+1).zfill(3)


        if re.search("jpg", x):
            name += ".jpg"
        else:
            name += ".png"

        path = os.getcwd() + "/"+key+"/"
        if not os.path.exists(path):
            os.makedirs(path)
        urllib.request.urlretrieve(x,  path + name)

from os import listdir
from os.path import isfile, join
import util

HTML = """
<html>
<body>
{0}
</body>
</html>
"""

def open_html(key):
    paths = ["./" + key + "/" + f for f in listdir(key) if isfile(join(key, f))]
    content = ""
    for p in paths:
        content += """<img src="{0}" style="width:100%"></img><br><br> """.format(p)
    html = HTML.format(content)
    f = open("index.html", "w")
    f.write(content)
    f.close()
    webbrowser.get("firefox").open("./index.html")

def do_search(key, num):
    res = getlinks_parser(key, num)
    save(key, res)
    open_html(key)

