import time
import hmac
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

message = b"Hello World"

# -------------------- MAC (HMAC) --------------------
secret_key = b'secret123'
start = time.time()
mac = hmac.new(secret_key, message, hashlib.sha256).digest()
end = time.time()
print("HMAC:", mac)
print("HMAC Generation Time:", end - start)

# -------------------- Digital Signature --------------------
key = RSA.generate(1024)
private_key = key
public_key = key.publickey()
h = SHA256.new(message)
start = time.time()
signature = pkcs1_15.new(private_key).sign(h)
end = time.time()
print("Digital Signature:", signature)
print("Signature Time:", end - start)
