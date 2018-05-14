# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

## flask 라이브러리 설치 선행(cmd > pip install flask)
## cmd > flask 입력 후 나오는 명령어 사용 후 작업
## browser > 127.0.0.1:5000

## reunder_template : html사용 / request : 요청 처리
import hashlib
import sqlite3                                                  ## sql db사용
from flask import Flask, render_template, request, g            ## g는 전역변수와 유사한 객체

DATABASE = 'database.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None :
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext                                ## flask가 종료되는 시점에 사용될 함수.
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False, modify=False):
    cur = get_db().execute(query, args)
    if modify:
        try : 
            get_db().commit()
            cur.close()
        except :
            return False
        return True
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv       ## if one이 있으면 return (rv ~ else None), else return rv
                                                        ## 2개의 if문을 한 줄로 쓰는 방법 지양(return을 하나 쓰기위한 코드)

## app.route() 호출 후 app.route()가 hello() 호출
## ()안의 인자는 주소, "/"는 기본 주소
@app.route("/")                 
def hello():
    return render_template("login.html")

@app.route("/login", methods=['POST'])             ## get:주소창에서 접근, post:데이터 전송에 따른 접근
def login():
    if request.method == 'POST' :
        id = request.form['id']
        pw = request.form['pw']
        # if id in users :
        #     if users[id] == hashlib.sha1(pw).hexdigest() :      ## hash는 항상 고정길이를 지님.
        #         return "login ok"
        #     else : 
        #         return "login fail !!!"
        # else :
        #     return "login fail !!!"

@app.route("/join", methods=['GET','POST'])             ## get:주소창에서 접근, post:데이터 전송에 따른 접근
def join():
    if request.method == 'POST' :
        id = request.form['id']
        pw = request.form['pw']
        sql = "insert into user(id, password) values ('%s', '%s')" % (id, pw)
        print sql
        query_db(sql)
        # if id not in users :
        #     users[id] = hashlib.sha1(pw).hexdigest()
        # else :
        #     return "Duplicate!!!"
        # return "join ok"
    return render_template("join.html")

@app.route("/name")
def name():
    return "This is my name!"

@app.route("/add")
@app.route("/add/")
@app.route("/add/<int:num1>")
@app.route("/add/<int:num1>/<int:num2>")        ## <> browser 형태로 인자 전달
def add(num1=None, num2=None):
    if (num1 is None or num2 is None) :
        return "/add/num1+num2"
    return str(num1+num2)                       ## str 형변환

##################### 응용 사칙연산 ######################
@app.route("/sub")
@app.route("/sub/")
@app.route("/sub/<int:num1>")
@app.route("/sub/<int:num1>/<int:num2>")        
def sub(num1=None, num2=None):
    if (num1 is None or num2 is None) :
        return "/sub/num1+num2"
    return str(num1 - num2)                     

@app.route("/mul")
@app.route("/mul/")
@app.route("/mul/<int:num1>")
@app.route("/mul/<int:num1>/<int:num2>")        
def mul(num1=None, num2=None):
    if (num1 is None or num2 is None) :
        return "/mul/num1+num2"
    return str(num1 * num2)                     

@app.route("/div")
@app.route("/div/")
@app.route("/div/<int:num1>")
@app.route("/div/<float:num1>/<float:num2>")
@app.route("/div/<int:num1>/<float:num2>")
@app.route("/div/<float:num1>/<int:num2>")
@app.route("/div/<int:num1>/<int:num2>")      
def div(num1=None, num2=None):
    if (num1 is None or num2 is None) :
        return "/div/num1+num2"
    elif (num1 is float(num1) or num2 is float(num2)) :
        if(num2 == 0):
            return "Impossible Div"
        return str(num1 / num2)
    elif(num2 == 0):
        return "Impossible Div"    
    return str(num1 / float(num2))
#########################################################