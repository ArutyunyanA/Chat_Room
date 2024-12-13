## Python Chat Application: Client-Server Messaging System

This project implements a client-server chat application in Python using sockets and multithreading. The system supports multiple clients, private messaging, and real-time message broadcasting. It’s a great demonstration of networking fundamentals and multithreaded programming.

# Features

# Server
	•	Handles multiple clients simultaneously using threading.
	•	User registration:
	•	Prompts new clients to provide a username upon connection.
	•	Sends a welcome message and notifies others when a user joins.
	•	Broadcasting:
	•	Messages from one client are sent to all connected clients.
	•	Private Messaging:
	•	Users can send private messages using the format @username: message.
	•	Automatically removes disconnected clients from the chat.

# Client
	•	Connects to the server via IP and port.
	•	Supports real-time message sending and receiving.
	•	Provides the ability to exit the chat gracefully by typing /exit.

# How It Works

# Server
	1.	Start the Server: The server listens for client connections on the specified IP and port.
	2.	User Registration:
	•	When a client connects, they are prompted to enter a username.
	•	The server maintains a list of active clients and their usernames.
	3.	Message Handling:
	•	If a message starts with @username:, the server sends it as a private message.
	•	Otherwise, the message is broadcast to all clients.
	4.	Disconnection Handling:
	•	The server removes a client if they disconnect or encounter an error.
	•	Other users are notified when someone leaves the chat.

# Client
	1.	Connect to the Server: The client enters the server’s IP and port to establish a connection.
	2.	Send and Receive Messages:
	•	Users can type messages to send them to the server.
	•	Incoming messages are displayed in real-time.
	3.	Exit the Chat:
	•	Typing /exit disconnects the client gracefully.

# Installation
	1.	Clone the repository:
 
```bash
git clone https://github.com/yourusername/chat-application.git
```


	2.	Navigate to the project directory:
 
```bash
cd chat-application
```


No additional libraries are required as the project relies on Python’s built-in socket and threading modules.

## Usage

# Server
	1.	Start the server:
 
```bash
python server.py
```

	2.	Enter the desired IP and port when prompted.
	3.	The server will listen for incoming connections and display logs for connected/disconnected clients.

# Client
	1.	Start the client:
 
```bash
python client.py
```

	2.	Enter the server’s IP and port to connect.
	3.	Provide a username when prompted, and start chatting!
	4.	Use the format @username: message for private messages.
	5.	Type /exit to leave the chat.

# Example Interaction

Server Output

Server running on 127.0.0.1:5000
Connecting from ('127.0.0.1', 53412)
Registration successful. Welcome to the chat, Alice!
Connecting from ('127.0.0.1', 53413)
Registration successful. Welcome to the chat, Bob!

Client 1 (Alice)

Enter server IP: 127.0.0.1
Enter server port: 5000
Enter your name: Alice
Registration successful. Welcome to the chat, Alice!
Bob has joined the chat.
@Bob: Hi Bob!
Private message from Bob: Hi Alice!

Client 2 (Bob)

Enter server IP: 127.0.0.1
Enter server port: 5000
Enter your name: Bob
Registration successful. Welcome to the chat, Bob!
Alice: Hello, everyone!
@Alice: Hello, Alice!

# File Structure
	•	server.py: The server script for managing clients and handling communication.
	•	client.py: The client script for connecting to the server and sending/receiving messages.

# Customization
	1.	Port and IP Configuration:
	•	Change the default IP or port in the script or via user input.
	2.	User Management:
	•	Add features like user authentication or persistent usernames.
	3.	UI Improvements:
	•	Replace the console-based client with a GUI using frameworks like tkinter or PyQt.
	4.	Advanced Features:
	•	Add message encryption (e.g., using ssl).
	•	Implement message history storage in a database.

# Limitations
	•	The current implementation lacks message encryption, making it insecure for sensitive communication.
	•	Server performance may degrade with a large number of connected clients due to its single-thread-per-client model.

# Future Enhancements
	•	Add encryption for secure communication.
	•	Create a web-based client using WebSockets.
	•	Implement chat room functionality (e.g., multiple rooms with separate topics).

