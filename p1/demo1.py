# -*- coding: utf-8 -*-
import uuid
import socket

def get_mac_addr():
    mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

myname = socket.getfqdn(socket.gethostname())
myAdd = socket.gethostbyname(myname)
myMac = get_mac_addr()

print myname
print myAdd
print myMac

#--------------------------------------------------------------------------------------------------------

import os
#print os.system('ipconfig /all')
#print os.system('ping www.xunlei.com')

#--------------------------------------------------------------------------------------------------------

language = 'python'
def foo1():
    language = 'hello'
    print(language)
def foo2():
    print(language)
def foo3():
    global language
    language = 'hello'
    print(language)
foo1()
foo2()
foo3()
print(language)

#--------------------------------------------------------------------------------------------------------

def foo1(arg1,arg2,key1=1,key2=2,*arg,**keywords):
    print 'arg1 is', arg1
    print 'arg2 is', arg2
    print 'key1 is', key1
    print 'key2 is', key2
    print 'Arbitrary is', arg
    print 'keywords is', keywords

foo1(1,2,3,4,5,6,k1=1,k2=2,k3=3)