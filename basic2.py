# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

## 라이브러리 추가
import urllib2
import re

## urllib2 사용 예제
url = 'https://box.cdpython.com/ezen/'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
html = res.read()
# print html
## ip주소/포트번호 패턴 찾기 d+.d+.d+.d+/d+ 의 패턴 = 정규표현식
## / 기준으로 ip, 포트번호 분리
ipaddress, port = re.findall("\d+\.\d+\.\d+\.\d+\/\d+"
                    , html)[0].split('/')

print "ip : ", ipaddress+"\n", "port : ", port

