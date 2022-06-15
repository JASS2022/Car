import asyncio
import websockets

message = '{"type": "locationUpdate","data":{"aprilTag":20}}'

async def hello():
    async with websockets.connect("ws://192.168.8.128:8080") as websocket:
        await websocket.send(message)
        reply = await websocket.recv()
        print(f"Received {reply}")

asyncio.run(hello())