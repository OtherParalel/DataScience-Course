import socket

class WordCountClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect_to_server(self, message):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.host, self.port))
        client_socket.send(bytes(message, "utf-8"))

        word_count = client_socket.recv(1024).decode("utf-8")
        print(f"Word count: {word_count}")

        client_socket.close()

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 5555
    client = WordCountClient(host, port)

    while True:
        message = input("Enter a phrase: ")
        if message == "exit":
            break
        client.connect_to_server(message)
