# Print
# print(4+1)

#  Variablen
#a  = 3
#b = 7
#print(a+b)

# Mit Benutzer Eingabe + Variable

# zahl = int(input("Gib eine Zahl ein: "))
# print("Deine Zahl * 4 ist:", zahl * 4)

# Auswählen zwischen + und -

while True: 
    try:
        rechner = int(input("1 = Addieren | 2 = Subtrahieren | 3 = Multipliezieren | 4 = Dividieren: "))
    except ValueError:
        print("Fehler: Bitte Zahl von 1-4 eigenben")
        continue #Geht zurück zum Anfang der Schleife

    if rechner == 1:
        print("Du hast + gewählt")
        zahl1 = int(input("Bitte gib die erste Zahl ein: "))
        zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        print("Das Ergebnis ist:", zahl1 + zahl2)

    if rechner == 2:
        print("Du hast - gewählt")
        zahl1 = int(input("Bitte gib die erste Zahl ein: "))
        zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        print("Das Ergebnis ist:", zahl1 - zahl2)

    if rechner == 3:
        print("Du hast * gewählt")
        zahl1 = int(input("Bitte gib die erste Zahl ein: "))
        zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        print("Das Ergebnis ist", zahl1 * zahl2 )

    if rechner == 4:
        print("Du hast / gewählt")
        zahl1 = int(input("Bitte gib die erste Zahl ein: "))
        zahl2 = int(input("Bitte gib die zweite Zahl ein: "))
        print("Das Ergebnis ist", zahl1 / zahl2 )

    print("Berechnung abgeschlossen was jetzt?")
    option = input("Neue Berechnung starten? [Y/N]: ").strip().upper()
    if option == "Y":
        print("Neustart...")
    
    elif option == "N":
        print("Programm beendet")
        exit() #Beendet das Programm

    else:
        print("Fehler: Bitte gib Y/y für eine neue Berechnung ein oder N/n zum beenden")

    # Work in progress ...