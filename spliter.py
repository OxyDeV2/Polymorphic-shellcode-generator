def spliter(shellcode):
    shellcode = shellcode.replace("\\x", "")
    return shellcode