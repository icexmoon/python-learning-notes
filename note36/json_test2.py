from typing import Any
from collections.abc import Mapping
from collections.abc import MutableSequence


class JSONReader:
    def __init__(self, dictData:dict) -> None:
        self.__dictData = dict(dictData)

    def __getattr__(self, name: str) -> Any:
        if hasattr(self.__dictData, name):
            return getattr(self.__dictData, name)
        elif name in self.__dictData:
            attrValue = self.__dictData[name]
            if isinstance(attrValue, Mapping):
                return self.__class__(attrValue)
            elif isinstance(attrValue, MutableSequence):
                return [self.__class__(item) for item in attrValue]
            else:
                return attrValue
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