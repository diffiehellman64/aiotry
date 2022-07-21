from aiohttp import web
from models.fill_db import create_database

create_database()

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")

@routes.get('/about')
async def hello(request):
    return web.Response(text="about")

@routes.post('/about')
async def hello(request):
    return web.Response(text="about")

app = web.Application()
app.add_routes(routes)
web.run_app(app)