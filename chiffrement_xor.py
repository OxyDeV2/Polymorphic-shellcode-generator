from bytetohex import bytetohex
from unsplitter import unsplitter

def xor(shellcode, key, debug):

    # Conversion de la chaîne de caractères en bytes
    shellcode_bytes = bytes.fromhex(shellcode)
    key_bytes = bytes.fromhex(key)

    xored_shellcode = bytearray()
    key_length = len(key_bytes)

    for i in range(len(shellcode_bytes)):
        # Effectuer l'opération de XOR sur chaque octet
        xored_byte = shellcode_bytes[i] ^ key_bytes[i % key_length]
        xored_shellcode.append(xored_byte)
        # Parse du shellcode
        hex_shellcode = bytetohex(xored_shellcode)
        crypted_shellcode = unsplitter(hex_shellcode)


    if debug == "1":
        print("{DEBUG-MOD} shellcode_bytes -> ", shellcode_bytes)
        print("{DEBUG-MOD} key_bytes -> ", key_bytes)   
        print("{DEBUG-MOD} xored_byte -> ", xored_byte)
        print("{DEBUG-MOD} xored_shellcode -> ", xored_shellcode)
        print("{DEBUG-MOD} hex_shellcode -> ", hex_shellcode)
        print("\n --- # ---------- # ---\n")
    else:
        print("", end="")

        # - Resultat du polymorphisme - #
    print("- Shellcode chiffré : ", crypted_shellcode, "\n- Taille : ",len(crypted_shellcode)/4," octets\n")

