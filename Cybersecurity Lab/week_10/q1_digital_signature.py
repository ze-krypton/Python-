from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

pr = rsa.generate_private_key(public_exponent=65537, key_size=2048)
pu = pr.public_key()

msg = b"affan"

pss = padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)

sig = pr.sign(msg, pss, hashes.SHA256())

try:
    pu.verify(sig, msg, pss, hashes.SHA256())
    print("Valid signature")
except:
    print("Invalid signature")
