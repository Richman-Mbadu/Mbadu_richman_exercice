#!/bin/bash

# Partition à vérifier
PARTITION=${1:-/}

# Vérifier que la partition existe
if ! df "$PARTITION" > /dev/null 2>&1; then
  echo "Erreur : partition invalide."
  exit 1
fi

# Récupération du pourcentage d'utilisation (sans le %)
USAGE=$(df "$PARTITION" | awk 'NR==2 {gsub("%",""); print $5}')

echo "Utilisation de $PARTITION : $USAGE%"

# Conditions
if [ "$USAGE" -ge 90 ]; then
  echo "CRITIQUE : utilisation supérieure à 90% !"
elif [ "$USAGE" -ge 80 ]; then
  echo "ALERTE : utilisation supérieure à 80%."
else
  echo "OK : tout est normal."
fi