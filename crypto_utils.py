# crypto_utils.py
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64

def load_public_key(path):
    with open(path, "rb") as f:
        return RSA.import_key(f.read())

def load_private_key(path):
    with open(path, "rb") as f:
        return RSA.import_key(f.read())

def encrypt_message(message, receiver_pubkey):
    session_key = get_random_bytes(16)  # AES key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    cipher_rsa = PKCS1_OAEP.new(receiver_pubkey)
    enc_session_key = cipher_rsa.encrypt(session_key)

    return base64.b64encode(enc_session_key + cipher_aes.nonce + tag + ciphertext).decode()

def decrypt_message(encrypted, private_key):
    encrypted = base64.b64decode(encrypted)
    enc_session_key = encrypted[:256]
    nonce = encrypted[256:272]
    tag = encrypted[272:288]
    ciphertext = encrypted[288:]

    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    message = cipher_aes.decrypt_and_verify(ciphertext, tag)
    return message.decode()
