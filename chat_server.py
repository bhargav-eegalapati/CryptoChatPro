# chat_server.py
import socket, threading
from crypto_utils import load_private_key, load_public_key, encrypt_message, decrypt_message

private_key = load_private_key("private.pem")
receiver_pubkey = load_public_key("public.pem")  # replace with receiver’s pubkey

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(1)

conn, addr = server.accept()
print("Connected by", addr)

def receive():
    while True:
        try:
            encrypted = conn.recv(4096).decode()
            msg = decrypt_message(encrypted, private_key)
            print(f"\nClient: {msg}")
        except:
            print("Connection closed.")
            break

threading.Thread(target=receive).start()

while True:
    msg = input("You: ")
    enc = encrypt_message(msg, receiver_pubkey)
    conn.send(enc.encode())
