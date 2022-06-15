import asyncio
import websockets

message = '{"type": "locationUpdate","data":{"aprilTag":20}}'

# initial message --> Assumption: We'll always start from 'Hotel'
# {"type":"initialCarLocation","data":{"trip":[{"x":1,"y":3}]}}
# follow up
# {"type": "locationUpdate","data":{"aprilTag":6}}


async def hello():
    async with websockets.connect("ws://192.168.8.128:8080") as websocket:
        await websocket.send(message)
        reply = await websocket.recv()
        print(f"Received {reply}")

# asyncio.run(hello())

if __name__ == '__main__':
    user_input = ""
    while user_input != "q":
        user_input = input("Enter command:\n>> ")

        if user_input == "hotel_start":
            print("Successfully send hotel_start")
            asy