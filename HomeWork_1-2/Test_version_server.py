import socket
import threading

# функція для обробки повідомлення від клієнта
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    # надсилання привітання клієнту
    client_socket.send(bytes("Welcome to the chatroom! Type 'exit' to leave.\n", "utf-8"))

    while True:
        # отримання повідомлення від клієнта
        message = client_socket.recv(1024).decode("utf-8")

        # перевірка, чи не вийшов клієнт
        if message == "exit":
            print(f"[DISCONNECTED] {client_address} disconnected.")
            client_socket.close()
            break

        # виведення повідомлення клієнта
        print(f"[{client_address}] {message}")

        # відповідь чат-бота
        response = chatbot_response(message)
        client_socket.send(bytes(response, "utf-8"))

# функція для запуску сервера
def start_server():
    # встановлення параметрів сервера
    host = "127.0.0.1"
    port = 12345

    # створення сокету сервера
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # прив'язка сокету до адреси та порту сервера
    server_socket.bind((host, port))

    # початок прослуховування вхідних з'єднань
    server_socket.listen()

    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        # очікування нового з'єднання
        client_socket, client_address = server_socket.accept()

        # запуск нового потоку для обробки з'єднання з клієнтом
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# функція для відповіді чат-бота
def chatbot_response(message):
    if "дякую" in message.lower():
        return "Не має за що. Що нового?"
    elif "погода" in message.lower():
        return "На жаль, я не можу надати інформацію про погоду. Спробуйте дізнатися на сайті погоди."
    elif "привіт" in message.lower():
        return "Привіт! Як справи?"
    else:
        return "Вибачте, я не розумію вас. Можливо, спробуйте сказати щось інше."


# запуск сервер
start_server()
