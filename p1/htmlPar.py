# -*- coding: utf-8 -*-

# import html2text
#
# f = open("html.xml", 'r')
# content = f.read()
#
# h = html2text.HTML2Text()
# h.ignore_links = False
# print content
# print "---"
# print h.handle(content)
#


import xml.sax


class HtmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        f = file("htmlResult.txt", 'a+')
        if tag == "a":
            name = attributes["href"]
            if "/13" in name:
                urlcontent = "http://ppt.geekbang.org" + name
                value = urlcontent.replace('/13', '')
                f.write(value)
                f.write('\n')
                print value

        f.close()



if __name__ == "__main__":
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = HtmlHandler()
    parser.setContentHandler(Handler)
    parser.parse("html.xml")

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
