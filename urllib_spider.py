#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "liuxin"
# Date: 2018
#practice urllib


# import urllib.request

# response = urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print(response.read().decode('utf-8'))





# import urllib.request
# import urllib.parse

# data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())





# import urllib.request
# import urllib.error

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)
#     print('ok')
#     print(response.read())
# except urllib.error.URLError as e:
#     print('timeout error')

# print('end')


#urllib.parse.urljoin()等方法可以拼接url






#https://cuiqingcai.com/5052.html
#request：它是最基本的HTTP请求模块，可以用来模拟发送请求。就像在浏览器里输入网址然后回车一样，只需要给库方法传入URL以及额外的参数，就可以模拟实现这个过程了。
#error：异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作以保证程序不会意外终止。
#parse：一个工具模块，提供了许多URL处理方法，比如拆分、解析、合并等。
#robotparser：主要是用来识别网站的robots.txt文件，然后判断哪些网站可以爬，哪些网站不可以爬，它其实用得比较少。

#常用的方法
#request:  urlopen()
#error:    URLError()
#paese:    urlencode()  urlsplit()  urljoin() quote()
