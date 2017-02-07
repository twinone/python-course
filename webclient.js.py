import urllib.request


def httpget(url):
    f = urllib.request.urlopen(url)
    return str(f.read(), 'utf-8')


# Run webserver.py, then webclient.py
print(httpget("http://localhost:8080"))