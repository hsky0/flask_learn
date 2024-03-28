from flask import Flask, request, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# 使用flask类创建一个app对象
# __name__: 代表app.py这个模块
# 1. 出现bug， 可以帮助我们快速定位
# 2. 对于寻找模板文件，有一个相对路径
app = Flask(__name__)

HOSTNAME="127.0.0.1" 

PORT = 3306

USERNAME = "root"

PASSWORD = "root"

DATABASE = "database_learn"

app.config['SQLALCHEMY_DATABASE_URI']  = \
f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4" 

# 在app.config中设置好数据库的信息
# 然后使用SQLAlchemy(app)创建一个db对象
# SQLAlchemy会自动读取app.config中连接数据库的信息
db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone()) # 若输出(1,)表示数据库连接成功

def datetime_format(value, format='%Y年%m月%d日 %H :%M'):
    return value.strftime(format)

app.add_template_filter(datetime_format, 'dformat')



# 1. debug模式：
# 1.1 开启debug模式后，只要修改代码就会保存和自动加载，不需要手动启动项目
# 1.2 开发时候遇到bug，开启该模式后，在浏览器上就会看到出错信息
# linux环境：flask --app app run --debug


# 2. 修改host：
# 主要作用：让其他电脑能访问到我电脑上的flask项目(同一个局域网)
# linux环境: flask run --host=0.0.0.0


# 3. 修改端口号
# linux环境：flask run --host=0.0.0.0 --port=8000 

# 创建 一个路由和视图函数的映射
# '/'表示一个根路由，即除了域名意外没有其他东西

# url: http[80]/https[443]://www.qq.com:443/path  

@app.route('/')
def hello_world():
    return render_template("index.html", username='htlf')


@app.route("/profile")
def profile():
    return "我是个人中心"


# <>括号中传入参数，带参数的url
@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return "博客：%s" % blog_id

# 查询字符串的方式传参
# /book/list: 返回第一页的数据
# /book/list?page=2: 获取第二页的数据
@app.route('/book/list')
def book_list():
    # agruments: 参数
    # request.args: 类字典类型
    page = request.args.get("page", default=1, type=int)
    return f"第{page}的图书列表"


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

@app.route('/filter')
def filter_demo():
    user = User(username='htl', email='htl@qq.com')
    mytime = datetime.now()
    return render_template('filter.html', user=user, mytime=mytime)


@app.route('/child1')
def child1():
    return render_template('child1.html') 
 

@app.route('/static')
def static_demo():
    return render_template('static.html')

if __name__ == "__main__":
    app.run()