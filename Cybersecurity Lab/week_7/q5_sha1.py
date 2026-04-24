import hashlib

message = input("enter message: ")
message_bytes = message.encode()
hash_object = hashlib.sha1(message_bytes)
digest = hash_object.hexdigest()
print("message digest (SHA-1):", digest)
