import os
import shutil
import sys
"""
Scrivi una funzione "file_backup" che sia in grado 
di effettuare copie di backup di determinati tipi di file, con le seguenti caratteristiche:

- Percorso da scansionare, di backup e tipologia di file da copiare dovranno essere passati dall'utente 
  tramite input
- Il programma dovrà verificare la presenza o meno di una cartella di backup al percorso fornito
  e qualora questa non fosse presente dovrà crearla
- La funzione dovrà anche gestire l'eventuale scelta da parte dell'utente, di un percorso da scansionare 
  che non esiste    """


class BackUp:

  def __init__(self):
    self.scan = ""
    self.estensione = ""
    self.backup = ""

  def copy(self):    
    try:
      for cartella, _, files in os.walk(self.scan):
        for file in files:
          if file.endswith(self.estensione):
            shutil.copy(os.path.join(cartella,file), self.backup)
    except:
      print("Errore nella copia dei file!")
    else:
      print("Copia dei file Terminato!")
      input()

  def start(self):
    try:
      self.scan=input("Inserisci il percorso di scansione: ")
      self.estensione=input("Inserisci il tipo di file di cui vuoi fare il BackUp: ")
      self.backup=input("Inserisci il percorso di BackUp: ")
      if not os.path.isdir(self.scan): 
        print(f"Il percorso di scansione {self.scan} non è valido!")
        input()
        sys.exit()
      if not os.path.isdir(self.backup):
        print(f"Il percorso di BackUp {self.backup} non esiste! \nCreo cartella indicata...\n")
        os.makedirs(self.backup)
    except:
      print("Errore nell'inserimento dei dati richiesti!")
      input()
    else:
      print("I dati inseriti sono corretti!")
      input("\nPremi ENTER per iniziare...")
      self.copy()


if __name__ == "__main__":
  backup = BackUp()
  backup.start()
