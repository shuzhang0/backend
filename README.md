# backend
    使用python的flask框架搭建的纯后端项目，部署在阿里云服务器上
## 文件说明
    app.py 规定了路由函数，被前端调用
    sql.py 中的函数被app.py调用，实现对数据库的操作
## 接口设计
[登录](#登录)  
[注册](#注册)  
[获取用户角色等信息](#获取用户角色等信息)  
[获取图书列表(+top20+个性推荐)](#获取图书列表(+top20+个性推荐))  
[获取某图书详情](#获取某图书详情)  
[评价图书/更新评价](#评价图书/更新评价)  
[获取图书所有评价](#获取图书所有评价)  
[获取用户购物车](#获取用户购物车)  
[购物车新加图书/数量+1](#购物车新加图书/数量+1)  
[购物车某图书数量-1](#购物车某图书数量-1)  
[删除购物车某图书](#删除购物车某图书)  
[生成订单(清空购物车)](#生成订单(清空购物车))  
[获取用户订单](#获取用户订单)  
[查看订单详情](#查看订单详情)  
[管理员-查看所有用户](#管理员-查看所有用户)  
[管理员-查看所有图书](#管理员-查看所有图书)  
[管理员-查看所有订单](#管理员-查看所有订单)  
[获取全站TOP20图书(被get_books调用)](#获取全站TOP20图书(被get_books调用))  
[获取给用户个性推荐图书(被get_books调用)](#获取给用户个性推荐图书(被get_books调用))  
[管理员-获取全站订单/网址/地区统计](#管理员-获取全站订单/网址/地区统计)  
[管理员-获取全站订单统计(被get_satistics调用)](#管理员-获取全站订单统计(被get_satistics调用))  
[管理员-获取全站网址统计(被get_satistics调用)](#管理员-获取全站网址统计(被get_satistics调用))  
[管理员-获取全站地区统计(被get_satistics调用)](#管理员-获取全站地区统计(被get_satistics调用))  
[管理员-删除用户](#管理员-删除用户)  
[管理员-修改用户资料](#管理员-修改用户资料)  
[根据书名搜索图书](#根据书名搜索图书)  
[根据分类查找图书](#根据分类查找图书)  
### URL概览
    URL：47.101.69.44：5000
    /login
        /regist
    /login/get_user_status

    /get_books
        /get_book_detail
    /add_book_rating
        /get_book_ratings

    /get_cart
        /add_cart
        /minus_cart
        /del_cart

    /get_user_orders
        /add_order
    /get_order_detail

    /admin/get_all_users
    /admin/get_all_books
    /admin/get_all_orders
    
    /get_books_tops
    /get_books_for_user

    /admin/get_satistics
        /admin/get_orders_sum
        /admin/get_urls_sum
        /admin/get_locations_sum

    /admin/del_user
    /modify_user
    /search_books
### 登录
#### url地址：
    📌/login
#### 前端传后端：
    📌{
        "username":"ff",
        "password":"1"
    }
#### 后端传前端：0 成功 1 密码错 -1 无用户
    📌{
        "status": 0
    }
### 注册
#### url地址：
    📌/regist
#### 前端传后端：1 超管 2 普通用户
    📌{
        "username":"a",
        "password":"1",
        "role":1
    }
#### 后端传前端：
    📌{
        "status": 0 //or -1
    }
### 获取用户角色等信息
#### url地址：
    📌/login/get_user_status
#### 前端传后端：
    📌{
        "username":"a"
    }
#### 后端传前端：
    📌{
        "code": 200,
        "data": {
            "role": 1,
            "user_id": 19,
            "username": "a"
        }
    }
### 获取图书列表(+top20+个性推荐)
#### url地址：
    📌/get_books
#### 前端传后端：
    📌{
        "username":"aaa"
    }
#### 后端传前端：200 表示操作成功，以下都是
（每一项20条记录，关键字如下）
'code': 200,
'all_books': [],
'tops_books':[],
'cus_books':[]
    📌{
       "all_books": [
            {
               "author": "Libby Purves",
               "book_id": 636988,
               "category": "Sciences",
               "image_url": "P/000636988X.01.LZZZZZZZ.jpg",
               "name": "How Not to Be a Perfect Mother: The Crafty
    Mother's Guide to a Quiet Life (How Not to)",
               "press": "HarperCollins Publishers",
               "price": "115.00",
               "publish_date": "1986"
           },        //省略
        ],
       "code": 200,
       "cus_books": [
            {
               "author": "Rich Shapero",
               "book_id": 971880107,
               "category": "Philosophy Religion",
               "image_url": "P/0971880107.01.LZZZZZZZ.jpg",
               "name": "Wild Animus",
               "press": "Too Far",
               "price": "68.00",
               "publish_date": "2004"
           },        //省略
        ],
       "tops_books": [
            {
               "author": "Rebecca Wells",
               "book_id": 60976845,
               "category": "Political Science Law",
               "image_url": "P/0060976845.01.LZZZZZZZ.jpg",
               "name": "Little Altars Everywhere: A Novel",
               "press": "Perennial",
               "price": "186.00",
               "publish_date": "1996"
           },        //省略
        ]
    }

### 获取某图书详情
#### url地址：
    📌/get_book_detail
#### 前端传后端：
    📌{
        "book_id":636988
    }
#### 后端传前端：
    📌{
        "code": 200,
        "data": [
            {
                "author": "Libby Purves",
                "book_id": 636988,
                "category": "Sciences",
                "image_url": "P/000636988X.01.LZZZZZZZ.jpg",
                "name": "How Not to Be a Perfect Mother: The Crafty Mother's Guide to a Quiet Life (How Not to)",
                "press": "HarperCollins Publishers",
                "price": "115.00",
                "publish_date": "1986"
            }
        ]
    }
### 评价图书/更新评价
#### url地址：
    📌/add_book_rating
#### 前端传后端：rating: 0-10   
    📌{
        "username":"aaa",
        "book_id":636988,
        "rating":8
    }
#### 后端传前端：
    📌{
        "status": 0
    }
### 获取图书所有评价
#### url地址：
    📌/get_book_ratings
#### 前端传后端：
    📌{
        "book_id":636988
    }
#### 后端传前端：
    📌{
        "code": 200,
        "data": [
            {
                "rating": 8,
                "username": "aaa"
            },
            {
                "rating": 10,
                "username": "dd"
            }
        ]
    }
### 获取用户购物车
#### url地址：
    📌/get_cart
#### 前端传后端：
    📌{
        "username":"aaa"
    }
#### 后端传前端：number 是购物车这本书的数量
    📌{
        "code": 200,
        "data": [
            {
                "author": "Libby Purves",
                "book_id": 636988,
                "image_url": "http://images.amazon.com/images/P/000636988X.01.LZZZZZZZ.jpg",
                "name": "How Not to Be a Perfect Mother: The Crafty Mother's Guide to a Quiet Life (How Not to)",
                "press": "HarperCollins Publishers",
                "price": "115.00",
                "publish_date": "1986",
             "number": 2
            }
        ]
    }
### 购物车新加图书/数量+1
#### url地址：
    📌/add_cart
#### 前端传后端：
    📌{
        "username":"aaa",
        "book_id":636988
    }
#### 后端传前端：
    📌{
        "status": 0
    }

### 购物车某图书数量-1
#### url地址：
    📌/minus_cart
#### 前端传后端：
    📌{
        "username":"aaa",
        "book_id":636988
    }
#### 后端传前端：-1 书不存在
    📌{
        "status": 0 //-1
    }

### 删除购物车某图书
#### url地址：
    📌/del_cart
#### 前端传后端：
    📌{
        "username":"aaa",
        "book_id":636988
    }
#### 后端传前端：-1 书不存在
    📌{
        "status": 0 //or -1
    }

### 生成订单(清空购物车)
#### url地址：
    📌/add_order
#### 前端传后端：
    📌{
        "username":"aaa"
    }
#### 后端传前端：
payment： 支付总金额   
status状态：0:未付款，1:已付款，2:未发货，3:已发货，4:交易成功，5:交易关闭
    📌{
        "code": 200,
        "data": {
            "order_id": "10002734",
            "payment": "0",
            "status": 0,
            "user_id": 1
        }
    }

### 获取用户订单
#### url地址：
    📌/get_user_orders
#### 前端传后端：
    📌{
        "username":"aaa"
    }
#### 后端传前端：status状态：0:未付款，1:已付款，2:未发货，3:已发货，4:交易成功，5:交易关闭
    📌{
        "code": 200,
        "data": [
            {
                "order_id": "10002834",
                "payment": "341.70",
                "payment_type": null,
                "status": 0,
                "user_id": 1
            },
            {
                "order_id": "10002835",
                "payment": "51.70",
                "payment_type": null,
                "status": 1,
                "user_id": 1
            }
        ]
    }
### 查看订单详情
#### url地址：
    📌/get_order_detail
#### 前端传后端：
    📌{
        "order_id":"10002834"
    }
#### 后端传前端：mount是买这本书的数量，total_price总价
    📌{
        "code": 200,
        "data": [
            {
                "author": "Libby Purves",
                "book_id": 636988,
                "image_url": "http://images.amazon.com/images/P/000636988X.01.LZZZZZZZ.jpg",
                "name": "How Not to Be a Perfect Mother: The Crafty Mother's Guide to a Quiet Life (How Not to)",
                "press": "HarperCollins Publishers",
                "price": "115.00",
                "publish_date": "1986",
                "mount": 2,
             "book_total_price": 134.00
            }
        ]
    }
### 管理员-查看所有用户
#### url地址：
    📌/admin/get_all_users
#### 前端传后端：
    📌无
#### 后端传前端：
    📌{
        "code": 200,
        "data": [
            {
                "email": null,
                "gender": null,
                "nickname": null,
                "password": "1",
                "phone": null,
                "user_id": 2,
                "username": "bbb"
            },
            {
                "email": null,
                "gender": null,
                "nickname": null,
                "password": "1",
                "phone": null,
                "user_id": 19,
                "username": "a"
            },
            {
                "email": null,
                "gender": null,
                "nickname": null,
                "password": "1",
                "phone": null,
                "user_id": 29,
                "username": "fff"
            },
            {
                "email": null,
                "gender": null,
                "nickname": null,
                "password": "1",
                "phone": null,
                "user_id": 1,
                "username": "aaa"
            }
        ]
    }
### 管理员-查看所有图书
#### url地址：
    📌/admin/get_all_books
#### 前端传后端：
    📌无
#### 后端传前端：设置了20个
    📌和获取图书列表一样
### 管理员-查看所有订单
#### url地址：
    📌/admin/get_all_orders
#### 前端传后端：
    📌无
#### 后端传前端：设置了20个
    📌{
        "code": 200,
        "data": [
            {
                "order_id": "10002834",
                "payment": "341.70",
                "payment_type": null,
                "post_fee": null,
                "status": 0,
                "user_id": 1
            }
        ]
    }
### 获取全站TOP20图书(被get_books调用)
#### url地址：
    📌/get_books_tops
#### 前端传后端：
    📌无
#### 后端传前端：设置了20个
    📌{
        "code": 200,
        "data": [
            {
                "author": "Rebecca Wells",
                "book_id": 60976845,
                "category": "Political Science Law",
                "image_url": "P/0060976845.01.LZZZZZZZ.jpg",
                "name": "Little Altars Everywhere: A Novel",
                "press": "Perennial",
                "price": "186.00",
                "publish_date": "1996"
            },
            {
                "author": "David Sedaris",
                "book_id": 316776963,
                "category": "Culture Education and Sports",
                "image_url": "P/0316776963.01.LZZZZZZZ.jpg",
                "name": "Me Talk Pretty One Day",
                "press": "Back Bay Books",
                "price": "91.00",
                "publish_date": "2001"
            },
            {
                "author": "John Irving",
                "book_id": 345361792,
                "category": "Sciences",
                "image_url": "P/0345361792.01.LZZZZZZZ.jpg",
                "name": "A Prayer for Owen Meany",
                "press": "Ballantine Books",
                "price": "67.00",
                "publish_date": "1990"
            },
            {
                "author": "Richard Russo",
                "book_id": 375726403,
                "category": "Sciences",
                "image_url": "P/0375726403.01.LZZZZZZZ.jpg",
                "name": "Empire Falls",
                "press": "Vintage Books USA",
                "price": "162.00",
                "publish_date": "2002"
            },
            {
                "author": "Dan Brown",
                "book_id": 385504209,
                "category": "Political Science Law",
                "image_url": "P/0385504209.01.LZZZZZZZ.jpg",
                "name": "The Da Vinci Code",
                "press": "Doubleday",
                "price": "177.00",
                "publish_date": "2003"
            },
            {
                "author": "Nicholas Sparks",
                "book_id": 446606812,
                "category": "Political Science Law",
                "image_url": "P/0446606812.01.LZZZZZZZ.jpg",
                "name": "Message in a Bottle",
                "press": "Warner Vision",
                "price": "126.00",
                "publish_date": "1999"
            },
            {
                "author": "James Patterson",
                "book_id": 446610038,
                "category": "Military Science",
                "image_url": "P/0446610038.01.LZZZZZZZ.jpg",
                "name": "1st to Die: A Novel",
                "press": "Warner Vision",
                "price": "100.00",
                "publish_date": "2002"
            },
            {
                "author": "Tracy Chevalier",
                "book_id": 452282152,
                "category": "Political Science Law",
                "image_url": "P/0452282152.01.LZZZZZZZ.jpg",
                "name": "Girl with a Pearl Earring",
                "press": "Plume Books",
                "price": "89.00",
                "publish_date": "2001"
            },
            {
                "author": "Catherine Coulter",
                "book_id": 515118656,
                "category": "Economy",
                "image_url": "P/0515118656.01.LZZZZZZZ.jpg",
                "name": "The Cove",
                "press": "Jove Books",
                "price": "123.00",
                "publish_date": "1996"
            },
            {
                "author": "Nora Roberts",
                "book_id": 515128554,
                "category": "Sciences",
                "image_url": "P/0515128554.01.LZZZZZZZ.jpg",
                "name": "Heart of the Sea (Irish Trilogy)",
                "press": "Jove Books",
                "price": "191.00",
                "publish_date": "2000"
            },
            {
                "author": "Wally Lamb",
                "book_id": 671003755,
                "category": "Military Science",
                "image_url": "P/0671003755.01.LZZZZZZZ.jpg",
                "name": "She's Come Undone (Oprah's Book Club (Paperback))",
                "press": "Washington Square Press",
                "price": "143.00",
                "publish_date": "1996"
            },
            {
                "author": "Wally Lamb",
                "book_id": 671021001,
                "category": "Political Science Law",
                "image_url": "P/0671021001.01.LZZZZZZZ.jpg",
                "name": "She's Come Undone (Oprah's Book Club)",
                "press": "Pocket",
                "price": "115.00",
                "publish_date": "1998"
            },
            {
                "author": "Stephen King",
                "book_id": 743457358,
                "category": "Sciences",
                "image_url": "P/0743457358.01.LZZZZZZZ.jpg",
                "name": "Everything's Eventual : 14 Dark Tales",
                "press": "Pocket",
                "price": "153.00",
                "publish_date": "2002"
            },
            {
                "author": "Mitch Albom",
                "book_id": 786868716,
                "category": "Culture Education and Sports",
                "image_url": "P/0786868716.01.LZZZZZZZ.jpg",
                "name": "The Five People You Meet in Heaven",
                "press": "Hyperion",
                "price": "150.00",
                "publish_date": "2003"
            },
            {
                "author": "Amy Tan",
                "book_id": 804106304,
                "category": "Medicine Health Care",
                "image_url": "P/0804106304.01.LZZZZZZZ.jpg",
                "name": "The Joy Luck Club",
                "press": "Prentice Hall (K-12)",
                "price": "91.00",
                "publish_date": "1994"
            },
            {
                "author": "Rich Shapero",
                "book_id": 971880107,
                "category": "Philosophy Religion",
                "image_url": "P/0971880107.01.LZZZZZZZ.jpg",
                "name": "Wild Animus",
                "press": "Too Far",
                "price": "68.00",
                "publish_date": "2004"
            },
            {
                "author": "Alexander McCall Smith",
                "book_id": 1400034779,
                "category": "Economy",
                "image_url": "P/1400034779.01.LZZZZZZZ.jpg",
                "name": "The No. 1 Ladies' Detective Agency (Today Show Book Club #8)",
                "press": "Anchor",
                "price": "126.00",
                "publish_date": "2003"
            },
            {
                "author": "Sarah Waters",
                "book_id": 1573228737,
                "category": "Culture Education and Sports",
                "image_url": "P/1573228737.01.LZZZZZZZ.jpg",
                "name": "Affinity",
                "press": "Riverhead Books",
                "price": "168.00",
                "publish_date": "2002"
            },
            {
                "author": "Celia Brooks Brown",
                "book_id": 1841721522,
                "category": "Economy",
                "image_url": "P/1841721522.01.LZZZZZZZ.jpg",
                "name": "New Vegetarian: Bold and Beautiful Recipes for Every Occasion",
                "press": "Ryland Peters &amp; Small Ltd",
                "price": "82.00",
                "publish_date": "2001"
            },
            {
                "author": "Leo Tolstoy",
                "book_id": 1853260622,
                "category": "Culture Education and Sports",
                "image_url": "P/1853260622.01.LZZZZZZZ.jpg",
                "name": "War and Peace (Wordsworth Classics)",
                "press": "NTC/Contemporary Publishing Company",
                "price": "101.00",
                "publish_date": "1997"
            }
        ]
    }
### 获取给用户个性推荐图书(被get_books调用)
#### url地址：
    📌/get_books_for_user
#### 前端传后端：
    📌{
        "username":"aaa"
    }
#### 后端传前端：设置了20个
    📌和获取TOP20一样
### 管理员-获取全站订单/网址/地区统计
#### url地址：
    📌/admin/get_satistics
#### 前端传后端：
    📌无
#### 后端传前端：
    📌{
        "code": 200,
        "locations": [
            {
                "address": "IANA, 保留地址",
                "ip": "115.182.62.85",
                "times": "3040",
                "user_id": "10018"
            } ....],
        "orders": [
            {
                "month": "4",
                "sum": "630"
            }........],
        "urls": [
         {
                "times": "42926",
                "url": "GET /feed HTTP/1.1"
            },..........]
    }
### 管理员-获取全站订单统计(被get_satistics调用)
#### url地址：
    📌/admin/get_orders_sum
#### 前端传后端：
    📌无
#### 后端传前端：
    📌{
        "code": 200,
        "data": [
            {
                "month": "4",
                "sum": "630"
            },
            {
                "month": "5",
                "sum": "695"
            },
            {
                "month": "6",
                "sum": "675"
            }
        ]
    }
### 管理员-获取全站网址统计(被get_satistics调用)
#### url地址：
    📌/admin/get_orders_sum
#### 前端传后端：
    📌无
#### 后端传前端：50条
    📌{
        "code": 200,
        "data": [
            {
                "times": "42926",
                "url": "GET /feed HTTP/1.1"
            },
            {
                "times": "9001",
                "url": "GET //wp-content/plugins/wp-postratings/postratings-css.css?ver=1.63 HTTP/1.1"
            },
            {
                "times": "8664",
                "url": "GET //wp-includes/js/jquery/jquery.js?ver=1.10.2 HTTP/1.1"
            }
        ]
    }
### 管理员-获取全站地区统计(被get_satistics调用)
#### url地址：
    📌/admin/get_orders_sum
#### 前端传后端：
    📌无
#### 后端传前端：(50条)
    📌{
        "code": 200,
        "data": [
            {
                "address": "IANA, 保留地址",
                "ip": "115.182.62.85",
                "times": "3040",
                "user_id": "10018"
            },
            {
                "address": "北京市, 鹏博士长城宽带",
                "ip": "61.135.219.2",
                "times": "2687",
                "user_id": "13866"
            },
            {
                "address": "北京市, 联通互联网数据中心",
                "ip": "219.133.0.1",
                "times": "2657",
                "user_id": "1667"
            }
        ]
    }
### 管理员-删除用户
#### url地址：
    📌/admin/del_user
#### 前端传后端：
    📌{
        "username": "ppp"
    }
#### 后端传前端：
    📌{
        "status": 0
    }
### 管理员-修改用户资料
#### url地址：
    📌/modify_user
#### 前端传后端：前两个不能为空，username不存在返回-1
    📌{
        "username": "bbb",
        "password": "1",
        "nickname": "xxxxxxx",
        "gender": "f",
        "email": "225245@x.com",
        "phone": "03399"
    }
    or
    {
        "username": "bbb",
        "password": "11",
        "nickname": "",
        "gender": "",
        "email": "",
        "phone": ""
    }
#### 后端传前端：
    📌{
        "status": 0
    }
### 根据书名搜索图书
#### url地址：
    📌/search_books
#### 前端传后端：
    📌{
        "keyword": "How to",
        "type": 1
    }
#### 后端传前端：
    📌{
        "code": 200,
        "data": [
            {
                "author": "Dolores Krieger",
                "book_id": 67176537,
                "category": "History",
                "image_url": "P/067176537X.01.LZZZZZZZ.jpg",
                "name": "The Therapeutic Touch: How to Use Your Hands to Help or to Heal",
                "press": "Fireside",
                "price": "127.00",
                "publish_date": "1979"
            },
            {
                "author": "Moveon",
                "book_id": 193072229,
                "category": "Sciences",
                "image_url": "P/193072229X.01.LZZZZZZZ.jpg",
                "name": "MoveOn's 50 Ways to Love Your Country: How to Find Your Political Voice and Become a Catalyst for Change",
                "press": "Inner Ocean Publishing",
                "price": "143.00",
                "publish_date": "2004"
            },
            {
                "author": "Whitney Otto",
                "book_id": 345370805,
                "category": "Culture Education and Sports",
                "image_url": "P/0345370805.01.LZZZZZZZ.jpg",
                "name": "How to Make an American Quilt",
                "press": "Ballantine Books",
                "price": "186.00",
                "publish_date": "1992"
            },
            {
                "author": "David Steinman",
                "book_id": 345374657,
                "category": "Sciences",
                "image_url": "P/0345374657.01.LZZZZZZZ.jpg",
                "name": "Diet for a Poisoned Planet: How to Choose Safe Foods for You and Your Family",
                "press": "Ballantine Books",
                "price": "58.00",
                "publish_date": "1992"
            },
            {
                "author": "THOMAS ROCKWELL",
                "book_id": 440401119,
                "category": "Philosophy Religion",
                "image_url": "P/0440401119.01.LZZZZZZZ.jpg",
                "name": "How to Fight a Girl",
                "press": "Yearling",
                "price": "166.00",
                "publish_date": "1988"
            },
            {
                "author": "Ellyn Satter",
                "book_id": 915950839,
                "category": "Medicine Health Care",
                "image_url": "P/0915950839.01.LZZZZZZZ.jpg",
                "name": "How to Get Your Kid to Eat but Not Too Much",
                "press": "Bull Publishing Company",
                "price": "105.00",
                "publish_date": "1987"
            },
            {
                "author": "Andy Sloss",
                "book_id": 1860198597,
                "category": "Philosophy Religion",
                "image_url": "P/1860198597.01.LZZZZZZZ.jpg",
                "name": "How to Draw Celtic Knotwork: A Practical Handbook",
                "press": "Brockhampton Press",
                "price": "91.00",
                "publish_date": "0"
            }
        ]
    }
### 根据分类查找图书
#### url地址：
    📌/search_books
#### 前端传后端：
    📌{
        "keyword": "Medicine Health Care",
        "type": 2
    }
#### 后端传前端：设置了20个
    📌{
        "code": 200,
        "data": [
            {
                "author": "Matthew Thomas",
                "book_id": 7100221,
                "category": "Medicine Health Care",
                "image_url": "P/0007100221.01.LZZZZZZZ.jpg",
                "name": "TERROR FIRMA",
                "press": "Trafalgar Square",
                "price": "80.00",
                "publish_date": "2001"
            },
            {
                "author": "John Bellairs",
                "book_id": 14036336,
                "category": "Medicine Health Care",
                "image_url": "P/014036336X.01.LZZZZZZZ.jpg",
                "name": "The House With a Clock in Its Walls",
                "press": "Puffin Books",
                "price": "83.00",
                "publish_date": "1993"
            },
            {
                "author": "Joseph Girzone",
                "book_id": 20199090,
                "category": "Medicine Health Care",
                "image_url": "P/0020199090.01.LZZZZZZZ.jpg",
                "name": "Joshua In the Holy Land",
                "press": "Simon Schuster Trade",
                "price": "84.00",
                "publish_date": "1993"
            },
            {
                "author": "Ernest Hemingway",
                "book_id": 20518609,
                "category": "Medicine Health Care",
                "image_url": "P/0020518609.01.LZZZZZZZ.jpg",
                "name": "Short Stories of Ernest Hemingway (A Scribner classic)",
                "press": "Simon &amp; Schuster",
                "price": "68.00",
                "publish_date": "1987"
            },
            {
                "author": "M. M. Kaye",
                "book_id": 31215125,
                "category": "Medicine Health Care",
                "image_url": "P/031215125X.01.LZZZZZZZ.jpg",
                "name": "The Far Pavilions",
                "press": "St. Martin's Press",
                "price": "178.00",
                "publish_date": "1997"
            },
            {
                "author": "Stephen Baxter",
                "book_id": 34543076,
                "category": "Medicine Health Care",
                "image_url": "P/034543076X.01.LZZZZZZZ.jpg",
                "name": "Manifold: Time (Manifold (Paperback))",
                "press": "Del Rey Books",
                "price": "134.00",
                "publish_date": "2000"
            },
            {
                "author": "Michael Paterniti",
                "book_id": 38533303,
                "category": "Medicine Health Care",
                "image_url": "P/038533303X.01.LZZZZZZZ.jpg",
                "name": "Driving Mr. Albert: A Trip Across America With Einstein's Brain",
                "press": "Delta",
                "price": "158.00",
                "publish_date": "2001"
            },
            {
                "author": "SUE MARGOLIS",
                "book_id": 38533656,
                "category": "Medicine Health Care",
                "image_url": "P/038533656X.01.LZZZZZZZ.jpg",
                "name": "Apocalipstick",
                "press": "Delta",
                "price": "129.00",
                "publish_date": "2003"
            },
            {
                "author": "IAN MCEWAN",
                "book_id": 38572179,
                "category": "Medicine Health Care",
                "image_url": "P/038572179X.01.LZZZZZZZ.jpg",
                "name": "Atonement : A Novel",
                "press": "Anchor",
                "price": "82.00",
                "publish_date": "2003"
            },
            {
                "author": "Shel Silverstein",
                "book_id": 60256672,
                "category": "Medicine Health Care",
                "image_url": "P/0060256672.01.LZZZZZZZ.jpg",
                "name": "Where the Sidewalk Ends : Poems and Drawings",
                "press": "HarperCollins",
                "price": "185.00",
                "publish_date": "1974"
            },
            {
                "author": "Gregory Maguire",
                "book_id": 60987103,
                "category": "Medicine Health Care",
                "image_url": "P/0060987103.01.LZZZZZZZ.jpg",
                "name": "Wicked: The Life and Times of the Wicked Witch of the West",
                "press": "Regan Books",
                "price": "74.00",
                "publish_date": "1996"
            },
            {
                "author": "Tony Hillerman",
                "book_id": 61000280,
                "category": "Medicine Health Care",
                "image_url": "P/0061000280.01.LZZZZZZZ.jpg",
                "name": "The Fly on the Wall",
                "press": "HarperTorch",
                "price": "189.00",
                "publish_date": "1990"
            },
            {
                "author": "Patricia Kennealy-Morrison",
                "book_id": 61056103,
                "category": "Medicine Health Care",
                "image_url": "P/0061056103.01.LZZZZZZZ.jpg",
                "name": "Blackmantle (Keltiad)",
                "press": "Eos",
                "price": "124.00",
                "publish_date": "1998"
            },
            {
                "author": "Paul Monette",
                "book_id": 62507249,
                "category": "Medicine Health Care",
                "image_url": "P/0062507249.01.LZZZZZZZ.jpg",
                "name": "Becoming a Man : Half a Life Story",
                "press": "HarperSanFrancisco",
                "price": "119.00",
                "publish_date": "1993"
            },
            {
                "author": "Fern Michaels",
                "book_id": 82176828,
                "category": "Medicine Health Care",
                "image_url": "P/082176828X.01.LZZZZZZZ.jpg",
                "name": "What You Wish for",
                "press": "Zebra Books",
                "price": "104.00",
                "publish_date": "2001"
            },
            {
                "author": "Ted Dekker",
                "book_id": 84994371,
                "category": "Medicine Health Care",
                "image_url": "P/084994371X.01.LZZZZZZZ.jpg",
                "name": "Blink",
                "press": "WestBow Press",
                "price": "109.00",
                "publish_date": "2003"
            },
            {
                "author": "ALEXANDER MCCALL SMITH",
                "book_id": 140003180,
                "category": "Medicine Health Care",
                "image_url": "P/140003180X.01.LZZZZZZZ.jpg",
                "name": "The Kalahari Typing School for Men (No. 1 Ladies' Detective Agency)",
                "press": "Anchor",
                "price": "180.00",
                "publish_date": "2004"
            },
            {
                "author": "Don DeLillo",
                "book_id": 140077022,
                "category": "Medicine Health Care",
                "image_url": "P/0140077022.01.LZZZZZZZ.jpg",
                "name": "White Noise (Contemporary American Fiction)",
                "press": "Penguin Books",
                "price": "134.00",
                "publish_date": "1991"
            },
            {
                "author": "Stewart O'Nan",
                "book_id": 140250964,
                "category": "Medicine Health Care",
                "image_url": "P/0140250964.01.LZZZZZZZ.jpg",
                "name": "Snow Angels",
                "press": "Penguin Books",
                "price": "115.00",
                "publish_date": "1995"
            },
            {
                "author": "Jane Austen",
                "book_id": 140620664,
                "category": "Medicine Health Care",
                "image_url": "P/0140620664.01.LZZZZZZZ.jpg",
                "name": "Mansfield Park (Penguin Popular Classics)",
                "press": "Penguin Books Ltd",
                "price": "63.00",
                "publish_date": "1994"
            }
        ]
    }
[回到顶部](#backend)
