from aiohttp import web
from minter.routes import setup_routes
from minter.utils import create_wallet_pool_trustees

def main(argv):
    app = web.Application()
    app.on_startup.append(create_wallet_pool_trustees)
    setup_routes(app)
    web.run_app(app)


