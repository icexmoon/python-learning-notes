import requests
urls = ("https://www.liaoxuefeng.com/wiki/1016959663602400/1183249464292448",
        "https://www.runoob.com/w3cnote/python-spider-intro.html",
        "https://www.runoob.com/w3cnote/secure-wordpress-nginx.html",
        "https://cn.python-requests.org/zh_CN/latest/")
urlReqGen = (requests.get(url) for url in urls)
print(type(urlReqGen))
for resp in urlReqGen:
    print(len(resp.text))
# <class 'generator'>
# 222
# 63870
# 49798
# 25894