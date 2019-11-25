from flask import Flask,request,render_template
app = Flask(__name__)

# @app.router("/home",methods=["GET"])
@app.route("/home",methods=["GET"])
def index_url():
    print("请求。。。")
    return render_template("home.html",result="返回值")

if __name__ == "__main__":
    app.run()