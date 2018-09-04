from aiohttp import web
from minter.utils import build_mint_req


async def transfer(request):
    req = await build_mint_req(request)
    return web.Response(text=req)
