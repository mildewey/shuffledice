from aiohttp import web

import logging
logger = logging.getLogger(__name__)

async def index(request):
    logger.info('Fetching index with request: %s' % request)
    return web.Response(text="Let's roll!")
