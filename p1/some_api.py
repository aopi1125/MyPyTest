#1.
#常用内置函数：(不用import就可以直接使用)
help(obj)
#在线帮助, obj可是任何类型

callable(obj)
#查看一个obj是不是可以像函数一样调用

repr(obj)
#得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝

eval_r(str)
#表示合法的python表达式，返回这个表达式

dir(obj)
#查看obj的name
#space中可见的name

hasattr(obj, name)
#查看一个obj的name
#space中是否有name

getattr(obj, name)
#得到一个obj的name
#space中的一个name

setattr(obj, name, value)
# 为一个obj的name
# space中的一个name指向vale这个object

delattr(obj, name)
# 从obj的name
# space中删除一个name

vars(obj)
# 返回一个object的name
# space。用dictionary表示

locals()
# 返回一个局部name
# space, 用dictionary表示

globals()
# 返回一个全局name
# space, 用dictionary表示

type(obj)
# 查看一个obj的类型

isinstance(obj, cls)
# 查看obj是不是cls的instance

issubclass(subcls, supcls)
# 查看subcls是不是supcls的子类

#类型转换函数
chr(i)
# 把一个ASCII数值, 变成字符

ord(i)
# 把一个字符或者unicode字符, 变成ASCII数值

oct(x)
# 把整数x变成八进制表示的字符串

hex(x)
# 把整数x变成十六进制表示的字符串

str(obj)
# 得到obj的字符串描述

list(seq)
# 把一个sequence转换成一个list

tuple(seq)
# 把一个sequence转换成一个tuple

dict(), dict(list)
# 转换成一个dictionary

int(x)
# 转换成一个integer

long(x)
# 转换成一个long
# interger

float(x)
# 转换成一个浮点数

complex(x)
# 转换成复数

max(...)
# 求最大值

min(...)
# 求最小值
# 用于执行程序的内置函数

#complie
# 如果一段代码经常要使用, 那么先编译, 再运行会更快。

# 2.
# 和操作系统相关的调用
# 系统相关的信息模块
import sys

sys.argv是一个list, 包含所有的命令行参数.
sys.stdout
sys.stdin
sys.stderr
# 分别表示标准输入输出, 错误输出的文件对象.

sys.stdin.readline()
# 从标准输入读一行

sys.stdout.write("a")
# 屏幕输出a

sys.exit(exit_code)
# 退出程序

sys.modules
# 是一个dictionary，表示系统中所有可用的module

sys.platform
# 得到运行的操作系统环境

sys.path
# 是一个list, 指明所有查找module，package的路径.

# 操作系统相关的调用和操作
import os

os.environ
# 一个dictionary
# 包含环境变量的映射关系

os.environ["HOME"]
# 可以得到环境变量HOME的值

os.chdir(dir)
# 改变当前目录

os.chdir('d:\\outlook')
# 注意windows下用到转义

os.getcwd()
# 得到当前目录

os.getegid()
# 得到有效组id

os.getgid()
# 得到组id

os.getuid()
# 得到用户id

os.geteuid()
# 得到有效用户id

os.setegid
os.setegid()
os.seteuid()
os.setuid()

os.getgruops()
# 得到用户组名称列表

os.getlogin()
# 得到用户登录名称

os.getenv
# 得到环境变量

os.putenv
# 设置环境变量

os.umask
# 设置umask

os.system(cmd)
# 利用系统调用，运行cmd命令

# 操作举例：
os.mkdir('/tmp/xx')
os.system("echo 'hello' > /tmp/xx/a.txt")
os.listdir('/tmp/xx')
os.rename('/tmp/xx/a.txt', '/tmp/xx/b.txt')
os.remove('/tmp/xx/b.txt')
os.rmdir('/tmp/xx')

# 用python编写一个简单的shell
# !/usr/bin/python
import os, sys
cmd = sys.stdin.readline()
while cmd:
    os.system(cmd)
    cmd = sys.stdin.readline()

# 用os.path编写平台无关的程序
os.path.abspath("1.txt") == os.path.join(os.getcwd(), "1.txt")
os.path.split(os.getcwd())
# 用于分开一个目录名称中的目录部分和文件名称部分。

os.path.join(os.getcwd(), os.pardir, 'a', 'a.doc')
# 全成路径名称.

os.pardir
# 表示当前平台下上一级目录的字符..

os.path.getctime("/root/1.txt")
# 返回1.txt的ctime(创建时间)
# 时间戳

os.path.exists(os.getcwd())
# 判断文件是否存在

os.path.expanduser('~/dir')
# 把
# ~扩展成用户根目录

os.path.expandvars('$PATH')
# 扩展环境变量PATH

os.path.isfile(os.getcwd())
# 判断是否是文件名，1
# 是0否

os.path.isdir('c:\Python26\temp')
# 判断是否是目录, 1
# 是0否

os.path.islink('/home/huaying/111.sql')
# 是否是符号连接
# windows下不可用

os.path.ismout(os.getcwd())
# 是否是文件系统安装点
# windows下不可用

os.path.samefile(os.getcwd(), '/home/huaying')
# 看看两个文件名是不是指的是同一个文件

os.path.walk('/home/huaying', test_fun, "a.c")
# 遍历 / home / huaying下所有子目录包括本目录, 对于每个目录都会调用函数test_fun.
# 例：在某个目录中，和他所有的子目录中查找名称是a.c的文件或目录。
def test_fun(filename, dirname, names):
    # filename即是walk中的a.c
# dirname是访问的目录名称
if filename in names:
    # names是一个list, 包含dirname目录下的所有内容
print os.path.join(dirname, filename)
os.path.walk('/home/huaying', test_fun, "a.c")


# 文件操作
# 打开文件
f = open("filename", "r")

# r只读
# w写
# rw读写
# rb读二进制
# wb写二进制
# w + 写追加

# 读写文件
f.write("a")
f.write(str)

# 写一字符串
f.writeline()

f.readlines()
# 与下read类同
f.read()
# 全读出来

f.read(size)
# 表示从文件中读取size个字符

f.readline()
# 读一行, 到文件结尾, 返回空串.f.readlines()
# 读取全部，返回一个list.list每个元素表示一行，包含
# "\n" \
f.tell()
# 返回当前文件读取位置

f.seek(off, where)
# 定位文件读写位置.off表示偏移量，正数向文件尾移动，负数表示向开头移动。
# where为0表示从开始算起, 1
# 表示从当前位置算, 2
# 表示从结尾算.

f.flush()
# 刷新缓存

# 关闭文件
f.close()

# 这些特殊字符是 。 ^ $ *+ ? {[] \ | ( )
# *表示{,} +表示{1,} ?表示{0,1}