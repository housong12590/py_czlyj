from flask import Flask, url_for

app = Flask(__name__)


@app.route("/", methods=['GET'], endpoint='index1')
def index():
    print(url_for('index1'))
    return "GET"


@app.route("/", methods=['POST'], endpoint='index2')
def index():
    print(url_for('index2'))
    return "POST"


@app.route('/', methods=['PUI'], endpoint='index3')
def index():
    return "PUT"


@app.route('/', methods=['DELETE'], endpoint='index4')
def index():
    return "DELETE"


if __name__ == '__main__':
    app.run()
