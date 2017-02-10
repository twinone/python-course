import urllib.request
import lxml.html

QUERY_URL = 'https://pixabay.com/en/photos/?q=cat'

def query(s):
    return QUERY_URL + '+'.join(query.split(' '))


def httpget(url):
    """Devuelve un objecto de tipo bytes"""
    f = urllib.request.urlopen(url)
    return f.read()


def httpget(url):
    f = urllib.request.urlopen(url)
    return str(f.read(), 'utf-8')


dom =  lxml.html.fromstring(httpget(url))

for link in dom.xpath('//img/@src'): # select the url in href for all a tags(links)
    print(link)
