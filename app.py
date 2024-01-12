import jieba
from flask import Flask, render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/')
# def index():
#     d=[]
#     con = sqlite3.connect("movie.db")
#     cur = con.cursor()
#     sql = "select count(*) from movie250"
#     data = cur.execute(sql)
#     for i in data:
#         d.append(i[0])
#     sql = 'select instroduction from movie250'
#     data = cur.execute(sql)
#     text = ""
#     for item in data:
#         # print(item[0])
#         text = text + item[0]
#     # 分词
#     cut = jieba.cut(text)
#     string = ' '.join(cut)
#     d.append(len(string))
#     cur.close()
#     con.close()
#     return render_template("index1.html", count=d)
@app.route('/index')
def home():
    return index()


@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", movies=datalist)


@app.route('/score')
def score():
    scoreList = []
    scoreNum = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scoreList.append(item[0])
        scoreNum.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html", scoreList=scoreList, scoreNum=scoreNum)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")



@app.route('/introduction')
def introduction():
    return render_template("introduction.html")

@app.route('/sg')
def sg():
    return render_template("sg.html")

@app.route('/lx')
def lx():
    return render_template("lx.html")
if __name__ == '__main__':
    app.run()
