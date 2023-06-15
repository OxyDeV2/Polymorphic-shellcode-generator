from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Fonction pour chiffrer le shellcode en utilisant AES en mode CBC
def encrypt_shellcode(shellcode, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_shellcode = pad(shellcode.encode(), AES.block_size)
    encrypted_shellcode = cipher.encrypt(padded_shellcode)
    return iv, encrypted_shellcode

# Fonction pour déchiffrer le shellcode en utilisant AES en mode CBC
def decrypt_shellcode(encrypted_shellcode, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_shellcode = cipher.decrypt(encrypted_shellcode)
    unpadded_shellcode = unpad(decrypted_shellcode, AES.block_size)
    return unpadded_shellcode