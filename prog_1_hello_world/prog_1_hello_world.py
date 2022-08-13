from flask import Flask

app = Flask(__name__)


@app.route('/')
def upload_file():
    return "<h1>hello world</h1>"


@app.route('/<name>')
def func2(name):
    str = "hello "+name
    return str


if __name__ == '__main__':
    app.run()
