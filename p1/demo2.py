# -*- coding: utf-8 -*-

f = file("test.txt", 'w')
f.write("1:insert some text into file")
f.write("2:insert nextline 2")
f.close()

#o = open("file.txt")
#o.read()
#o.close()

f = open("test.txt", 'r')
print "the top 8 char is '%s'"%f.read(8)
print "print the next read content %s"%f.read()
print f.tell()

f = file("text.txt", 'w+')
f.write('welcome: 1:insert some text in the text.txt file\n')
f.write("2:insert line two")
f.close()
f = open("text.txt", 'r+')
print f.read()
f.seek(8)
f.write("--*--")
f.seek(0)
print f.read()
print "the top 8 char is '%s'"%f.read(8)
print f.tell()

##--------------------------------------------------------------------------------------------------------
# 关于open 模式：
# w     以写方式打开，
# a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
# r+     以读写模式打开
# w+     以读写模式打开 (参见 w )
# a+     以读写模式打开 (参见 a )
# rb     以二进制读模式打开
# wb     以二进制写模式打开 (参见 w )
# ab     以二进制追加模式打开 (参见 a )
# rb+    以二进制读写模式打开 (参见 r+ )
# wb+    以二进制读写模式打开 (参见 w+ )
# ab+    以二进制读写模式打开 (参见 a+ )
#--------------------------------------------------------------------------------------------------------

a = [x+2 for x in range(10)]
print a

import sys
print sys.version
print sys.copyright

d = {'name':{}, 'age':{}, 'sex':{}}
print 'name' in d.keys()
print 'name' in 'myname'
#print d.keys().__contains__('name')

int('100', 2)#二进制转十进制
int('44', 8)#八进制转十进制
int('0x4', 16)#十六进制转十进制
#反转
bin(int('100', 2))#binary
bin(4)
oct(int('44', 8))
hex(int('0x4', 16))
