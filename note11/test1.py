def receiveFunc(func):
    print(type(func))
    return func

def hellow():
    print("hellow world")

returned=receiveFunc(hellow)
returned()
# <class 'function'>
# hellow world
def getMultipParam(*multipParams):
    for param in multipParams:
        print(param,' ',end='')
    print()
    
getMultipParam(1,2,3)
getMultipParam('a','b','c','d','e')
# 1  2  3
# a  b  c  d  e
def getMultipParam(*multipParams):
    for param in multipParams:
        print(param,' ',end='')
    print()
    
getMultipParam(*[1,2,3])
getMultipParam(*['a','b','c','d','e'])
# 1  2  3
# a  b  c  d  e
def getKVParams(**kvParams:dict):
    for paramKey,paramVal in kvParams.items():
        print(paramKey,':',paramVal,end=',')
    print()
    
getKVParams(name="jack",age=16)
getKVParams(career="enginner",age=18)
# name : jack,age : 16,
# career : enginner,age : 18,
def getKVParams(**kvParams:dict):
    for paramKey,paramVal in kvParams.items():
        print(paramKey,':',paramVal,end=',')
    print()
    
getKVParams(**{"name":"jack","age":16})
getKVParams(**{"career":"teacher","age":17})
# name : jack,age : 16,
# career : teacher,age : 17,
def getEveryParams(*multipParams,**kvParams:dict):
    for param in multipParams:
        print(param,end=',')
    print()
    for paramKey,paramVal in kvParams.items():
        print(paramKey,':',paramVal,end=',')
    print()
    
getEveryParams(1,2,3,age=16,name="jack")
# 1,2,3,
# age : 16,name : jack,
def getInnerFunc():
    def innerFunc():
        print("hellow world")
    return innerFunc

test=getInnerFunc()
test()
# hellow world