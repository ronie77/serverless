# from http.server import BaseHTTPRequestHandler
# from cowpy import cow

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
#         self.wfile.write(message.encode())
#         return

from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
def hello(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")
