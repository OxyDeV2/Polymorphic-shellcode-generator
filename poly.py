## - Générateur de shellcode polymorphique - ##
## -     Développé par Skriix & OxyDe      - ##

# Les bibliothéques #
import sys
from xor.py import xor

# - Ma fonction main - #
def poly(arg1, arg2):
    # Code de la fonction ici #
    print("Arguments reçus :", arg1, arg2)
    if arg2 == "xor":
        #xor(arg1)
    elif arg2 == "aes":
        #aes(arg1)



if __name__ == "__main__":
    if len(sys.argv) != 3 and sys.arg2 != "xor" or sys.arg2 != "aes":
        print("Le programme nécessite 2 arguments minimum.\n")
        print("./poly [shellcode] [chiffrement]")
        print("Deux chiffrements possible : xor ou aes")
        print("Exemple : ./poly fichieravecshellcode.txt xor \n")
    else:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        poly(arg1, arg2)