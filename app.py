import json
from json import JSONDecodeError

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 解决跨域的问题

import sql

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def start():
    return f'connect! success!!'

@app.route('/hello/<username>')
def hello(username):
    return f'Hello {username}!'


# -------------------------user-------------------------- #


@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        data = json.loads(request.get_data(as_text=True))  # get json data
        print("login...")
        print(data)

        result = sql.login(data['username'], data['password'])
        print(result)

        t = {
            "status": result
        }
        return jsonify(t)  # -1/0/1
    except JSONDecodeError as e:
        t = {
            "status": 400
        }
        return jsonify(t)


@app.route('/regist', methods=['POST', 'GET'])
def register():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("register...")
    print(data)

    result = sql.regist(data['username'], data['password'], data['role'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # -1/0


@app.route('/login/get_user_status', methods=['POST', 'GET'])
def user_status():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("status getting...")
    print(data)

    the_user_status = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_user_status(data['username'])

    the_user_status['data'] = data
    return jsonify(the_user_status)  # -1/0


# -------------------------BOOKS-------------------------- #


@app.route('/get_books', methods=['POST', 'GET'])
def get_books():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print(data)

    the_book_info = {  # prepare to send
        'code': 200,
        'all_books': [],
        'tops_books':[],
        'cus_books':[]
    }

    all_books = sql.get_books(data['username'])
    tops_books = sql.get_books_tops()
    cus_books = sql.get_books_for_user(data['username'])

    the_book_info["all_books"] = all_books
    the_book_info["tops_books"] = tops_books
    the_book_info["cus_books"] = cus_books
    return jsonify(the_book_info)  # json


@app.route('/get_book_detail', methods=['POST', 'GET'])
def get_book_detail():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("book detail...")
    print(data)

    the_book_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_book_detail(data['book_id'])

    the_book_info["data"] = data
    return jsonify(the_book_info)  # json


@app.route('/add_book_rating', methods=['POST', 'GET'])
def add_book_rating():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("rating...")
    print(data)

    result = sql.add_book_rating(data['username'], data['book_id'], data['rating'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # 0


@app.route('/get_book_ratings', methods=['POST', 'GET'])
def get_book_ratings():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("get ratings...")
    print(data)

    the_book_ratings = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_book_ratings(data['book_id'])

    the_book_ratings["data"] = data
    return jsonify(the_book_ratings)


# -------------------------cart-------------------------- #


@app.route('/get_cart', methods=['POST', 'GET'])
def get_cart():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("get cart...")
    print(data)

    the_cart_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_cart(data['username'])

    the_cart_info["data"] = data
    return jsonify(the_cart_info)  # json


@app.route('/add_cart', methods=['POST', 'GET'])
def add_cart():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("add to cart...")
    print(data)

    result = sql.add_cart(data['username'], data['book_id'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # 0


@app.route('/minus_cart', methods=['POST', 'GET'])
def modi_cart():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("minus 1...")
    print(data)

    result = sql.minus_cart(data['username'], data['book_id'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # 0


@app.route('/del_cart', methods=['POST', 'GET'])
def del_cart():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("delete-from cart...")
    print(data)

    result = sql.del_cart(data['username'], data['book_id'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # 0


# -------------------------orders-------------------------- #


@app.route('/add_order', methods=['POST', 'GET'])
def add_orders():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("add order and clear user's cart...")
    print(data)

    the_order_create = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.add_order(data['username'])
    the_order_create['data'] = data

    return jsonify(the_order_create)  # JSON


@app.route('/get_user_orders', methods=['POST', 'GET'])
def get_user_orders():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("getting user's orders...")
    print(data)

    the_orders_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_user_orders(data['username'])

    the_orders_info["data"] = data
    return jsonify(the_orders_info)  # json


@app.route('/get_order_detail', methods=['POST', 'GET'])
def get_order_detail():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print("getting order details...")
    print(data)

    the_order_detail = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_order_detail(data['order_id'])

    the_order_detail["data"] = data
    return jsonify(the_order_detail)  # json


# -------------------------Admin-------------------------- #


@app.route('/admin/get_all_users', methods=['POST', 'GET'])
def admin_get_users():
    # data = json.loads(request.get_data(as_text=True))  # get json data

    the_user_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.admin_get_all_users()

    the_user_info["data"] = data
    return jsonify(the_user_info)  # json


@app.route('/admin/get_all_books', methods=['POST', 'GET'])
def admin_get_books():
    # data = json.loads(request.get_data(as_text=True))  # get json data

    the_book_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.admin_get_all_books()

    the_book_info["data"] = data
    return jsonify(the_book_info)  # json


@app.route('/admin/get_all_orders', methods=['POST', 'GET'])
def admin_get_orders():
    # data = json.loads(request.get_data(as_text=True))  # get json data

    the_order_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.admin_get_all_orders()

    the_order_info["data"] = data
    return jsonify(the_order_info)  # json


# -------------------------for user's taste-------------------------- #


@app.route('/get_books_tops', methods=['POST', 'GET'])
def get_books_tops():
    #data = json.loads(request.get_data(as_text=True))  # get json data

    the_book_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_books_tops()

    the_book_info["data"] = data
    return jsonify(the_book_info)  # json


@app.route('/get_books_for_user', methods=['POST', 'GET'])
def get_books_for_user():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print(data)

    the_book_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_books_for_user(data['username'])

    the_book_info["data"] = data
    return jsonify(the_book_info)  # json


# -------------------------Website Management-------------------------- #


@app.route('/admin/get_orders_sum', methods=['POST', 'GET'])
def get_orders_sum():
    # data = json.loads(request.get_data(as_text=True))  # get json data

    the_book_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.get_orders_sum()

    the_book_info["data"] = data
    return jsonify(the_book_info)  # json


# -------------------------Addition for Admin-------------------------- #


@app.route('/modify_user', methods=['POST', 'GET'])
def modify_user():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print(data)

    result = sql.modify_user(data['username'], data['password'], data['nickname'],
                             data['gender'], data['email'], data['phone'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # 0


@app.route('/admin/del_user', methods=['POST', 'GET'])
def del_user():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print(data)

    result = sql.del_user(data['username'])
    print(result)

    t = {
        "status": result
    }
    return jsonify(t)  # 0


# -------------------------Search for Books-------------------------- #


@app.route('/search_books', methods=['POST', 'GET'])
def search_books():
    data = json.loads(request.get_data(as_text=True))  # get json data
    print(data)

    the_book_info = {  # prepare to send
        'code': 200,
        'data': []
    }

    data = sql.search_books(data['keyword'], data['type'])

    the_book_info["data"] = data
    return jsonify(the_book_info)  # json


# -------------------------THE END-------------------------- #


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
