from aiohttp import web

from .routers import router


async def create_app():
    app = web.Application()
    app.add_routes(router)
    return app
