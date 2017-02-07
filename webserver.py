import http.server
import socketserver


DATA = """
{
  "name": "John",
  "fav_num": 6.2831,
  "test": null,
  "cities": [
    "Barcelona",
    "London"
  ]
}
"""

def write(h, ctype, str):
    h.send_response(200)
    h.send_header('Content-Type:', ctype)
    h.end_headers()
    h.wfile.write(bytes(str, 'utf-8'))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        write(self, "text/html", DATA)


def serve(addr=('0.0.0.0', 8080)):

    srv = socketserver.TCPServer(addr, Handler)

    print("serving at", addr)
    srv.serve_forever()


serve()