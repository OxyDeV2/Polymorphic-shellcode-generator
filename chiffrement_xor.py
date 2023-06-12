from bytetohex import bytetohex
from unsplitter import unsplitter

def xor(shellcode, key):

    # Conversion de la chaîne de caractères en bytes
    shellcode_bytes = bytes.fromhex(shellcode)
    key_bytes = bytes.fromhex(key)

    xored_shellcode = bytearray()
    key_length = len(key_bytes)

    for i in range(len(shellcode_bytes)):
        # Effectuer l'opération de XOR sur chaque octet
        xored_byte = shellcode_bytes[i] ^ key_bytes[i % key_length]
        xored_shellcode.append(xored_byte)
        hex_shellcode = bytetohex(xored_shellcode)
        crypted_shellcode = unsplitter(hex_shellcode)

    
    print("Shellcode chiffré -> ", crypted_shellcode)