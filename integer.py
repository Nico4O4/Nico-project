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
    rechner = int(input("Gib 1 für + und 2 für - ein: "))

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

    print("Berechnung abgeschlossen was jetzt?")
    option = input("Neue Berechnung starten? [Y/N]: ")
    
    if option == "N":
        print("Programm beendet")
        exit()