This project implements a simple, end-to-end encrypted chat application using Python's socket library for network communication and the PyCryptodome library for strong hybrid encryption.

The application uses the following cryptographic scheme:

RSA with PKCS#1 OAEP for key exchange.

AES in EAX mode for symmetric message encryption (Authenticated Encryption with Associated Data).

This hybrid approach leverages the speed of symmetric encryption (AES) for the message content and the security of asymmetric encryption (RSA) for securely transmitting the short, randomly generated AES session key.

🛠️ Requirements
Python 3.x

The pycryptodomex (or pycryptodome) library.

Installation
Bash

pip install pycryptodomex
📂 Project Files
File Name	Description
rsa_keys.py	Utility script to generate a pair of 2048-bit RSA private.pem and public.pem keys.
crypto_utils.py	Contains core cryptographic functions for loading keys, encrypting messages (using hybrid RSA-AES/EAX), and decrypting messages.
chat_server.py	The chat server application. Listens on 0.0.0.0:12345 and uses its own private key (private.pem) to decrypt incoming messages and the client's public key (public.pem) to encrypt outgoing messages.
chat_client.py	The chat client application. Connects to 127.0.0.1:12345. Uses the server's public key (public.pem) for encryption and its own private key (private.pem) for decryption.
private.pem	
Server's private key. 

public.pem	
Server's public key. 


Export to Sheets

🚀 Usage
Step 1: Generate RSA Keys
Run the key generation script. This creates private.pem and public.pem in the project directory.

Bash

python rsa_keys.py
Step 2: Key Distribution (Crucial for a real scenario)
In a real-world two-party chat (Alice and Bob):

Alice (Server) needs to share her public key with Bob.

Bob (Client) needs to share his public key with Alice.

For this simple demo using the same key pair for both:

The server uses private.pem (for decrypting) and public.pem (for encrypting).

The client uses private.pem (for decrypting) and public.pem (for encrypting).

Step 3: Start the Server
Open the first terminal, navigate to the project folder, and run the server:

Bash

python chat_server.py
It will print "Connected by ('<client_ip>', <port>)" once the client connects.

Step 4: Start the Client
Open a second terminal, navigate to the project folder, and run the client:

Bash

python chat_client.py
The client will automatically attempt to connect to the server at 127.0.0.1:12345.

Step 5: Chat!
You can now type messages in either terminal. The messages will be automatically encrypted before sending and decrypted upon receiving.

⚠️ Important Note for Real Use
The current setup uses the same key pair (private.pem/public.pem) for both the server and the client for demonstration purposes. For a real, secure two-way chat, you must:

Generate two separate key pairs (one for Alice/Server, one for Bob/Client).

Update chat_server.py to use:

Alice's Private Key for decryption.

Bob's Public Key for encryption.

Update chat_client.py to use:

Bob's Private Key for decryption.

Alice's Public Key for encryption.
