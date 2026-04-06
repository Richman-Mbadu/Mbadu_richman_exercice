import os

# Demande du nom du dossier

dossier = input("Entrez le nom du dossier: ")

# verification du dossier

if os.path.isdir(dossier):
    print("Le dossier n'existe pas.")

else:
    file =  os.listdir(dossier)
    total_taille = 0
    gros = ("", 0)

    print("\nListe des fichiers: ")

    for fichier in fichiers:
        chemin_complet = os.path.join(dossier, fichier)
        
        # Verfictaion du fichier
        if os.path.isfile(chemin_complet):
            taille = os.path.getsize(chemin_complet)
            taille_totale += taille
            
            print(f"{fichier} : {taille} octets")
            
            # Vérification du plus gros fichier
            if taille > plus_gros[1]:
                plus_gros = (fichier, taille)

    # Affichage du plus gros fichier
    if plus_gros[0]:
        print(f"\n📁 Plus gros fichier : {plus_gros[0]} ({plus_gros[1]} octets)")
    else:
        print("\nAucun fichier trouvé")

    # Affichage de la taille totale
    print(f"\nTaille totale du dossier : {taille_totale} octets")