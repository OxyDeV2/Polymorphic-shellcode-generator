## - Générateur de shellcode polymorphique - ##
## -     Développé par Skriix & OxyDe      - ##

# Les bibliothèques #
import sys, argparse
from chiffrement_xor import xor

#Paramètres
parser = argparse.ArgumentParser(description='[+] Chiffrement shellcode')
parser.add_argument('-s', '--shellcode', help='Entrez le shellcode')
parser.add_argument('-t', '--type', help='Le type de chiffrement')
parser.add_argument('-k', '--key', help='La clé')
args = parser.parse_args()

def help():
    parser.print_help()
    exit(1)

# - Ma fonction main - #
def poly(arg1, arg2):
    print("Arguments reçus :", arg1, arg2)
    if arg2 == "xor":
        print("test")
        #xor(arg1)
    elif arg2 == "aes":
        print("test")
        #aes(arg1)

if __name__ == "__main__":

    shellcode = args.shellcode
    key = args.shellcode
    type = args.shellcode

    if len(sys.argv) != 3 and type != "xor" or type != "aes":
        help()
        print("Le programme nécessite 2 arguments minimum.\n")
        print("./poly [shellcode] [chiffrement]")
        print("Deux chiffrements possible : xor ou aes")
        print("Exemple : ./poly fichieravecshellcode.txt xor \n")
    else:
        poly(key, shellcode)