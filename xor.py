monshellcode = b"arg"  # Remplacez par votre propre shellcode
cle = 0xAA  # Remplacez par votre propre clé

xored_shellcode = bytearray()

for byte in shellcode:
    xored_byte = byte ^ key
    xored_shellcode.append(xored_byte)

# Affichage du shellcode XORé
print(xored_shellcode)