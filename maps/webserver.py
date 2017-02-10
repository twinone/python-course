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


def serve(ctype="application/json", content=DATA, addr=('0.0.0.0', 8080)):
    # A Handler handles incoming requests and provides a response
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # Send the STATUS 200 OK
            self.send_response(200)
            self.send_header('Content-Type:', ctype)
            self.end_headers()
            # Write the output (must be a bytes object)
            self.wfile.write(bytes(content, 'utf-8'))
    # create the server
    srv = socketserver.TCPServer(addr, Handler)


    print("serving at", addr)
    # infinite loop
    srv.serve_forever()

if __name__ == '__main__':
    serve()
    # code after this point will not be executed