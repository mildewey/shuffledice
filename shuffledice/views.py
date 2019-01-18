from aiohttp import web
import dice

async def index(request):
    return web.Response(text="Let's roll!")

async def roll_dice(request):
    return web.Response(text="%s" % dice.d6())
