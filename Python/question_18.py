import csv

# Ouverture et lecture du fichier CSV
with open('etudiants.csv', newline='', encoding='utf-8') as file:
    lect = csv.reader(file)

    # Ignorer l'entête du fichier
    next(lect)

    etudiants = []
    for ligne in lect:
        nom = ligne[0]
        # prenom = ligne[1]
        etudiants.append((nom, prenom))

# Affichage des étudiants
print("Liste des étudiants:")
for nom, note in etudiants:
    print(f"{nom} {note}")

# Calcul de la moyenne générale
somme_gene = sum(float(note) for _, note in etudiants)
moyenne_gene = somme_gene / len(etudiants)
print("\nMoyenne générale:", moyenne_gene)

# affichage des étudiants ayant une note inférieure à 10

print("\nÉtudiants ayant une note inférieure à 10: ")
for nom, note in etudiants:
    if float(note) < 10:
        print(f"{nom} : {note}")
