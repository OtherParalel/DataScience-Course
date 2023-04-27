import asyncio
import socket

async def add(x, y):
    return x + y

async def subtract(x, y):
    return x - y

async def multiply(x, y):
    return x * y

async def handle_client(reader, writer):
    # Отримати два числа від клієнта
    data = await reader.read(1024)
    message = data.decode().strip()
    x, y = message.split()

    # Виконати арифметичні операції над числами
    result_add = await add(int(x), int(y))
    result_subtract = await subtract(int(x), int(y))
    result_multiply = await multiply(int(x), int(y))

    # Відправити результати клієнту
    response = f"{result_add} {result_subtract} {result_multiply}\n"
    writer.write(response.encode())
    await writer.drain()

    # Закрити з'єднання
    writer.close()

async def main():
    # Створити сокет для сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 8888))
    server_socket.listen()

    # Створити сервер на основі сокета
    server = await asyncio.start_server(handle_client, sock=server_socket)

    async with server:
        await server.serve_forever()

asyncio.run(main())
