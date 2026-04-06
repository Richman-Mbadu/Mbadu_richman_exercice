
while True:

    phrase = input("Entrez la phrase: ")

    # le rendre en minuscules
    phrase = phrase.lower()

    # Découppage de la phrase en mots

    mots = phrase.split()
    # print(mots)

    # Comptage de nombre de mots

    nombre_mots = len(mots)
    print(f"Nombre total de mots: {nombre_mots}")

    # Le mot le plus long

    long_mot = max(mots, key=len)
    print(f"Le mot le plus long est: {long_mot}")

    # les mots repétés

    rep = {}

    for mot in mots:
        for mot in rep:
            rep[mot] += 1
        else:
            rep[mot] = 1

    # affichage des mots répétés
    print("Mots répétés:")
    for mot, count in rep.items():
        print(f"{mot} : {count}")