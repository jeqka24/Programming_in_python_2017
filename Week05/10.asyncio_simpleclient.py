import asyncio

async def tcp_echo_writer(message, loop):
    reader, writer = await asyncio.open_connection("localhost", 10001, loop=loop)

    print("send: %r" % message)
    writer.write(message.encode())
    writer.close()

loop = asyncio.get_event_loop()
message = "Hello, World!"
loop.run_until_complete(tcp_echo_writer(message, loop))
loop.close()
