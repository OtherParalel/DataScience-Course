import socket
import threading

class ChatbotServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.responses = {
            'Привіт': 'Привіт! Я чат-бот. Чим можу допомогти?',
            'Як справи?': 'Добре, дякую! Як ви?',
            'Що робиш?': 'Я відповідаю на ваші повідомлення!',
            'Поки': 'До побачення! Буду радий вам допомогти знову!',
        }

    def handle_client(self, client_socket, client_address):
        print(f"[NEW CONNECTION] {client_address} connected.")
        client_socket.send(bytes("Welcome to the chatroom! Type 'exit' to leave.\n", "utf-8"))

        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")

                if message.strip() == "exit":
                    print(f"[DISCONNECTED] {client_address} disconnected.")
                    client_socket.close()
                    break

                print(f"[{client_address}] {message}")
                response = self.chatbot_response(message)
                client_socket.send(bytes(response, "utf-8"))

            except ConnectionResetError:
                print(f"[ERROR] {client_address} connection reset.")
                break

    def chatbot_response(self, message):
        if "дякую" in message.lower():
            return "Не має за що. Що нового?"
        elif "погода" in message.lower():
            return "На жаль, я не можу надати інформацію про погоду. Спробуйте дізнатися на сайті погоди."
        elif message.strip() in self.responses:
            return self.responses[message.strip()]
        else:
            return "Ви кажете? Я не знаю, що відповісти на це. Спробуйте запитати щось інше."

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('127.0.0.1', 55000))
        server_socket.listen()
        print(f"[LISTENING] Server is listening on {self.host}:{self.port}")

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()

            except KeyboardInterrupt:
                print("[SERVER SHUTDOWN] Shutting down server.")
                break

            except Exception as e:
                print("[ERROR] ", e)
                break

        server_socket
