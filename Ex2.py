import hashlib

# Take input from the user
a = input("Enter a string: ")

# Generate MD5 hash
result = hashlib.md5(a.encode())
print("MD5 Hash (bytes):", result.digest())

# Display available hash algorithms
print("Available hashing algorithms:", hashlib.algorithms_guaranteed)
