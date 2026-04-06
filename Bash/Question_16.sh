#!/bin/bash

# Nom du fichier
fichier="rapport_systeme.txt"

# Écriture dans le fichier
echo "===== RAPPORT SYSTÈME =====" > $fichier
echo "" >> $fichier

echo "Nom de la machine :" >> $fichier
hostname >> $fichier
echo "" >> $fichier

echo "Noyau Linux :" >> $fichier
uname -r >> $fichier
echo "" >> $fichier

echo "Adresse IP :" >> $fichier
hostname -I >> $fichier
echo "" >> $fichier

echo "Espace disque :" >> $fichier
df -h >> $fichier
echo "" >> $fichier

echo "Utilisation mémoire :" >> $fichier
free -h >> $fichier
echo "" >> $fichier

echo "Utilisateurs connectés :" >> $fichier
who >> $fichier
echo "" >> $fichier

echo "===== FIN DU RAPPORT =====" >> $fichier