import requests
import re

#get请求
response = requests.get('http://www.baidu.com/')
print(type(response))
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.status_code)

#get方式
r = requests.get('http://httpbin.org/get')
print(r.text)


#添加参数
data = {data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
    'name': 'germey',
    'age': 22
}
r2 = requests.get("http://httpbin.org/get", params=data)
print(r2.text)


#添加请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r3 = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r3.text)
print(titles)



#图片、音频、视频这些文件本质上都是由二进制码组成的，由于有特定的保存格式和对应的解析方式，我们才可以看到这些形形色色的多媒体。
#所以，想要抓取它们，就要拿到它们的二进制码。
#response.text 返回str  response.content 返回二进制数据
#保存图片．

r = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(r.content)



#post请求
data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)


#文件上传
files = {'file': open('favicon.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)


#维持会话
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)


#SSL证书验证 verify参数，默认为true需要验证
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


#使用代理
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
 
requests.get("https://www.taobao.com", proxies=proxies)


#超时设置
r = requests.get("https://www.taobao.com", timeout = 1)
print(r.status_code)


#身份认证
import requests
from requests.auth import HTTPBasicAuth
 
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
print(r.status_code)

#简单写法：
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)



#Prepared Request
#有了Request这个对象，就可以将请求当作独立的对象来看待，这样在进行队列调度时会非常方便
from requests import Request, Session
 
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)

























#https://cuiqingcai.com/5052.html
