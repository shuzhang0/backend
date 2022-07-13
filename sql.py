import decimal
import random
from decimal import Decimal

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 解决跨域的问题

import pymysql

# 配置数据库
con = pymysql.connect(
    host='47.101.69.44',
    user='root',
    password='123456',
    db='testsql',
    charset='utf8'
)

app = Flask(__name__)
CORS(app, supports_credentials=True)


# -------------------------for reference-------------------------- #


@app.route('/')
def sql_use():
    # 游标
    cursor = con.cursor()

    # 查询全部
    sql = "select * from user"
    count = cursor.execute(sql)
    users = cursor.fetchall()  # 获取全部数据
    for user in users:
        print(user)

    # 查询一条
    sql = "select * from user where user_id=1"
    count = cursor.execute(sql)
    user = cursor.fetchone()  # 获取一条数据
    print(user)

    # 新增数据
    name = "赵五"
    password = "1"
    sql = 'insert into user(username, password)values("%s","%s")' % (name, password)
    count = cursor.execute(sql)
    con.commit()  # 提交至数据库

    # 删除数据
    name = "赵五"
    sql = 'delete from user where username="%s"' % name
    count = cursor.execute(sql)
    con.commit()

    # 修改数据
    name = "aaa"
    password = "000"
    sql = 'update user set username="%s",password="%s" where username="%s"' % (name, password, name)
    count = cursor.execute(sql)
    con.commit()

    # 关闭
    cursor.close()
    con.close()

    return '000'


# -------------------------UTILS-------------------------- #


def trim_url(url):
    url = url[32:]
    print(url)
    return url


# -------------------------user-------------------------- #


def login(username, password):
    cursor = con.cursor()  # initiate
    sql = "select username, password from user"
    cursor.execute(sql)
    names = cursor.fetchall()  # get all
    for (name, pwd) in names:  # check
        print(name)
        if name == username:
            if pwd == password:
                cursor.close()  # close
                return 0  # user match
            else:
                cursor.close()  # close
                return 1  # user not right pwd

    cursor.close()  # close
    return -1  # user not exist


def regist(username, password, role):
    cursor = con.cursor()  # initiate
    sql = "select username from user"
    cursor.execute(sql)
    names = cursor.fetchall()  # get all username
    for (name,) in names:  # check for unique name
        print(name)
        if name == username:
            print('already exists')
            cursor.close()  # close
            return -1

    sql = 'insert into user(username, password)values("%s","%s")' % (username, password)
    cursor.execute(sql)
    user_id = username_to_id(username)
    sql = 'insert into user_role(user_id, role_id)values("%d","%d")' % (user_id, role)
    cursor.execute(sql)
    con.commit()  # 提交至数据库

    cursor.close()  # close
    return 0


def get_user_status(username):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    sql = "select role_id from user_role where user_id='%d'" % user_id
    cursor.execute(sql)
    role = cursor.fetchone()
    user_role = role[0]

    t = {'user_id': user_id, 'username': username, 'role': user_role}
    cursor.close()  # close
    return t


# !!!!! following functions for inner use !!!!! #


def username_to_id(username):
    cursor = con.cursor()  # initiate
    sql = "select user_id from user where username='%s'" % (username)
    cursor.execute(sql)
    user_id = cursor.fetchone()  # get one record
    # print(user_id[0])
    id = user_id[0]
    print(id)
    print("id now...")

    cursor.close()  # close
    return id


# -------------------------BOOKS-------------------------- #


def get_books(username):
    cursor = con.cursor()  # initiate
    # user_id = username_to_id(username)
    sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
          " from book_info "
    cursor.execute(sql)
    book_detail = cursor.fetchmany(20)  # get many record
    t = []
    for one_book in book_detail:
        sql = "select name from book_category where cate_id='%s'" % (one_book[7])   # category id -> category name
        cursor.execute(sql)
        cate = cursor.fetchone()

        slice = {'book_id': one_book[0], 'name': one_book[1], 'image_url': trim_url(one_book[2]),
                 'press': one_book[3], 'publish_date': one_book[4],
                 'author': one_book[5], 'price': one_book[6], 'category': cate[0]}  # prepare json data
        t.append(slice)

    cursor.close()  # close
    return t


def get_book_detail(book_id):
    cursor = con.cursor()  # initiate
    sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
          " from book_info where book_id='%s'" % (book_id)
    cursor.execute(sql)
    book_detail = cursor.fetchone()  # get one record
    # print(book_detail)
    t = []

    sql = "select name from book_category where cate_id='%s'" % (book_detail[7])   # category id -> category name
    cursor.execute(sql)
    cate = cursor.fetchone()

    slice = {'book_id': book_detail[0], 'name': book_detail[1], 'image_url': trim_url(book_detail[2]),
             'press': book_detail[3], 'publish_date': book_detail[4],
             'author': book_detail[5], 'price': book_detail[6], 'category': cate[0]}  # prepare json data
    t.append(slice)
    print(t)

    cursor.close()  # close
    return t


def add_book_rating(username, book_id, rating):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select * from book_ratings where user_id='%d' and book_id='%d'" % (user_id, book_id)
    cursor.execute(sql)
    book_rating = cursor.fetchone()
    if book_rating is None:
        sql = "insert into book_ratings(user_id, book_id, score) values('%d','%d','%d')" % (user_id, book_id, rating)
        cursor.execute(sql)
    else:
        sql = "update book_ratings set score='%d' where user_id='%d' and book_id='%d'" % (rating, user_id, book_id)
        cursor.execute(sql)

    con.commit()  # 提交至数据库
    cursor.close()  # close
    return 0


def get_book_ratings(book_id):
    cursor = con.cursor()  # initiate
    sql = "select user_id, score from book_ratings where book_id='%d'" % (book_id)
    cursor.execute(sql)
    book_ratings = cursor.fetchall()
    t = []
    for one_rating in book_ratings:
        user_id = one_rating[0]
        score = one_rating[1]
        sql = "select username from user where user_id='%d'" % (user_id)
        cursor.execute(sql)
        the_user = cursor.fetchone()
        username = the_user[0]
        slice = {'username': username, 'rating': score}
        t.append(slice)

    print(t)
    cursor.close()  # close
    return t


# -------------------------cart-------------------------- #


def get_cart(username):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select book_id, number from book_cart where user_id='%d'" % (user_id)
    cursor.execute(sql)
    cart_books = cursor.fetchall()
    t = []
    for one_book in cart_books:
        book_id = one_book[0]
        number = one_book[1]

        sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
              " from book_info where book_id='%s'" % (book_id)
        cursor.execute(sql)
        book_detail = cursor.fetchone()

        sql = "select name from book_category where cate_id='%s'" % (book_detail[7])   # category id -> category name
        cursor.execute(sql)
        cate = cursor.fetchone()

        slice = {'book_id': book_detail[0], 'name': book_detail[1], 'image_url': trim_url(book_detail[2]),
                 'press': book_detail[3], 'publish_date': book_detail[4],
                 'author': book_detail[5], 'price': book_detail[6], 'category': cate[0],
                 'number': number}  # prepare json data
        t.append(slice)
        print(t)

    cursor.close()  # close
    return t


def add_cart(username, book_id):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select * from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
    cursor.execute(sql)
    cart_item = cursor.fetchone()
    if cart_item is None:
        sql = "insert into book_cart(user_id, book_id, number) values('%d','%d',1)" % (user_id, book_id)
        cursor.execute(sql)
    else:
        sql = "update book_cart set number=number+1 where user_id='%d' and book_id='%d'" % (user_id, book_id)
        cursor.execute(sql)

    con.commit()  # 提交至数据库
    cursor.close()  # close
    return 0


def minus_cart(username, book_id):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select number from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
    cursor.execute(sql)
    cart_item = cursor.fetchone()
    if cart_item is not None:
        if cart_item[0] == 1:
            sql = "delete from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
            cursor.execute(sql)
        else:
            sql = "update book_cart set number=number-1 where user_id='%d' and book_id='%d'" % (user_id, book_id)
            cursor.execute(sql)
    else:
        return -1

    con.commit()  # 提交至数据库
    cursor.close()  # close
    return 0


def del_cart(username, book_id):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select number from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
    cursor.execute(sql)
    cart_item = cursor.fetchone()
    if cart_item is not None:
        sql = "delete from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
        cursor.execute(sql)
    else:
        return -1

    con.commit()  # 提交至数据库
    cursor.close()  # close
    return 0


# !!!!! following functions for inner use !!!!! #


def clear_cart(username):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select book_id from book_cart where user_id='%d'" % (user_id)
    cursor.execute(sql)
    cart_list = cursor.fetchall()
    for cart_item in cart_list:
        book_id = cart_item[0]
        sql = "delete from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
        cursor.execute(sql)

    con.commit()  # 提交至数据库
    cursor.close()  # close
    return 0


def get_cart_price(username):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    sql = "select book_id, number from book_cart where user_id='%d'" % (user_id)
    cursor.execute(sql)
    cart_books = cursor.fetchall()

    total_price = decimal.Decimal(0.00)  # total price
    for one_book in cart_books:
        book_id = one_book[0]
        number = one_book[1]
        # print(book_id)
        # print(number)
        sql = "select book_id, price from book_info where book_id='%d'" % (book_id)
        cursor.execute(sql)
        book_detail = cursor.fetchone()
        total_price += book_detail[1] * number
        print(total_price)

    print(total_price)
    cursor.close()  # close
    return total_price


# -------------------------orders-------------------------- #


def add_order(username):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    # step 1 : create an 'order' table record
    order_id = random.randint(10000001, 10009999)  # make a random order_id
    order_id = str(order_id)
    print(order_id)
    order_price = get_cart_price(username)  # get cart total price
    order_price = str(order_price)
    sql = "insert into orders(order_id, user_id, payment, status) " \
          "values('%s','%d','%s',0)" % (order_id, user_id, order_price)
    cursor.execute(sql)

    # step 2 : go through the 'book_cart' table and move to 'order_detail' table
    sql = "select book_id, number from book_cart where user_id='%d'" % (user_id)
    cursor.execute(sql)
    cart_list = cursor.fetchall()
    for cart_item in cart_list:
        book_id = cart_item[0]
        mount = cart_item[1]
        sql = "delete from book_cart where user_id='%d' and book_id='%d'" % (user_id, book_id)
        cursor.execute(sql)
        sql = "insert into order_detail(order_id, book_id, mount) " \
              "values('%s','%d','%d')" % (order_id, book_id, mount)
        cursor.execute(sql)

    t = {'order_id': order_id, 'user_id': user_id, 'payment': order_price, 'status': 0}
    con.commit()  # 提交至数据库
    cursor.close()  # close
    return t


def get_user_orders(username):
    cursor = con.cursor()  # initiate
    user_id = username_to_id(username)
    print(user_id)
    sql = "select order_id, user_id, payment, payment_type, status from orders where user_id='%d'" % (user_id)
    cursor.execute(sql)
    user_orders = cursor.fetchall()
    t = []

    for one_order in user_orders:
        slice = {'order_id': one_order[0], 'user_id': one_order[1], 'payment': one_order[2],
                 'payment_type': one_order[3], 'status': one_order[4]}  # prepare json data
        t.append(slice)
        print(t)

    cursor.close()  # close
    return t


def get_order_detail(order_id):
    cursor = con.cursor()  # initiate

    sql = "select book_id, mount from order_detail where order_id='%s'" % (order_id)
    cursor.execute(sql)
    order_books = cursor.fetchall()
    t = []
    for one_book in order_books:
        book_id = one_book[0]
        mount = one_book[1]
        sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
              " from book_info where book_id='%s'" % (book_id)
        cursor.execute(sql)
        book_detail = cursor.fetchone()

        total_price = book_detail[6] * mount  # total price for the specific book

        sql = "select name from book_category where cate_id='%s'" % (book_detail[7])   # category id -> category name
        cursor.execute(sql)
        cate = cursor.fetchone()

        slice = {'book_id': book_detail[0], 'name': book_detail[1], 'image_url': trim_url(book_detail[2]),
                 'press': book_detail[3], 'publish_date': book_detail[4],
                 'author': book_detail[5], 'price': book_detail[6], 'category': cate[0],
                 'mount': mount,
                 'book_total_price': total_price}  # prepare json data
        t.append(slice)
        print(t)

    cursor.close()  # close
    return t


# -------------------------Admin-------------------------- #


def admin_get_all_users():
    cursor = con.cursor()  # initiate

    sql = "select user_id, username, nickname, password, gender, email, phone from user"
    cursor.execute(sql)
    user_list = cursor.fetchmany(20)  # get many record
    t = []
    for one_user in user_list:
        slice = {'user_id': one_user[0], 'username': one_user[1], 'nickname': one_user[2], 'password': one_user[3],
                 'gender': one_user[4], 'email': one_user[5], 'phone': one_user[6]}  # prepare json data
        t.append(slice)

    cursor.close()  # close
    return t


def admin_get_all_books():
    cursor = con.cursor()  # initiate

    sql = sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
                " from book_info "
    cursor.execute(sql)
    book_detail = cursor.fetchmany(20)  # get many record
    t = []

    for one_book in book_detail:
        sql = "select name from book_category where cate_id='%s'" % (one_book[7])   # category id -> category name
        cursor.execute(sql)
        cate = cursor.fetchone()

        slice = {'book_id': one_book[0], 'name': one_book[1], 'image_url': trim_url(one_book[2]),
                 'press': one_book[3], 'publish_date': one_book[4],
                 'author': one_book[5], 'price': one_book[6], 'category': cate[0]}  # prepare json data
        t.append(slice)

    cursor.close()  # close
    return t


def admin_get_all_orders():
    cursor = con.cursor()  # initiate

    sql = "select order_id, user_id, payment, payment_type, status, post_fee" \
          " from orders "
    cursor.execute(sql)
    order_list = cursor.fetchmany(20)  # get many record
    t = []
    for one_order in order_list:
        slice = {'order_id': one_order[0], 'user_id': one_order[1], 'payment': one_order[2],
                 'payment_type': one_order[3], 'status': one_order[4], 'post_fee': one_order[5]}  # prepare json data
        t.append(slice)

    cursor.close()  # close
    return t


# -------------------------for user's taste-------------------------- #


def get_books_tops():
    cursor = con.cursor()  # initiate
    sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
          " from book_info where size is not null"
    cursor.execute(sql)
    book_detail = cursor.fetchmany(20)  # get many record
    t = []
    for one_book in book_detail:
        sql = "select name from book_category where cate_id='%s'" % (one_book[7])   # category id -> category name
        cursor.execute(sql)
        cate = cursor.fetchone()

        slice = {'book_id': one_book[0], 'name': one_book[1], 'image_url': trim_url(one_book[2]),
                 'press': one_book[3], 'publish_date': one_book[4],
                 'author': one_book[5], 'price': one_book[6], 'category': cate[0]}  # prepare json data
        t.append(slice)

    cursor.close()  # close
    return t


def get_books_for_user():
    cursor = con.cursor()  # initiate
    sql = "select book_id, name, image_url, press, publish_date, author, price, book_category_id" \
          " from book_info where size is not null"
    cursor.execute(sql)
    book_detail = cursor.fetchmany(20)  # get many record
    t = []
    for one_book in book_detail:
        sql = "select name from book_category where cate_id='%s'" % (one_book[7])   # category id -> category name
        cursor.execute(sql)
        cate = cursor.fetchone()

        slice = {'book_id': one_book[0], 'name': one_book[1], 'image_url': trim_url(one_book[2]),
                 'press': one_book[3], 'publish_date': one_book[4],
                 'author': one_book[5], 'price': one_book[6], 'category': cate[0]}  # prepare json data
        t.append(slice)

    cursor.close()  # close
    return t





















# -------------------------THE END-------------------------- #


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
