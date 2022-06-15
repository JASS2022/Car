import asyncio
import websockets

message = '{"type": "locationUpdate","data":{"aprilTag":20}}'

async def hello():
    async with websockets.connect("wss://jass22.finkmartin.com/car") as websocket:
        await websocket.send(message)
        reply = await websocket.recv()
        print(f"Received {reply}")

asyncio.run(hello())