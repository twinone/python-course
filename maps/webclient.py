import urllib.request


def httpget(url="http://localhost:8080"):
    f = urllib.request.urlopen(url)
    return str(f.read(), 'utf-8')


# Run webserver.py, then webclient.py
if __name__ == '__main__':
    print(httpget("http://localhost:8080"))