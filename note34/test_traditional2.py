import requests
import time
import json
startTime = time.time()
names = ['Han Meimei','Brus Lee','Jack Chen']
results = {}
for name in names:
    resp = requests.get("http://myweb.com/?name={}".format(name), timeout=60)
    respJson = json.loads(resp.content)
    if respJson['status'] == 'success':
        results[name]=respJson['result']
print(results)
endTime = time.time()
print("the time spends is {:.2f}s".format(endTime-startTime))
print('end')
# the time spends is 0.13s
# end
