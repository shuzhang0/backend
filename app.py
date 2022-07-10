from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 解决跨域的问题

app = Flask(__name__)
CORS(app, supports_credentials=True)

# 配置数据库
app.config['SECRET_KEY'] = 'hard to guess'  # 一个字符串，密码。也可以是其他如加密过的

# 在此登录的是root用户，要填上密码如123456，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
# "mysql://账号:密码@数据库ip地址:端口号/数据库名"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@47.101.69.44:3306/testsql'

# 设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # 实例化数据库对象，它提供访问Flask-SQLAlchemy的所有功能


# 创建orm模型---
class mmm(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)

#db.drop_all()
#db.create_all()

@app.route('/mmm')
def mmm_view():
    #1. 添加数据
    # sql语句为 insert table mmm value （xxx），这里不用
    #之前创建了mmm类对象，所以直接调用即可
    article = mmm(title= "l", content="dddd")

    #数据添加
    db.session.add(article)
    #数据提交
    db.session.commit()
    #最后进行返回操作
    return "数据操作成功"


@app.route('/')
def hello_word():
    return "hello, word"


@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'


@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        print("post")
        data = request.get_json(silent=True)
        print(data['aa'])  # 123
        return data['aa']
    else:
        print("get")
        return "get"


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

    per_one=mmm(title='no', content='000')

    app.run(host='0.0.0.0', port=5000, debug=True)
