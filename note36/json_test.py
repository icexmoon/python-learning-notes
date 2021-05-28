jsonStr = '''{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}'''
import json
jsonObj = json.loads(jsonStr)
print(type(jsonObj))
print(jsonObj['sites'][0]['name'])
print(jsonObj.sites)
# <class 'dict'>
# 菜鸟教程
# Traceback (most recent call last):
#   File "D:\workspace\python\python-learning-notes\note36\test.py", line 12, in <module>
#     print(jsonObj.sites)
# AttributeError: 'dict' object has no attribute 'sites'