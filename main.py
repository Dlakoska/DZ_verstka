from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

host_name = 'localhost'
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    filename = "dz.html"

    def get_html_content(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            context = f.read()
        return context

    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        print(query)
        page_content = self.get_html_content()
        self.send_response(200)
        self.send_header('Content-type', "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == '__main__':
    webServer = HTTPServer((host_name, server_port), MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")
