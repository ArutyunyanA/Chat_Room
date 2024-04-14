
import socket
import threading

class ChatServer:
   
   def __init__(self, host, port):
       self.host = host
       self.port = port
       self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.clients = {}

   def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Сервер запущен на {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Подключение от {client_address}")
            client_username = self.register_user(client_socket)  # Получаем имя пользователя
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_username))
            client_thread.start()

   def register_user(self, client_socket):
       try:
           client_socket.send("Введите ваше имя: ".encode())
           username = client_socket.recv(1024).decode().strip()
           if not username:
               username = "No Name"
           client_socket.send(f"Регистрация прошла успешно. Добро пожаловать в чат, {username}!\n".encode())
           self.broadcast(f"{username} присоединился к чату.")
           self.clients[username] = client_socket  # Сохраняем имя пользователя и его сокет
           self.send_user_list(client_socket)
           return username  # Возвращаем имя пользователя
       except Exception as e:
           print(f"Ошибка при регистрации пользователя: {e}")
           client_socket.close()

   def handle_client(self, client_socket, client_username):
       while True:
           try:
               message = client_socket.recv(1024).decode()
               if message:
                   if message.startswith("@"):
                       recipient_and_message = message[1:].split(":", 1)
                       recipient_name = recipient_and_message[0].strip()
                       private_message = recipient_and_message[1].strip()
                       if recipient_name in self.clients:
                           recipient_socket = self.clients[recipient_name]
                           recipient_socket.send(f"Личное сообщение от {client_username}: {private_message}".encode())
                       else:
                           client_socket.send("Пользователь не найден.".encode())
                   else:
                       self.broadcast(message)
               else:
                   self.remove_client(client_socket)
                   break
           except Exception as e:
               print(f"Ошибка при обработке клиента: {e}")
               self.remove_client(client_socket)
               break

   def remove_client(self, client_socket):
       for username, socket in self.clients.items():
           if socket == client_socket:
               self.broadcast(f"{username} покинул чат.")
               del self.clients[username]
               client_socket.close()
               break

   def broadcast(self, message):
       for client_socket in self.clients.values():
           try:
               client_socket.send(message.encode())
           except Exception as e:
               print(f"Ошибка при отправке сообщения: {e}")

   def send_user_list(self, client_socket):
       user_list = "Пользователи онлайн: " + ", ".join(self.clients.keys())
       client_socket.send(user_list.encode())

if __name__ == "__main__":
   host = input("Введите IP-адрес сервера: ")
   port = int(input("Введите порт сервера: "))
   server = ChatServer(host, port)
   server.start()





