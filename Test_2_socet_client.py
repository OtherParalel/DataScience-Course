import asyncio

async def send_message(x, y):
    # Відправити запит серверу
    reader, writer = await asyncio.open_connection('localhost', 8888)
    message = f"{x} {y}\n"
    writer.write(message.encode())

    # Отримати відповідь від серверу
    data = await reader.read(1024)
    response = data.decode().strip()

    # Розділити відповідь на результати арифметичних операцій
    result_add, result_subtract, result_multiply = response.split()
    print(f"Результати: Додавання: {result_add}, Віднімання: {result_subtract}, Множення: {result_multiply}")

    # Закрити з'єднання
    writer.close()

asyncio.run(send_message(5, 3))
