import asyncio
import websockets
import threading

# message = '{"type": "locationUpdate","data":{"aprilTag":20}}'

# initial message --> Assumption: We'll always start from 'Hotel'
# {"type":"initialCarLocation","data":{"trip":[{"x":1,"y":3}]}}
# follow up
# {"type": "locationUpdate","data":{"aprilTag":6}}

async def main():
    socket = await websockets.connect("ws://192.168.8.128:8080")
    user_input = ""
    while user_input != "q":
        user_input = input("Enter command:\n>> ")

        if user_input == "hotel_goal":
            message = '{"type":"initialCarLocation","data":{"trip":[{"x":2,"y":0}]}}'
            # used exit for testing
            # message = '{"type":"initialCarLocation","data":{"trip":[{"x":1,"y":1}]}}'
            await send_msg(message, socket)
        elif user_input == "tag_hotel_entry":
            message = '{"type": "locationUpdate","data":{"aprilTag":2}}'
            await send_msg(message, socket)
        elif user_input == "tag_hotel_exit":
            message = '{"type": "locationUpdate","data":{"aprilTag":7}}'
            await send_msg(message, socket)
        elif user_input == "giu_goal":
            message = '{"type":"initialCarLocation","data":{"trip":[{"x":0,"y":2}]}}'
            await send_msg(message, socket)
        elif user_input == "tag_giu_exit":
            message = '{"type": "locationUpdate","data":{"aprilTag":6}}'
            await send_msg(message, socket)
        elif user_input == "tag_giu_entry":
            message = '{"type": "locationUpdate","data":{"aprilTag":74}}'
            await send_msg(message, socket)
        elif user_input == "py_goal":
            message = '{"type":"initialCarLocation","data":{"trip":[{"x":2,"y":4}]}}'
            await send_msg(message, socket)
        elif user_input == "tag_py_exit":
            message = '{"type": "locationUpdate","data":{"aprilTag":20}}'
            await send_msg(message, socket)
        elif user_input == "tag_py_entry":
            message = '{"type": "locationUpdate","data":{"aprilTag":96}}'
            await send_msg(message, socket)
        elif user_input == "tag_bump":
            message = '{"type": "locationUpdate","data":{"aprilTag":0}}'
            await send_msg(message, socket)
    exit(42)

async def send_msg(message, socket):
    await socket.send(message)
    # start receiving thread
    await receive_msg(socket)


async def receive_msg(socket, timer=3):
    print("\n\nEntering receive_msg")
    try:
        reply = await asyncio.wait_for(socket.recv(), timeout=timer)
    except:
        print("No reply received")
    else:
        print(f"Received {reply}")
        if "stop" in reply:
            await receive_msg(socket, timer=None)



# asyncio.run(hello())
def confirmation_msg(tag):
    print(f"Successfully send apriltag {tag}")

if __name__ == '__main__':
    asyncio.run(main())

