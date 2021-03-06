# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

## flask 라이브러리 설치 선행(cmd > pip install flask)
## cmd > flask 입력 후 나오는 명령어 사용 후 작업
## browser > 127.0.0.1:5000

## reunder_template : html사용 / request : 요청 처리
import hashlib                                                  ## 고유한 hash값을 비교
import sqlite3                                                  ## sql db사용
from flask import Flask, render_template, request, g, redirect, session, escape  ## g는 전역변수와 유사한 객체

DATABASE = 'database.db'

app = Flask(__name__)                   ## flask 객체 초기화
app.secret_key = 'n1a456k565427t98a%j1508/%j55S095h948$i^492n'      ## 비밀키. 암호화(encoding)를 위한 임의의 값 입력

def get_db():                           ## DB연동을 위한 함수
    db = getattr(g, '_database', None)
    if db is None :
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext                                ## flask가 종료되는 시점에 사용될 함수
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None :
        db.close()

def query_db(query, args=(), one=False, modify=False):  ## DB query문 사용을 위한 함수
    cur = get_db().execute(query, args)
    if modify:
        try : 
            get_db().commit()               ## 가입(DB에 추가) 시 commit이 필수
            cur.close()
        except :
            return False
        return True
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv       ## if one이 있으면 return (rv ~ else None), else return rv
                                                        ## 2개의 if문을 한 줄로 쓰는 방법 지양(return을 하나 쓰기위한 코드)

## app.route() 호출 후 app.route()가 hello() 호출
## ()안의 인자는 주소, "/"는 기본 주소(index)
@app.route("/")                 
def hello():
    if 'id' in session :
        ## escape를 사용하지 않을 경우 사용자가 입력한 값을 code로 해석할 가능성이 있음
        return 'Logged in as %s <a href = "/logout">logout</a>' % escape(session['id'])        
    return render_template("login.html")

@app.route("/logout")
def logout() :
    session.pop('id', None)
    return redirect('/login')

@app.route("/login", methods=['GET', 'POST'])             ## get:주소창에서 접근, post:데이터 전송에 따른 접근
def login():
    if request.method == 'POST' :
        id = request.form['id'].strip()
        pw = hashlib.sha1(request.form['pw'].strip()).hexdigest()

        sql = "select * from user where id='%s' and password='%s'" % (id, pw)
        if query_db(sql, one=True) :            ## 로그인 성공 시 로그인 상태 유지
            session['id'] = id
            return redirect("/")
        else :                                  ## 로그인 실패 시
            return "<script>alert('login fail'); history.back(-1);</script>"        ## history.back() = 뒤로가기 ()번
    if 'id' in session :
        return redirect("/")
    
    return render_template("login.html")
        
@app.route("/join", methods=['GET','POST'])             ## get:주소창에서 접근, post:데이터 전송에 따른 접근
def join():
    if request.method == 'POST' :
        id = request.form['id'].strip()
        pw = hashlib.sha1(request.form['pw'].strip()).hexdigest()

        sql = "select * from user where id='%s' " % id
        if query_db(sql, one=True) :                    ## 중복 가입 방지
            return "<script>alert('Existed ID'); history.back(-1);</script>"        ## 다시 가입화면으로

        sql = "insert into user(id, password) values ('%s', '%s')" % (id, pw)
        print sql
        query_db(sql, modify=True)
        # if id not in users :
        #     users[id] = hashlib.sha1(pw).hexdigest()
        # else :
        #     return "Duplicate!!!"
        return 'join ok <a href = "/login">Home</a>'
    if 'id' in session :
        return redirect("/")
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