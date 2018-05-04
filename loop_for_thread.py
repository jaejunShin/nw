# -*- coding: utf8 -*-
## 위 주석을 반드시 추가(한글 읽기)

import time
import threading            ## thread 라이브러리
import multiprocessing

def yes(no) :
    while True :
        print "yes - %d\t\n" % no
        time.sleep(0.5)             ## time.sleep(초)

def no(no) :
    while True :
        print "no - %d\t\n" % no
        time.sleep(0.5)             ## time.sleep(초)

# t1 = threading.Thread(target = yes, args = (1, ))           ## thread 생성
# t2 = threading.Thread(target = yes, args = (2, ))           ## target = 함수명, args = 함수인자

## thread 시작
# t1.start()
# t2.start()
if __name__ == '__main__' :
    p1 = multiprocessing.Process(target = yes, args = (1, ))
    p2 = multiprocessing.Process(target = yes, args = (2, ))
    p1.start()
    p2.start()


