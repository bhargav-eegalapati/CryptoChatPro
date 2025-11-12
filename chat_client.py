# chat_client.py
import socket, threading
from crypto_utils import load_private_key, load_public_key, encrypt_message, decrypt_message

SERVER_IP = '127.0.0.1'
PORT = 12345

private_key = load_private_key("private.pem")
receiver_pubkey = load_public_key("public.pem")  # replace with receiver’s pubkey in real use

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

def receive():
    while True:
        try:
            encrypted = client.recv(4096).decode()
            msg = decrypt_message(encrypted, private_key)
            print(f"\nFriend: {msg}")
        except:
            print("Connection closed.")
            break

threading.Thread(target=receive).start()

while True:
    msg = input("You: ")
    enc = encrypt_message(msg, receiver_pubkey)
    client.send(enc.encode())
