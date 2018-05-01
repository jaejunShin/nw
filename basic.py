# -*- coding: utf8 -*-

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

## 사전
user = {}
user['me'] = {'age':26, 'address':'daejeon'}    ## {키 : 값} 형태
user['you'] = {'age':30, 'address':'seoul'}

print user
print user['me']
print "user keys:", user.keys()       ## key 확인
print "me" in user.keys()

## 조건문 if, if else, if elif else
num = 4
if num > 0 :
    print "num > 0"

if num > 5 :
    print "num > 5"
else :
    print "num < 5"

if num % 2 == 0 :
    print "even"
elif num % 2 == 1 :
    print "odd"
else :
    print "????"