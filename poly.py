## - Générateur de shellcode polymorphique - ##
## -     Développé par Skriix & OxyDe      - ##

# Les bibliothéques #
import sys

# - Ma fonction main - #
def poly(arg1, arg2):
    # Code de la fonction ici #
    print("Arguments reçus :", arg1, arg2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Le programme nécessite 2 arguments minimum.\n")
        print("python3 poly [shellcode] [chiffrement]")
        print("Exemple :python3 poly fichieravecshellcode.txt xor \n")
    else:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        poly(arg1, arg2)
