def unsplitter(shellcode):
    return '\\x' + '\\x'.join(shellcode[i:i+2] for i in range(0, len(shellcode), 2))