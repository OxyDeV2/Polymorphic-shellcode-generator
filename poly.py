## -       Chiffrement de shellcode        - ##
## -     Développé par Skriix & OxyDe      - ##

# Les bibliothèques #
from chiffrement_aes import encrypt_shellcode, decrypt_shellcode
import argparse
from chiffrement_xor import xor
from dechiffrement_xor import dexor
from spliter import spliter
from unsplitter import unsplitter, unsplit_aes
import base64

#Paramètres
parser = argparse.ArgumentParser(description='[+] Chiffrement de shellcode')
parser.add_argument('-c', '--encrypt', action='store_true', help='Chiffrer le shellcode')
parser.add_argument('-d', '--decrypt', action='store_true', help='Déchiffrer le shellcode')
parser.add_argument('-s', '--shellcode', help='Le shellcode à chiffrer')
parser.add_argument('-t', '--type', help='Le type de chiffrement [xor ou aes] - Pour dechiffrer [DEXOR]')
parser.add_argument('-k', '--key', help='La clé, pour AES la clé doit faire une taille de 16, 24 ou 32 caractères')
parser.add_argument('--debug', help='Activation du debug [0 ou 1]')
args = parser.parse_args()

#Les variables
shellcode = args.shellcode
key = args.key  
type = args.type
debug = args.debug  

if __name__ == "__main__":
    if args.encrypt and args.shellcode and args.key and args.type == "aes":
        # Chiffrement du shellcode
        shellcode = spliter(args.shellcode, debug)
        key = args.key.encode() 
        iv, encrypted_shellcode = encrypt_shellcode(shellcode, key)
        encrypted_shellcode_b64 = base64.b64encode(encrypted_shellcode).decode("utf-8")
        print("Shellcode chiffré (en base64) :")
        print(encrypted_shellcode_b64)
        print("IV (en base64) :")
        print(base64.b64encode(iv).decode("utf-8"))
    elif args.decrypt and args.type == "aes" and args.key:
        # Déchiffrement du shellcode
        key = args.key.encode()
        encrypted_shellcode_b64 = input("Veuillez saisir le shellcode chiffré (en base64) : ")
        iv_b64 = input("Veuillez saisir l'IV (en base64) : ")
        encrypted_shellcode = base64.b64decode(encrypted_shellcode_b64.encode("utf-8"))
        iv = base64.b64decode(iv_b64.encode("utf-8"))
        decrypted_shellcode = decrypt_shellcode(encrypted_shellcode, key, iv)
        convert_shellcode = decrypted_shellcode.decode('latin-1') 
        split_decrypted_shellcode = unsplit_aes(convert_shellcode)
        print("Shellcode déchiffré :\t", split_decrypted_shellcode)
        print("Longueur du shellcode : ", len(split_decrypted_shellcode))
    elif type == "xor":
        #Chiffrement XOR du shellcode
        xor(spliter(shellcode, debug), spliter(key, debug), debug)
    elif type == "dexor":
        #Déchiffrement XOR du shellcode
        dexor(spliter(shellcode, debug), spliter(key, debug), debug)
    elif args.encrypt and args.decrypt:
         print("Erreur : les options -c et -d sont mutuellement exclusives. Veuillez choisir soit le chiffrement (-c) soit le déchiffrement (-d).")
    else:
        parser.print_help() 