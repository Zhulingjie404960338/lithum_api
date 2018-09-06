from flask import Flask, url_for

app = Flask(__name__)

@app.route('/index',endpoint="xxx")  #endpoint是别名
def index():
    v = url_for("xxx")
    print(v)
    return "index"

@app.route('/zzz/<int:nid>',endpoint="aaa")  #endpoint是别名
def zzz(nid):
    v = url_for("aaa",nid=nid)
    print(v)
    return "index2"

if __name__ == '__main__':
    app.run(debug=True)