@echo off
setlocal

echo Scegli un'opzione:
echo 1. Pull - Scarica i file da github a locale
echo 2. Commit - Carica i file da locale a github
echo 3. Rimuovi tutti i commit

set /p scelta=Inserisci il numero dell'opzione desiderata: 

if "%scelta%"=="1" (
	git pull
) else if "%scelta%"=="2" (
	python check.py Libro.tex
	del /f /q Libro.aux
	del /f /q Libro.bcf
	del /f /q Libro.ent
	del /f /q Libro.out
	del /f /q Libro.toc
	del /f /q Libro.run.xml
	del /f /q "Libro.synctex(busy)"
	del /f /q Libro.log
	del /f /q Libro.synctex.gz
	git add .
	git commit -m "Update"
	git push	
) else if "%scelta%"=="3" (
	git checkout --orphan nuovo-branch
	git add -A
	git commit -am "First commit"
	git branch -D main
	git branch -m main
	git push -f origin main
) else (
	echo Scelta non valida.
)

endlocal
