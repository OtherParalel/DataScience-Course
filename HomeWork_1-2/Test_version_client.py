import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"  # або встановити IP-адресу сервера
port = 12345  # або встановити той же порт, який використовується на сервері

client_socket.connect((host, port))

while True:
    message = input("Введіть повідомлення: ")
    client_socket.send(bytes(message, "utf-8"))

    if message == "exit":
        break

    response = client_socket.recv(1024).decode("utf-8")
    print(response)

client_socket.close()
