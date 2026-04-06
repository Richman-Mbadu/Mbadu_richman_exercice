#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <dossier>"
  exit 1
fi

DOSSIER=$1

# Vérification du dossier
if [ ! -d "$DOSSIER" ]; then
  echo "Erreur : le dossier n'existe pas."
  exit 1
fi