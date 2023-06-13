## -       Chiffrement de shellcode        - ##
## -     Développé par Skriix & OxyDe      - ##

# Les bibliothèques #
import argparse
import binascii
from chiffrement_xor import xor
from chiffrement_aes import aes
from spliter import spliter

#Paramètres
parser = argparse.ArgumentParser(description='[+] Chiffrement de shellcode')
parser.add_argument('-s', '--shellcode', help='Entrez le shellcode')
parser.add_argument('-t', '--type', help='Le type de chiffrement [XOR ou AES]')
parser.add_argument('-k', '--key', help='La clé')
parser.add_argument('-d','--debug', help='Activation du debug [0 ou 1]')
args = parser.parse_args()

#Les variables
shellcode = args.shellcode
key = args.key
type = args.type
debug = args.debug


def help():
    parser.print_help()
    exit(1)


if __name__ == "__main__":
    if type == "aes":
        aes(spliter(shellcode, debug), spliter(key, debug), debug)
    elif type == "xor":
        xor(spliter(shellcode, debug), spliter(key, debug), debug)
    else:
        parser.print_help()