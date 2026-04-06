#!/bin/bash


if [ -z "$1" ]; then
  echo "Usage: $0 <fichier_log>"
  exit 1
fi

FICHIER=$1

if [ ! -f "$FICHIER" ]; then
  echo "Erreur : le fichier n'existe pas."
  exit 1
fi

total_lignes=$(wc -l < "$FICHIER")

nb_error=$(grep -i "ERROR" "$FICHIER" | wc -l)

nb_warning=$(grep -i "WARNING" "$FICHIER" | wc -l)

echo "=== RÉSUMÉ ==="
echo "Nombre total de lignes : $total_lignes"
echo "Nombre de lignes ERROR : $nb_error"
echo "Nombre de lignes WARNING : $nb_warning"

echo ""
echo "=== 3 DERNIÈRES LIGNES ==="
tail -n 3 "$FICHIER"