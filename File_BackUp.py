import os
import shutil
"""
Scrivi una funzione "file_backup" che sia in grado 
di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:

- Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente 
  tramite input
- Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito
  e qualora questa non fosse presente dovrà crearla
- La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare 
  che non esiste    """
percorso_scan=input("Inserisci il percorso di scansione: ")
tipo_file=input("Inserisci il tipo di file di cui vuoi fare il BackUp: ")
percorso_back=input("Inserisci il percorso di BackUp: ")

def back_up(scan,tipo,back):
    if not os.path.isdir(scan):   # se la cartella da scannerizzare scelta non esiste...
        print(f"Il percorso di scansione {scan} non è valido!")
        return None
    if not os.path.isdir(back): # se la cartella di back up scelta non esiste...
        print(f"Il percorso di BackUp {back} non esiste! \nCreo cartella indicata...\n")
        os.makedirs(back)       # creo cartello col percorso scelto per backup
    print(f"Copia dei file in {back} in corso...\n")
    for cartella,sottocartella,files in os.walk(scan):#controllo cartella,sottocartella e files in percorso scan
        for file in files:  # per ogni file tra tutti i files
            if file.endswith(tipo): #se finisce con l'estensione richiesta
                shutil.copy(os.path.join(cartella,file),back)# copio da percorso scan a percorso backup
    print("BackUp terminato!")

back_up(percorso_scan,tipo_file,percorso_back)
input("")
