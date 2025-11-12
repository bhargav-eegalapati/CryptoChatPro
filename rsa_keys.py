# rsa_keys.py
from Crypto.PublicKey import RSA

def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as priv:
        priv.write(private_key)
    with open("public.pem", "wb") as pub:
        pub.write(public_key)

if __name__ == "__main__":
    generate_keys()
