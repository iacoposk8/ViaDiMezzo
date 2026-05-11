import subprocess
import os
import shutil

def comprimi_pdf(input_path, output_path, livello_compressione=4):
    """
    Comprime un PDF utilizzando Ghostscript.
    
    livello_compressione:
    0: default (quasi nessuna compressione)
    1: prepress (alta qualità, file grande - 300 dpi)
    2: printer (buona qualità, per stampanti - 300 dpi)
    3: ebook (qualità media, ottimo compromesso - 150 dpi)
    4: screen (bassa qualità, file piccolissimo, ideale per schermi - 72 dpi)
    """
    
    qualita = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Cerca l'eseguibile corretto di Ghostscript in base al sistema operativo
    comandi_gs =['gs', 'gswin64c', 'gswin32c', 'gswin64.exe']
    eseguibile_gs = None
    
    for comando in comandi_gs:
        if shutil.which(comando):
            eseguibile_gs = comando
            break
            
    if not eseguibile_gs:
        print("Errore: Ghostscript non è installato o non è nelle variabili d'ambiente (PATH).")
        print("Scaricatelo da https://ghostscript.com/releases/gsdnld.html")
        return

    if not os.path.exists(input_path):
        print(f"Errore: Il file '{input_path}' non è stato trovato nella cartella.")
        return

    print(f"Inizio la compressione di '{input_path}'...")
    print("Potrebbe volerci qualche istante (dipende dal numero di pagine)...")

    # Costruisci il comando per Ghostscript
    comando =[
        eseguibile_gs,
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        f'-dPDFSETTINGS={qualita[livello_compressione]}',
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        f'-sOutputFile={output_path}',
        input_path
    ]

    try:
        # Esegue il comando
        subprocess.run(comando, check=True)
        
        # Calcola le dimensioni finali
        peso_iniziale = os.path.getsize(input_path) / (1024 * 1024)
        peso_finale = os.path.getsize(output_path) / (1024 * 1024)
        
        print("\n--- COMPRESSIONE COMPLETATA ---")
        print(f"File salvato come: {output_path}")
        print(f"Dimensione Originale: {peso_iniziale:.2f} MB")
        print(f"Nuova Dimensione:   {peso_finale:.2f} MB")
        
    except subprocess.CalledProcessError as e:
        print(f"Si è verificato un errore durante la compressione: {e}")

# --- ESECUZIONE ---
file_input = "../../../Libro.pdf"
file_output = "Libro_compresso.pdf"

# Usiamo il livello 4 (/screen) per cercare di forzare i 35MB a scendere verso i 5MB.
comprimi_pdf(file_input, file_output, livello_compressione=4)