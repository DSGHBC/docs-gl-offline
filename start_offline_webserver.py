import http.server
import socketserver
import os

os.chdir('htdocs')


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '': 'text/html'}


host = "localhost"
port = 8000
with socketserver.ThreadingTCPServer((host, port), Handler) as httpd:
    httpd.request_queue_size = 10
    print(f"serving docs at http://{host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()
