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
