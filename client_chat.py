import socket
import threading

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message:
                print(f"Server: {message}")
        except:
            print("An error occurred!")
            client.close()
            break

def send_message():
    while True:
        message = input("")
        client.send(message.encode('utf-8'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
