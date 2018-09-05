from aiohttp import web
from minter.utils import build_mint_req, transfer_funds


async def mint(request):
    try:
        req = await build_mint_req(request)
    except Exception as e:
        raise web.HTTPForbidden(reason=str(e))
    return web.Response(text=req)


async def transfer(request):
    try:
        req = await transfer_funds(request)
    except Exception as e:
        raise web.HTTPForbidden(reason=str(e))
    return web.Response(text=req)
