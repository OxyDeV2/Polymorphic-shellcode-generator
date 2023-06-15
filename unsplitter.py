def unsplitter(shellcode):
    return '\\x' + '\\x'.join(shellcode[i:i+2] for i in range(0, len(shellcode), 2))

def unsplit_aes(shellcode):
    unsplit_shellcode = "\\" + "\\".join(shellcode[i:i+3] for i in range(0, len(shellcode), 3))
    return unsplit_shellcode


