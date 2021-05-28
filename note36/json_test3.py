from typing import Any
from collections.abc import Mapping
from collections.abc import MutableSequence


class JSONReader:
    def __new__(cls, jsonData:Any) -> Any:
        if isinstance(jsonData, Mapping):
            return super().__new__(cls)
        elif isinstance(jsonData, MutableSequence):
            return [cls(item) for item in jsonData]
        else:
            return jsonData

    def __init__(self, dictData:Mapping) -> None:
        self.__dictData = dict(dictData)

    def __getattr__(self, name: str) -> Any:
        if hasattr(self.__dictData, name):
            return getattr(self.__dictData, name)
        elif name in self.__dictData:
            attrValue = self.__dictData[name]
            return self.__class__(attrValue)
        else:
            raise AttributeError

jsonStr = '''{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}'''
import json
jsonDict = json.loads(jsonStr)
jReader = JSONReader(jsonDict)
print(jReader.sites[0].name)
print(jReader.sites[1].url)
# 菜鸟教程
# www.google.com