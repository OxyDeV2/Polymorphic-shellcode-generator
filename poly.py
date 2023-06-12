## -       Chiffrement de shellcode        - ##
## -     Développé par Skriix & OxyDe      - ##

# Les bibliothèques #
import argparse
from chiffrement_xor import xor
from chiffrement_aes import aes

#Paramètres
parser = argparse.ArgumentParser(description='[+] Chiffrement de shellcode')
parser.add_argument('-s', '--shellcode', help='Entrez le shellcode')
parser.add_argument('-t', '--type', help='Le type de chiffrement [XOR ou]')
parser.add_argument('-k', '--key', help='La clé')
args = parser.parse_args()

#Les variables
shellcode = args.shellcode
key = args.key
type = args.type

def help():
    parser.print_help()
    exit(1)


if __name__ == "__main__":
    if type == "aes":
        aes(shellcode, key)
    elif type == "xor":
        xor(shellcode, key)