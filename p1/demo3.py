# coding=utf-8
#-*- coding:utf-8 -*-

import os
#os.system('ls -l')

from math import sqrt
def sqrt(n):
    return n
print sqrt(13689)
#raw_input()


#其实所有语言都是想通的，重要的是算法，所以掌握基础的经典的算法还是很有必要滴~~

def getprim(n):
    p = 3
    x = 0
    while(x<n):
        result = True
        for i in range(2, p-1):
            if(p%i==0):
                result = False
        if result==True:
            x+=1
            rst = p
        p+=2
    print rst

getprim(1000)