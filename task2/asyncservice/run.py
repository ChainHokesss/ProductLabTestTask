from aiohttp import web
import os

from src.app import create_app


if __name__ == '__main__':
    app = create_app()
    web.run_app(
        app,
        host=os.environ.get('AIOHTTP_HOST', 'localhost'),
        port=os.environ.get('AIOHTTP_PORT', 8080)
    )
