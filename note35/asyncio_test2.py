import asyncio
import aiohttp
from aiohttp import web
import pprint
from tqdm import tqdm
async def getPersonInfo(name):
    url = "http://myweb.com/?name={}".format(name)
    personInfo = {}
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                queryResult = await response.json()
                if queryResult['status'] == 'success':
                    personInfo = queryResult['result']
            elif response.status == 404:
                raise web.HTTPNotFound
            else:
                raise web.HTTPServerError
    return personInfo
                
async def getPeopleInfo(names):
    queryCoroutines = [getPersonInfo(name) for name in names]
    completedFutures = asyncio.as_completed(queryCoroutines)
    completedFutures = tqdm(completedFutures,total=len(names))
    results = {}
    for future in completedFutures:
        personInfo = await future
        results[personInfo['name']] = personInfo
    return results

names = ['Han Meimei', 'Brus Lee', 'Jack Chen']
loop = asyncio.get_event_loop()
results = loop.run_until_complete(getPeopleInfo(names))
loop.close()
pprint.pprint(results)
# 100%|███████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:10<00:00,  3.35s/it]
# {'Brus Lee': {'age': '30', 'career': 'engineer', 'name': 'Brus Lee'},
#  'Han Meimei': {'age': '20', 'career': 'student', 'name': 'Han Meimei'},
#  'Jack Chen': {'age': '50', 'career': 'actor', 'name': 'Jack Chen'}}

