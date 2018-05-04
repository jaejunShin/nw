# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

## flask 라이브러리 설치 선행(cmd > pip install flask)
## cmd > flask 입력 후 나오는 명령어 사용
## browser > 127.0.0.1:5000
from flask import Flask         
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"