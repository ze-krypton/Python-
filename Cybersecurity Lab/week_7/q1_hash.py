import hashlib

message = input("Enter Message: ")
message_bytes = message.encode()
hash_object = hashlib.sha256(message_bytes)
hash_value = hash_object.hexdigest()
print("Hash:", hash_value)
