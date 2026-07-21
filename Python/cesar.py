import unicodedata

def chiffrer_cesar_accents(texte, decalage):
    resultat = ""
    for caractere in texte:
        # Décompose le caractère en lettre de base + accent (NFD)
        decompose = unicodedata.normalize('NFD', caractere)
        lettre_base = decompose[0]
        accent = decompose[1:] if len(decompose) > 1 else ""

        if lettre_base.isalpha() and lettre_base.isascii():
            base = ord('A') if lettre_base.isupper() else ord('a')
            nouvelle_lettre = chr((ord(lettre_base) - base + decalage) % 26 + base)
            # Recombine la nouvelle lettre avec l'accent d'origine
            resultat += unicodedata.normalize('NFC', nouvelle_lettre + accent)
        elif caractere == 'ç':
            resultat += chr((ord('c') - ord('a') + decalage) % 26 + ord('a'))
        elif caractere == 'Ç':
            resultat += chr((ord('C') - ord('A') + decalage) % 26 + ord('A'))
        else:
            resultat += caractere
    return resultat


def dechiffrer_cesar_accents(texte, decalage):
    return chiffrer_cesar_accents(texte, -decalage)


# Exemple d'utilisation
if __name__ == "__main__":
    message = input("Veuillez entrer le message")
    cle = int(input("Entrez l'indice(ROT)")

    encrypte = chiffrer_cesar_accents(message, cle)
    decrypte = dechiffrer_cesar_accents(encrypte, cle)

    # print(f"Message original : {message}")
    print(f"Message chiffré  : {encrypte}")
    print(f"Message déchiffré: {decrypte}")
