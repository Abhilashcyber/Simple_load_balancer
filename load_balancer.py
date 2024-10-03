import aiohttp
import asyncio
from aiohttp import web

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    async def forward_request(self, client_path):
        server = self.get_server()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(f"http://{server}{client_path}") as response:
                    return await response.text()
            except Exception as e:
                return f"Error forwarding request to {server}: {e}"

load_balancer = LoadBalancer(["localhost:8000", "localhost:8001", "localhost:8002"])

async def handle(request):
    path = request.path
    response = await load_balancer.forward_request(path)
    return web.Response(text=response)

app = web.Application()
app.add_routes([web.get('/{tail:.*}', handle)])

if __name__ == "__main__":
    web.run_app(app, port=8080)
