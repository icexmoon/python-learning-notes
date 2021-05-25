import asyncio
import aiohttp
from aiohttp import web
import pprint
from tqdm import tqdm
import os


async def getHttpResp(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            ctype = response.headers.get('Content-type', '').lower()
            if response.status == 200:
                if 'json' in ctype:
                    queryResult = await response.json()
                else:
                    queryResult = await response.read()
                return queryResult
            elif response.status == 404:
                raise web.HTTPNotFound
            else:
                raise web.HTTPServerError


async def getPersonInfo(name, semphore):
    url = "http://myweb.com/?name={}".format(name)
    async with semphore:
        personInfoResp = await getHttpResp(url)
    if personInfoResp['status'] == 'success':
        personInfo = personInfoResp['result']
        personPictureUrl = personInfo['picture']
        async with semphore:
            picContent = await getHttpResp(personPictureUrl)
        _, _, picName = personPictureUrl.rpartition('/')
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, saveFile, picContent, picName)
        filePath = os.getcwd()+'\\'+picName
        personInfo['localPicture'] = filePath
    else:
        personInfo = {}
    return personInfo


def saveFile(content, filePath):
    with open(file=filePath, mode='wb') as fopen:
        fopen.write(content)


async def getPeopleInfo(names, semphore):
    queryCoroutines = [getPersonInfo(name, semphore) for name in names]
    completedFutures = asyncio.as_completed(queryCoroutines)
    completedFutures = tqdm(completedFutures, total=len(names))
    results = {}
    for future in completedFutures:
        personInfo = await future
        results[personInfo['name']] = personInfo
    return results
names = ['Han Meimei', 'Brus Lee', 'Jack Chen']
loop = asyncio.get_event_loop()
MAX_REQ = 10
semphore = asyncio.Semaphore(MAX_REQ)
results = loop.run_until_complete(getPeopleInfo(names, semphore))
loop.close()
pprint.pprint(results)
# 100%|███████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:10<00:00,  3.36s/it]
# {'Brus Lee': {'age': '30',
#               'career': 'engineer',
#               'localPicture': 'D:\\workspace\\python\\python-learning-notes\\note35\\2.png',
#               'name': 'Brus Lee',
#               'picture': 'http://myweb.com/images/2.png'},
#  'Han Meimei': {'age': '20',
#                 'career': 'student',
#                 'localPicture': 'D:\\workspace\\python\\python-learning-notes\\note35\\1.jpg',
#                 'name': 'Han Meimei',
#                 'picture': 'http://myweb.com/images/1.jpg'},
#  'Jack Chen': {'age': '50',
#                'career': 'actor',
#                'localPicture': 'D:\\workspace\\python\\python-learning-notes\\note35\\3.png',
#                'name': 'Jack Chen',
#                'picture': 'http://myweb.com/images/3.png'}}
