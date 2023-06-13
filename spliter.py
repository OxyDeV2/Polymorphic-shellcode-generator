def spliter(shellcode, debug):
    shellcode = shellcode.replace("\\x", "")
    if debug == "1":
        print("{DEBUG-MOD} splited_var -> ", shellcode)
    else:
        print("", end="")
    return shellcode