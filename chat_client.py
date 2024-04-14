import socket
import threading

class ChatClient:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print("Подключено к серверу.")

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print(message)
            except Exception as e:
                print(f"Подключение к серверу потеряно: {e}")
                break

if __name__ == "__main__":
    host = input("Введите IP-адрес сервера: ")
    port = int(input("Введите порт сервера: "))
    client = ChatClient(host, port)
    client.connect()

    receive_thread = threading.Thread(target=client.receive_messages)
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == "/exit":
            client.send_message(message)
            break
        else:
            client.send_message(message)
