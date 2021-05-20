import requests
import time
import json
import concurrent.futures
def getPersonInfo(name):
    resp = requests.get("http://myweb.com/?name={}".format(name), timeout=60)
    respJson = json.loads(resp.content)
    if respJson['status'] == 'success':
        return respJson['result']
    return {}
startTime = time.time()
names = ['Han Meimei','Brus Lee','Jack Chen']
results = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    mapIter = executor.map(getPersonInfo,names)
for name,info in zip(names,mapIter):
    results[name] = info
print(results)
endTime = time.time()
print("the time spends is {:.2f}s".format(endTime-startTime))
print('end')
# the time spends is 0.13s
# end
