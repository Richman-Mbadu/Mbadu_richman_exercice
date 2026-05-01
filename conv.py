from colorama import Fore
import pyfiglet
def affiche():
    font = pyfiglet.figlet_format("BIENVENU")
    font1 = pyfiglet.figlet_format("RICHMAN")
    print(Fore.GREEN+font)
    print(Fore.GREEN+font1)

convention = [128, 64, 32, 16, 8, 4, 2, 1]
def dec_bin():
    while True:
        try:
            # binaire = [1, 0]
            resultat = []
            decimal = int(input("Entrez le decimal (ou entrez 00 pour quitter): "))
            if decimal > 255:
                print("Veulliez entrez le decimal à partir de 0 à 255")
                continue
            elif decimal == 00:
                print("Fin du programme")
                break
            for val in convention:
                if decimal >= val:
                    resultat.append(1)
                    decimal -= val
                else:
                    resultat.append(0)
            print(resultat)
        except ValueError:
            print("Veuillez entrez un nombre ")
            
def bin_dec():
    while True:
        try:
            binaire = input("Entrez le binaire avec des virgules (ou entrez r pour quitter): ")
            if binaire == 'r':
                print("Fin du programme")
                break
            resultat = binaire.split(",")
            resultat = [int(x) for x in resultat]
            # somme = 0
            # for i in range(len(resultat)):
            #     somme += resultat[i] * convention[i]
            #     print(somme)

            calc1 = resultat[0] * convention[0]
            calc2 = resultat[1] * convention[1]
            calc3 = resultat[2] * convention[2]
            calc4 = resultat[3] * convention[3]
            calc5 = resultat[4] * convention[4]
            calc6 = resultat[5] * convention[5]
            calc7 = resultat[6] * convention[6]
            calc8 = resultat[7] * convention[7]

            somme = calc1 + calc2 + calc3 + calc4 
            somme2 = calc5 + calc6 + calc7 + calc8
            sommes = somme + somme2

            print(sommes)
        except ValueError:
            print("Veuillez entrer uniquement 0 ou 1 separés par des virgules")
        except IndexError:
            print("Veuillez entrez le binaire avec les virgules")

def dec_hex():
    while True:
        try:
            decimal = int(input("Entrez le decimal (ou entrez 0 pour quitter): "))
            if decimal == 0:
                print("Fin du programme")
                break
            hexadecimal = hex(decimal).upper()
            print(hexadecimal)
        except ValueError:
            print("Veuillez entrer un nombre valide")
def main():
    while True:
        try:
            print("1. Décimal en binaire")
            print("2. Binaire en décimal")
            print("3. Decimal en hexadecimal")
            print("4. Sorti")
            choix = int(input("Entrez votre choix: "))
            if choix == 1:
                dec_bin()
            elif choix == 2:
                bin_dec()
            elif choix == 3:
                dec_hex()
            elif choix == 4:
                print("Au revoir")
                break
            else:
                print("Entrez un numéro afficher ci-dessus")
            
        except ValueError:
            print("Veuillez entrer un nombre!!")

affiche()
main()
