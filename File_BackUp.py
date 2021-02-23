import os
import shutil
import sys


class BackUp:

  def __init__(self):
    self.scelta = ""
    self.scan = ""
    self.backup = ""

  def create_tree(self, cartella):
    """
    ottengo le sottocartelle del percorso di scansione sottoforma di path
    """
    cartella_list = cartella.split("\\")
    scan_list = self.scan.split("\\")
    new_list = ""
    for el in cartella_list:
      if el not in scan_list:
        new_list += ("\\" + el)
    return new_list
    
  def copy(self):    
    try:
      for cartella, _, files in os.walk(self.scan):
        os.makedirs(self.backup + self.create_tree(cartella), exist_ok=True)
        for file in files:
          if self.scelta != "all":
            if file.endswith(self.scelta):
              shutil.copy(os.path.join(cartella,file), self.backup+self.create_tree(cartella))
          else:
            shutil.copy(os.path.join(cartella,file), self.backup+self.create_tree(cartella))
    except shutil.SameFileError as e:
      print(f"Errore nella copia dei file...{e}!\nUno o più file del percorso di scansione sono già presenti nella cartella di BackUp!\nRiprova selezionando 2 cartelle distinte!(Se i file sono nel Desktop,assicurati di metterli prima in una cartella!)")
    except:
      print("Errore nella copia dei file!")
    else:
      print("Copia dei file Terminato!")
      input()

  def start(self):
    try:
      self.scan=input("Inserisci il percorso di scansione: ")
      self.scelta = input("Vuoi fare il BackUp di tutti i file(all) o solo di una determinata estensione(es. jpg,exe,ecc..)?")
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
