import asyncio
import http.server
import socketserver
import json

from controller import request_handler
from model.response import Response

PORT = 8000


def send_response(handler, response, message):
    if message is None:
        message = response.name
    handler.send_response(response.value)
    handler.send_header('Content-type', 'text/json')
    handler.end_headers()

    output_data = {'message': message}
    output_json = json.dumps(output_data)

    handler.wfile.write(output_json.encode('utf-8'))
    return


async def call_controller(input_data, is_admin, method):
    if method == 'get_all':
        response, message = await request_handler.get_all(input_data, is_admin)
    elif method == 'update':
        response, message = await request_handler.update(input_data, is_admin)
    elif method == 'delete':
        response, message = await request_handler.delete(input_data, is_admin)
    elif method == 'create':
        response, message = await request_handler.create(input_data, is_admin)
    else:
        response = Response.method_not_found
        message = 'Invalid method!'
    return message, response


class RequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])

        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None

        print(input_data)

        # todo decode token
        #  see if the user is the admin
        decoded_token = {
            'is_admin': True
        }

        if 'method' not in input_data:
            send_response(self, Response.invalid_request, 'Field "method" not specified!')
            return

        method = input_data['method']
        is_admin = decoded_token['is_admin']

        loop = asyncio.get_event_loop()
        coroutine = call_controller(input_data, is_admin, method)

        message, response = loop.run_until_complete(coroutine)

        send_response(self, response, message)


Handler = RequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Starting http://0.0.0.0:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping by Ctrl+C")
    httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`
