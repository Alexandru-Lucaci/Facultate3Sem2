from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# HTTPRequestHandler class


class HTTPRequestHandler(BaseHTTPRequestHandler):
    # GET
    def do_GET(self):
        # send response code
        self.send_response(200)

        # send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # send response
        response = {'message': 'Hello World!'}
        self.wfile.write(json.dumps(response).encode())

    # POST
    def do_POST(self):
        # get content length
        content_length = int(self.headers['Content-Length'])

        # get post data
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)

        # send response code
        self.send_response(200)

        # send headers
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # send response
        response = {'message': 'Received POST request!', 'data': data}
        self.wfile.write(json.dumps(response).encode())


# set up server
server_address = ('127.0.0.1', 8000)
httpd = HTTPServer(server_address, HTTPRequestHandler)

# run server
print('Starting server...')
httpd.serve_forever()
