import asyncio
from asyncio.events import Handle
import json
from aiohttp import web


async def initWebServer(loop: asyncio.AbstractEventLoop, host: str, port: str):
    port = int(port)
    app = web.Application(loop=loop)
    app.router.add_routes([web.get('/',home),web.get('/{name}',home)])
    handler = app.make_handler()
    server = await loop.create_server(handler, host=host, port=port)
    return server.sockets[0].getsockname()


def home(request):
    people = {'Han Meimei': {'name': 'Han Meimei', 'age': '20', 'career': 'student'},
              'Brus Lee': {'name': 'Brus Lee', 'age': '30', 'career': 'engineer'}}
    query = request.match_info.get('name', "").strip()
    print("receive query name:{}".format(query))
    resp = {'status':'fail','result':{}}
    if query in people:
        resp['status'] = 'success'
        resp['result'] = people[query]
    html = json.dumps(resp)
    return web.Response(content_type='application/json', text=html)


loop = asyncio.get_event_loop()
host = loop.run_until_complete(initWebServer(loop, '127.0.0.1', '8888'))
print('Server on {!s}'.format(host))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
print('Server shutting down.')
loop.close()
