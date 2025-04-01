import os

def clear_console():
    # Überprüft welches Betriebssystem benutzt wird
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Unix oder MacOS
        os.system("clear") 


history = [] # Liste für den Verlauf

def addieren(zahl1, zahl2): # Die Funktioon braucht 2 Zahlen die in der variable zahl1 und zahl2 gespeichert werden
    ergebnis = zahl1 + zahl2 # Die beiden Zahlen werden addiert und in der Variable ergebnis gespeichert
    history.append(f"{zahl1} + {zahl2} = {ergebnis}") # Der Verlauf wird in die Liste gespeichert
    return ergebnis # Das Ergebnis wird zurückgegeben 

def subtrahieren(zahl1, zahl2):
    ergebnis = zahl1 - zahl2
    history.append(f"{zahl1} - {zahl2} = {ergebnis}")
    return ergebnis 

def multiplizieren(zahl1, zahl2):
    ergebnis = zahl1 * zahl2
    history.append(f"{zahl1} * {zahl2} = {ergebnis}")
    return ergebnis

def dividieren(zahl1, zahl2):
    ergebnis = zahl1 / zahl2
    history.append(f"{zahl1} / {zahl2} = {ergebnis}")
    return ergebnis


while True: 
    try:
        rechner = (input(" | 1 = Addieren | 2 = Subtrahieren | 3 = Multipliezieren | 4 = Dividieren | Verlauf | Beenden | Clear | ")).strip().lower()
    except ValueError:
        print("Fehler: Bitte Zahl von 1-4 eingeben. ")
        continue #Geht zurück zum Anfang der Schleife

    if rechner == "1":
        print("Du hast + gewählt")
        try:
            zahl1 = int(input("Bitte gib die erste Zahl ein: "))
            zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        except ValueError:
            print("Fehler: Bitte nur Zahlen eingeben. ")
            continue
        print("Das Ergebnis ist:", addieren(zahl1, zahl2))
    
    elif rechner == "2":
        print("Du hast - gewählt")
        try:
            zahl1 = int(input("Bitte gib die erste Zahl ein: "))
            zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        except ValueError:
            print("Fehler: Bitte nur Zahlen eingeben. ")
            continue
        print("Das Ergebnis ist:", subtrahieren(zahl1, zahl2))
        

    elif rechner == "3":
        print("Du hast * gewählt")
        try:
            zahl1 = int(input("Bitte gib die erste Zahl ein: "))
            zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        except ValueError:
            print("Fehler: Bitte nur Zahlen eingeben. ")
            continue  
        print("Das Ergebnis ist", multiplizieren(zahl1, zahl2))
     

    elif rechner == "4":
        print("Du hast / gewählt")
        try:
            zahl1 = int(input("Bitte gib die erste Zahl ein: "))
            zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        except ValueError:
            print("Fehler: Bitte nur Zahlen eingeben. ")
            continue
        print("Das Ergebnis ist", dividieren(zahl1, zahl2))
       

    elif rechner == "verlauf":
        if history:
            print("Letze Berechnungen seit dem letzen Start des Programm: ")
            for eintrag in history:
                print(eintrag)
            continue

        else: 
            print("Keine Berechnungen im Verlauf gefunden")
            continue # Geht zurück zum Anfang der 1. Schleife

    elif rechner == "beenden":
        print("Programm beendet")
        exit()

    elif rechner == "clear":
        clear_console()
        continue # Geht zurück zum Anfang der 1. Schleife

    else:
        print("Fehler: Bitte gib eine Zahl von 1-4 ein oder Verlauf / Beenden.")
        continue # Geht zurück zum Anfang der 1. Schleife

    while True:
        option = input("Zur Hauptauswahl zurück kehren? [Y/N]: ").strip().upper()
    
        if option == "Y":
            clear_console()
            break # Bricht die Y/N Schleife ab und geht zurück zur ersten Schleife
            

        elif option == "N":
            print("Programm beendet")
            exit() #Beendet das Programm

        else:
            print("Fehler: Bitte gib Y/y für eine neue Berechnung ein oder N/n zum beenden")

    # WIP ...
    # Calculator - coded by: Nico4O4