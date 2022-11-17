from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"


# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello World!"


# if __name__ == "__main__":
#     app.run()
