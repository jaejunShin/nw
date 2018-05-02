# import os              ## 라이브러리 불러오기
# import platform
# import subprocess
import urllib2

## urllib2 사용 예제
url = 'http://q02.blogspot.kr/2015/08/info.html'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
html = res.read()
print html