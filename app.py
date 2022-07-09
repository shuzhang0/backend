from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 解决跨域的问题

app = Flask(__name__)

'''配置数据库
app.config['SECRET_KEY'] = 'hard to guess'  # 一个字符串，密码。也可以是其他如加密过的

# 在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
# "mysql://账号:密码@数据库ip地址:端口号/数据库名"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@47.101.69.44:3306/books'

# 设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # 实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能'''


@app.route('/test', methods=['post'])
def test():
    data = request.get_json(silent=True)
    print(data['aa'])  # 123


@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'

'''
# 验证是否连接成功
@app.route('/')
def hello_word():
    engine = db.get_engine()
    conn = engine.connect()
    conn.close()  # 跟open函数一样，可以用with语句
    with engine.connect() as conn:
        result = conn.execute('select 1')  # 这两步打开数据库并且创建表
        print(result.fetchone())  # 打印一条数据
    return "hello, word"'''


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        print("post")
        # user = request.form['username']
        return jsonify({'status': '0', 'errmsg': 'post'})
    else:
        print("get")
        # user = request.args.get('username')  # GET方法获取数据，args是包含表单参数对及其对应值对的列表的字典对象。
        return jsonify({'status': '0', 'errmsg': 'get'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
