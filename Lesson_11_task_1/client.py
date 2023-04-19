import socket

server_address = '::1'  # Використовуємо IPv6 адресу localhost
server_port = 55000  # Порт сервера

# Створюємо сокет
client_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Підключаємося до сервера
client_socket.connect((server_address, server_port))

# Вводимо дві цифри
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

# Відправляємо дві цифри на сервер
message = f"{num1} {num2}"
client_socket.sendall(message.encode())

# Прийом відповіді від сервера
response = client_socket.recv(1024).decode()
print("Сума двох чисел:", response)

# Закриваємо з'єднання
client_socket.close()
