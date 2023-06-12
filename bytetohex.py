import binascii

def bytetohex(xored_shellcode):
    hex_shellcode = binascii.hexlify(xored_shellcode).decode('utf-8')
    return hex_shellcode