from http.server import BaseHTTPRequestHandler, HTTPServer
import redis

redis_host = os.environ.get('REDIS_IP')
redis_port = 6379
redis_password = ""
hostName = "0.0.0.0"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        try:

            r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

            r.set("msg:hello", "Hello Redis!!!")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            msg = r.get("msg:hello")
            self.wfile.write(bytes('<div style="text-align: center; padding-top: 200px"><h1>' + msg + '</h1></div>', "utf-8"))

        except Exception as e:
            print(e)

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")