from collections import namedtuple
import requests
import time
import json
import concurrent.futures
from tqdm import tqdm
from http import HTTPStatus
WebResult = namedtuple('WebResult','status result')
def getPersonInfo(name):
    resp = requests.get("http://myweb.com/?name={}".format(name), timeout=60)
    status = HTTPStatus.OK
    result = {}
    if resp.status_code != 200:
        if resp.status_code == 404:
            status = HTTPStatus.NOT_FOUND
        else:
            resp.raise_for_status()
    respJson = json.loads(resp.content)
    if respJson['status'] == 'success':
        result = respJson['result']
    return WebResult(status, result)
startTime = time.time()
names = ['Han Meimei','Brus Lee','Jack Chen']
results = {}
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    futuresMap = {}
    for name in names:
        future = executor.submit(getPersonInfo, name)
        futuresMap[future] = name
    futuresDone = concurrent.futures.as_completed(futuresMap)
    for future in tqdm(futuresDone,total=len(names)):
        try:
            webResult = future.result()
        except requests.exceptions.HTTPError as exc:
            pass
        except requests.exceptions.ChunkedEncodingError as exc:
            pass
        else:
            status = webResult.status
            if status != HTTPStatus.OK:
                pass
            else:
                results[futuresMap[future]] = webResult.result
print(results)
endTime = time.time()
print("the time spends is {:.2f}s".format(endTime-startTime))
print('end')
# 100%|███████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:30<00:00, 10.03s/it]
# {'Han Meimei': {'name': 'Han Meimei', 'age': '20', 'career': 'student'}, 'Brus Lee': {'name': 'Brus Lee', 'age': '30', 'career': 'engineer'}, 'Jack Chen': {'name': 'Jack Chen', 'age': '50', 'career': 'actor'}}
# the time spends is 30.14s
# end
