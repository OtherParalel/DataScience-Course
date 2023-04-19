import socket

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.bind(('::1', 55000))
sock.listen(10)
print('Server is running, please press ctrl+c to stop')
while True:
    try:
        conn, addr = sock.accept()
        print('Connected:', addr)
        data = conn.recv(1024).decode('utf-8')
        nums = data.split()  # Розділяємо отримані дані на окремі числа
        if len(nums) == 2:
            num1 = int(nums[0])
            num2 = int(nums[1])
            result = num1 + num2  # Обчислюємо суму
            conn.send(str(result).encode())  # Відправляємо суму назад клієнту
        else:
            conn.send("Invalid input".encode())  # Відправляємо повідомлення про помилку
        conn.close()
    except KeyboardInterrupt:
        print('Server stopped by user')
        sock.close()  # Close the socket before exiting
        break
    except Exception as e:
        print('Error occurred:', e)
        conn.close()
        sock.close()
