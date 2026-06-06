import http.server
import os

os.chdir("/Users/usama.shakeel/Downloads/codex podium 8")

class Handler(http.server.SimpleHTTPRequestHandler):
    pass

with http.server.HTTPServer(("", 3456), Handler) as httpd:
    httpd.serve_forever()
