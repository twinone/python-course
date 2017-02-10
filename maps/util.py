from math import cos, asin, sqrt
import webbrowser
import os

def distance(a, b):
    """Get the distance between two coordinates in kilometers"""
    # see
    # http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula

    (a1, a2) = a
    (b1, b2) = b
    p = 0.017453292519943295
    a = (0.5 - cos((b1 - a1) * p) / 2 + cos(a1 * p) * cos(b1 * p) *
         (1 - cos((b2 - a2) * p)) / 2)
    res = 12742 * asin(sqrt(a))


    return res


BASE_URL = 'https://www.google.com/maps/embed/v1/directions?key=AIzaSyBNIp87_yb-HNAdRnd-XTH5kWH0Xz0eDss&origin={0}&destination={1}&mode=bicycling'
TEMPLATE = """<html><body style="margin:0"><iframe src="{0}" style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;"></iframe></body></html>"""

def maps(a, b, filename="index.html", autoopen=True):
    """Generate a google maps with the route from a to b"""

    url = BASE_URL.format(a, b)
    text = TEMPLATE.format(url)
    with open(filename, "w") as text_file:
        text_file.write(text)
    if autoopen:
        webbrowser.open(os.path.realpath("./"+filename))

def tuplestring(t):
    (a, b) = t
    return str(a) + str(b)

