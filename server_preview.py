import http.server, os, sys

os.chdir("/Users/lorisfauville/Documents/Claude/Projects/SIte portfolio")
port = int(os.environ.get("PORT", 8080))
handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", port), handler)
httpd.serve_forever()
