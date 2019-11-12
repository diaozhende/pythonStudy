from flask import Flask
from flask import request
app = Flask(__name__)
# 请求方式和地址
@app.route('/signin',methods=['GET'])
def singin_form():
    return '''
        <form action="/signin" method="post">
         <p><input name="username"></p>
         <p><input name="password" type="password"></p>
         <p><button type="submit">Sign In</button></p>
         </form>
    '''

@app.route('/',methods=['GET','POST'])
def toHome():
    return "<h1>Home</h1>"


@app.route("/signin",methods=["POST"])
def signin():
    # 获取form表单提交过来的数据
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "password":
        return "<h1>Hello admin</h1>"
    return "<h1>用户名或密码错误</h1>"


if __name__ == '__main__':
# 运行 python app.py，Flask 自带的 Server 在端口 5000 上监听
    app.run()