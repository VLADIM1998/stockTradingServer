from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import pandas as pd
import json
# from main import main
from test import handle_request

hostName = "localhost"
serverPort = 8080

import time




class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        res = handle_request()
        print(res)     
        json_response = json.dumps(res)
        self.wfile.write(bytes(json_response, "utf-8"))


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")