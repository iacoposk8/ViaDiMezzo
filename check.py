#!/usr/bin/env python3
import re
import sys

def check_patterns(content):
    try:
        if re.search(r'(?<!\\)\%', content):
            print("\033[31mTROVATO SIMBOLO DI % NON PRECEDUTO DA BACKSLASH\033[0m")
            sys.exit(1)
        elif re.search(re.escape(r'}}\endnote'), content):
            print("\033[31mTROVATE NOTE APPICCICATE }}\\endnote INVECE DI }} \\endnote\033[0m")
            sys.exit(1)
        # Cerca 'ma' preceduto da spazio/tilde ma NON da virgola. (?i) ignora maiuscole/minuscole.
        elif re.search(r'(?<!,)(?:[\s~]+)\bma\b', content, re.IGNORECASE):
            print("\033[31mTROVATO 'ma' SENZA VIRGOLA PRECEDENTE [^,]\\sma\\b\033[0m")
            sys.exit(1)
        else:
            print("Nessun pattern pericoloso trovato")
            sys.exit(0)
    except re.error as e:
        print(f"\033[31mErrore regex: {e}\033[0m"); sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilizzo: script.py <file>"); sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as file:
            # Nota: uso r"" nelle stringhe di split per evitare problemi con i backslash
            content = file.read().split(r"\clearpage\section{Prefazione}")[1].split(r"\clearpage\section{Riferimenti}")[0]
        check_patterns(content)
    except Exception as e:
        print(f"\033[31mErrore: {e}\033[0m"); sys.exit(1)