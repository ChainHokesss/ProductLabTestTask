import json
from aiohttp import web

from . import async_service


router = web.RouteTableDef()


@router.post('/get_data_by_article')
async def test(request):
    data = await request.json()
    data = json.loads(data)

    try:
        articles = data['articles']

    except Exception as e:
        return web.Response("json should have 'articles' field", status=400)

    result = await async_service.main(articles)
    return web.Response(text=json.dumps(result), status=200)
