from aiohttp import web
from routes import setup_routes

import config
config.init()

import logging
logger = logging.getLogger(__name__)

logger.info('Initializing app')
app = web.Application()
logger.info('Setting up routes')
setup_routes(app)
logger.info('Starting web server')
web.run_app(app)
