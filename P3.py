#Write a program to implement 2x2 Hill cipher.

import numpy as np

# Function to find modular inverse of determinant
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Encrypt
def hill_cipher_2x2_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    
    # Padding if odd length
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    plaintext_pairs = []
    for i in range(0, len(plaintext), 2):
        pair = [ord(plaintext[i]) - 65, ord(plaintext[i+1]) - 65]
        plaintext_pairs.append(pair)

    key_matrix = np.array(key)
    ciphertext = ""

    for pair in plaintext_pairs:
        pt = np.array(pair).reshape(2, 1)
        ct = np.dot(key_matrix, pt) % 26
        ciphertext += chr(int(ct[0][0]) + 65) + chr(int(ct[1][0]) + 65)

    return ciphertext


# Decrypt
def hill_cipher_2x2_decrypt(ciphertext, key):
    key_matrix = np.array(key)

    # Determinant
    det = int(np.round(np.linalg.det(key_matrix)))
    det = det % 26

    det_inv = mod_inverse(det, 26)

    # Adjugate matrix
    adj = np.array([[key_matrix[1][1], -key_matrix[0][1]],
                    [-key_matrix[1][0], key_matrix[0][0]]])

    key_inverse = (det_inv * adj) % 26

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        pair = [ord(ciphertext[i]) - 65, ord(ciphertext[i+1]) - 65]
        ct = np.array(pair).reshape(2, 1)
        pt = np.dot(key_inverse, ct) % 26
        plaintext += chr(int(pt[0][0]) + 65) + chr(int(pt[1][0]) + 65)

    return plaintext


# Main
plaintext = "HELLO"
key = [[3, 4], [2, 3]]

ciphertext = hill_cipher_2x2_encrypt(plaintext, key)
decrypted = hill_cipher_2x2_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypted)
