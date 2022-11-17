from flask import Flask, Response
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return Response("<h1>Flask</h1><p>You visited: /%s</p>" % (path), mimetype="text/html")


# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello World!"


# if __name__ == "__main__":
#     app.run()
