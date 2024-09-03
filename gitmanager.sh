#!/bin/bash

echo "Scegli un'opzione:"
echo "1. Pull - Scarica i file da github a locale"
echo "2. Commit - Carica i file da locale a github"
echo "3. Rimuovi tutti i commit"

read -p "Inserisci il numero dell'opzione desiderata: " scelta

if [ "$scelta" = "1" ]; then
	git pull
elif [ "$scelta" = "2" ]; then
	git add .
	git commit -m "Update"
	git push
elif [ "$scelta" = "3" ]; then
	git checkout --orphan nuovo-branch
	git add -A
	git commit -am "First commit"
	git branch -D main
	git branch -m main
	git push -f origin main
else
	echo "Scelta non valida."
fi