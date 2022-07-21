from aiohttp import web

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