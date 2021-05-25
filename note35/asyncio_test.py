import asyncio
import aiohttp
from aiohttp import web
import pprint
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
                
def getPeopleInfo(loop, names):
    queryCoroutines = [getPersonInfo(name) for name in names]
    queryDone = asyncio.wait(queryCoroutines)
    futuresDone,_ = loop.run_until_complete(queryDone)
    results = {}
    for future in futuresDone:
        personInfo = future.result()
        results[personInfo['name']] = personInfo
    return results

names = ['Han Meimei', 'Brus Lee', 'Jack Chen']
loop = asyncio.get_event_loop()
results = getPeopleInfo(loop, names)
loop.close()
pprint.pprint(results)
# {'Brus Lee': {'age': '30', 'career': 'engineer', 'name': 'Brus Lee'},
#  'Han Meimei': {'age': '20', 'career': 'student', 'name': 'Han Meimei'},
#  'Jack Chen': {'age': '50', 'career': 'actor', 'name': 'Jack Chen'}}

