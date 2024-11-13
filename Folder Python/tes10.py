import hashlib

# Input String
data = "Halo, Python!"

# Hash dengan algoritma MD5
hash_md5 = hashlib.md5(data.encode()).hexdigest()
print("MD5 Hash:", hash_md5)

# Hash dengan algoritma SHA-1
hash_sha1 = hashlib.sha1(data.encode()).hexdigest()
print("SHA-1 Hash:", hash_sha1)

# Hash dengan algoritma SHA-256
hash_sha256 = hashlib.sha256(data.encode()).hexdigest()
print("HSA-256 Hash:", hash_sha256)

# Hash dengan algoritma SHA-512
hash_sha512= hashlib.sha512(data.encode()).hexdigest()
print("SHA-512 Hash:", hash_sha512)