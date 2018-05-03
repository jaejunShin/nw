# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

import socket       ## 통신을 위한 라이브러리

info = ("127.0.0.1", 9999)          ## 접속 서버 정보

s = socket.socket()                 ## TCP 소켓 생성

s.connect(info)                     ## 서버 접속

s.send("hello server\n")            ## 데이터 전송
print s.recv(1024)                  ## 데이터 수신 및 출력
s.close()                           ## 접속 종료