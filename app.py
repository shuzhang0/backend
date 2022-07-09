from flask import Flask

app = Flask(__name__)


@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'

@app.route('/')
def index():
    return f'Hello!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, deBug=True)
