#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "liuxin"
# Date: 2018-5-16
#practice beautifulsoup

#Beautiful Soup 4.2.0 文档:
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#pyquery：用于python的类似jQuery的库
#https://pythonhosted.org/pyquery/index.html#


import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5221.400 QQBrowser/10.0.1125.400'
}

response = requests.get('http://maoyan.com/board/4',headers=headers)
html = response.text
soup = BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.p)
print(soup.p.contents)
