import os              ## 라이브러리 불러오기
import platform
import subprocess
import urllib2

## urllib2 사용 예제
url = 'https://goo.gl/TFMAjZ'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
html = res.read()
print html