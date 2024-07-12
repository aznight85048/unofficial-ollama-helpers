import http.server
import socketserver
import requests

PORT = 11435  # Change this to your desired port for the proxy server
TARGET = "http://127.0.0.1:11434"

class Proxy(http.server.SimpleHTTPRequestHandler):

    def _set_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")

    def do_GET(self):
        url = TARGET + self.path
        response = requests.get(url, headers=self._filter_headers())
        self._send_response(response)

    def do_POST(self):
        url = TARGET + self.path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = requests.post(url, data=post_data, headers=self._filter_headers())
        self._send_response(response)

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self._set_cors_headers()
        self.end_headers()

    def _filter_headers(self):
        """ Filter headers to include only those that are necessary. """
        filtered_headers = {}
        for header, value in self.headers.items():
            if header in ["Content-Type", "Authorization", "User-Agent"]:
                filtered_headers[header] = value
        return filtered_headers

    def _send_response(self, response):
        self.send_response(response.status_code)
        self._set_cors_headers()
        for header, value in response.headers.items():
            if header.lower() not in ["content-encoding", "transfer-encoding", "content-length"]:
                self.send_header(header, value)
        self.end_headers()
        self.wfile.write(response.content)

if __name__ == "__main__":
    proxy_url = f"http://127.0.0.1:{PORT}"
    print("==================================================")
    print("Starting Ollama Serve Proxy to Avoid CORS Errors")
    print("==================================================")
    print(f"Ollama Target Server URL: {TARGET}")
    print(f"Proxy Server Running at : {proxy_url}")
    print("Note: This proxy server is designed to avoid CORS errors.")
    print("Potential Risks: Be cautious with the use of open CORS policy as it allows requests from any origin.")
    print("==================================================")
    print(f"Serving at port {PORT}")
    with socketserver.TCPServer(("", PORT), Proxy) as httpd:
        httpd.serve_forever()