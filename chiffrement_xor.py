
def xor(monshellcode, cle):

    print("Arguments reçus xor :", monshellcode, cle)
    # Parsing du shellcode str -> bytes ou chaques paires de type 0xAA = un octet
    shellcodeparsed = bytes.fromhex(monshellcode)
    xored_monshellcode = bytearray()

    for byte in shellcodeparsed:
        xored_byte = byte ^ cle
        xored_monshellcode.append(xored_byte)

    # Affichage du shellcode XOR et original
    
    print("Shellcode d'origine :", monshellcode)
    print("Shellcode chiffré :", xored_monshellcode)