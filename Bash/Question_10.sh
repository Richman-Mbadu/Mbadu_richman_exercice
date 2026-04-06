#!/bin/bash

# Demande à l'utilisateur de saisir un nom de fichier
read -p "Entrez le nom du fichier : " fichier

# Vérifier si le fichier existe
if [ -e "$fichier" ]; then
  echo "Le fichier existe."

  # Taille du fichier (en octets)
  taille=$(stat -c%s "$fichier")

  # Permissions du fichier
  permissions=$(stat -c%A "$fichier")

  echo "Taille : $taille octets"
  echo "Permissions : $permissions"
else
  echo "Le fichier n'existe pas."
fi