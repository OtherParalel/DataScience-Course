import socket

class WordCountServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(1)
        print(f"[LISTENING] Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[NEW CONNECTION] {client_address} connected.")

            message = client_socket.recv(1024).decode("utf-8")
            word_count = len(message.split())
            client_socket.send(bytes(str(word_count), "utf-8"))

            print(f"[{client_address}] Word count: {word_count}")
            client_socket.close()

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5555
    server = WordCountServer(host, port)
    server.start_server()
