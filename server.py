# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

import socket

info = ("127.0.0.1", 9999)

s = socket.socket()

s.bind(info)                    ## 9999번 포트 바인딩
s.listen(5)                     ## 바인딩 포트 리스닝

while True :
    client, address = s.accept()        ## 접속 요청 승인
    print "[+] new connection from %s(%d)" % (address[0], address[1])

    while True :
        try:
            data = client.recv(1024)    ## 클라이언트 데이터 수신
        except :
            print "Exception !!!"
            break

        ## data = client.recv(1024)        ## 클라이언트 데이터 수신

        if not data :                   ## 예외처리
            client.close()
            break

        print "address %s send data %s" % (address[0], data)

        client.send(data)               ## 클라이언트에 데이터 전송