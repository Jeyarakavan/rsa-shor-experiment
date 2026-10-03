import math

# --------------------------------------------------
# SIMPLE RSA DEMONSTRATION
# Educational example only - NOT secure for real use
# --------------------------------------------------

# Step 1: Choose two small prime numbers
p = 3
q = 5

# Step 2: Calculate n
n = p * q

# Step 3: Euler's totient
phi = (p - 1) * (q - 1)

# Step 4: Choose public exponent
e = 3

if math.gcd(e, phi) != 1:
    raise ValueError("e must be coprime with phi(n)")

# Step 5: Calculate private exponent
d = pow(e, -1, phi)

print("========== RSA KEY GENERATION ==========")
print(f"p = {p}")
print(f"q = {q}")
print(f"n = p × q = {n}")
print(f"phi(n) = {phi}")

print("\nPublic Key:")
print(f"(e={e}, n={n})")

print("\nPrivate Key:")
print(f"(d={d}, n={n})")

# --------------------------------------------------
# Encryption
# --------------------------------------------------

message = 7

ciphertext = pow(message, e, n)

print("\n========== ENCRYPTION ==========")
print(f"Original message : {message}")
print(f"Encrypted message: {ciphertext}")

# --------------------------------------------------
# Decryption
# --------------------------------------------------

decrypted = pow(ciphertext, d, n)

print("\n========== DECRYPTION ==========")
print(f"Ciphertext       : {ciphertext}")
print(f"Decrypted message: {decrypted}")