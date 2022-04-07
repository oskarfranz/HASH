import nacl.utils
import nacl.hash
import nacl.encoding

random = nacl.utils.random(128)
print("Random numbers:\n")
for char in random:
    print(str(char), end=" ")

message = "Arbitrary message".encode('ascii')
print("\n\nHashed word:\n")
hash = nacl.hash.sha256(message, encoder=nacl.encoding.HexEncoder)
print(hash)