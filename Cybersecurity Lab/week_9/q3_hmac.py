import hmac
import hashlib

key = b"secret_key"
message = b"Hello World"

send_value = hmac.new(key, message, hashlib.sha256).hexdigest()
print("Generated HMAC:", send_value)

hmac_receiver = hmac.new(key, message, hashlib.sha256).hexdigest()

if send_value == hmac_receiver:
    print("Message is authentic (HMAC matches)")
else:
    print("Message is tampered (HMAC does not match)")
