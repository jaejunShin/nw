# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

## flask 라이브러리 설치 선행(cmd > pip install flask)
## cmd > flask 입력 후 나오는 명령어 사용 후 작업
## browser > 127.0.0.1:5000

## reunder_template : html사용 / request : 요청 처리
from flask import Flask, render_template, request         
app = Flask(__name__)

## app.route() 호출 후 app.route()가 hello() 호출
## ()안의 인자는 주소, "/"는 기본 주소
@app.route("/")                 
def hello():
    return render_template("join.html")

@app.route("/join", methods=['GET','POST'])             ## get:주소창에서 접근, post:데이터 전송에 따른 접근
def join():
    if request.method == 'POST' :
        return "POST!!"
    return "GET!!"

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