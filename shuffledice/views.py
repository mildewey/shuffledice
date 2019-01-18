from aiohttp import web
import dice

import logging
logger = logging.getLogger(__name__)

async def index(request):
    logger.info('Fetching index with request: %s' % request)
    return web.Response(text="Let's roll!")

async def roll_dice(request):
    return web.Response(text="%s" % dice.d6())
