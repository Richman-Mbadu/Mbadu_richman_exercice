#!/bin/bash

# Vérifier qu'un fichier est fourni
if [ -z "$1" ]; then
  echo "Usage: $0 <fichier_utilisateurs>"
  exit 1
fi

FICHIER=$1

# Vérifier que le fichier existe
if [ ! -f "$FICHIER" ]; then
  echo "Erreur : le fichier n'existe pas."
  exit 1
fi

# Mot de passe temporaire
PASSWORD_TEMP="Temp1234"

# Lecture du fichier ligne par ligne
while read -r utilisateur
do
  [ -z "$utilisateur" ] && continue

  echo "Création de l'utilisateur : $utilisateur"

  # Créer l'utilisateur avec dossier personnel
  useradd -m "$utilisateur"

  # Définir le mot de passe
  echo "$utilisateur:$PASSWORD_TEMP" | chpasswd

  # Forcer le changement de mot de passe à la première connexion
  chage -d 0 "$utilisateur"

done < "$FICHIER"

echo "Tous les utilisateurs ont été créés."