from flask import Flask, request, redirect, url_for, jsonify

app = Flask(__name__)


@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'


@app.route('/')
def index():
    return f'Hello!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("post")
        # user = request.form['username']
        return jsonify({'status': '0', 'errmsg': 'post登录成功！'})
    else:
        print("get")
        # user = request.args.get('username')  # GET方法获取数据，args是包含表单参数对及其对应值对的列表的字典对象。
        return jsonify({'status': '0', 'errmsg': 'get登录成功！'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, deBug=True)
