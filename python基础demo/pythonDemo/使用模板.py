from flask import Flask,request,render_template
app = Flask("__name__")

@app.route("/",methods=["POST","GET"])
def toHome():
    return render_template("home.html")

@app.route("/login",methods=["GET"])
def toForm():
    # 通过render_template方法往前台进行传递参数
    return render_template("form.html")

@app.route("/submit",methods=["POST"])
def submit():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == "admin":
        # 通过render_template方法往前台进行传递参数
        return render_template("signin-ok.html",username = username)
    return render_template("form.html",message="Bad username or password",username = username)

if __name__ == "__main__":
    app.run()