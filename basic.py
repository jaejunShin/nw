# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)


import os              ## 라이브러리 불러오기
import platform
import subprocess

## print "hello python"

## 변수
msg = "hello python"
print msg

## 문자열 슬라이싱
print msg[1:3]          ## 문자열 index 1부터 3미만 출력(1,2 = e, l)
print msg[:3]           ## 0~2까지(h, e, l)
print msg[-1]           ## index 0기준 -1 출력(n)
print msg[:-2]          ## 0~ 0-2까지 출력
print msg[::-1]         ## 역순 출력

## 리스트
data = []
# 리스트에 자료 추가
data.append("hi")
data.append(123)
data.append(3.5)

print data
data.pop()              ## 리스트에 자료 제거(LIFO)
print data
data.pop()
print data
# 인덱스 검색
print data.index("hi")
# print data.index("nothing")         ## 존재하지 않는 값

## 사전 (키 : 값) 형태
user = {}
user['me'] = {'age':26, 'address':'daejeon'}    ## 사전 안의 사전
user['you'] = {'age':30, 'address':'seoul'}     

print user
print user['me']
print "user keys:", user.keys()       ## key 확인
print "me" in user.keys()

print type (user)

## 조건문 if, if else, if elif else
num = input("\ninput number : ")               ## 입력문
print type(num)

if num > 0 :
    print "num > 0"

if num > 5 :
    print "num > 5"
else :
    print "num =< 5"

if num % 2 == 0 :           ## {}가 없기 때문에 들여쓰기로 구분
    print "even"
    print "exe"
elif num % 2 == 1 :         ## else if가 아닌 elif임에 주의
    print "odd"
else :
    print "????"

char = raw_input("\ninput anythings : ")        ## 문자열 입력문
print type(char)
print char

## 함수
def addition(numbers):          ## def 함수명(인자)
    result = 0
    for number in numbers:
        result += number
    return result

data = [1, 2, 3]
print addition(data)

def help():
    print "id ------ print user id"
    print "pwd ------ print current pwd"
    print "ip ------ print ipaddress"
    print "quit ------ exit program"
    

help()

## 무한 루프
while True :
    cmd = raw_input('>>> ')
    if cmd == 'id' :
        if platform.system() == 'Windows' :
            print os.environ.get('USERNAME')
        else :
            print os.getenv('USER')
            
    elif cmd == 'pwd' :
        print os.getcwd()
            
    elif cmd == 'ip' :
        if platform.system() == 'Windows' :         ## OS가 Windows인 경우
            ################ 텍스트 찾는 방법 ################
            buf = subprocess.check_output('ipconfig')
            index = buf.find("IPv4")
            newline = buf[index:].find("\n")
            
            # print index, newline
            # print buf[index:index+newline]
            ipline = buf[index:index+newline]
            ip = ipline.split(':')      ## ()를 기준으로 데이터를 분리

            print ip[1].strip()         ## strip() : 공백 제거
            #################################################
        
        else :                              ## Linux인 경우 같은 방법 적용    
            buf = subprocess.check_output('ifconfig')
            target = 'addr:'
            # index = buf.find(target) + len(target)      ## len = length, 길이 만큼 출력문 제거
            # space = buf[index:].find("  ")
            # print index, space
            # print buf[index:index+space]
            
            ################### 응용 ####################
            index = buf.find(target)
            space = buf[index:].find("  ")
            ipline = buf[index:index+space]
            ip = ipline.split(':')
            print ip[1].strip()
            ############################################
        
    elif cmd == 'quit' :
        print cmd
        break
    
    else :
        help()
