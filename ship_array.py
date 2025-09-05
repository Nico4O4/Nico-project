import time

ships = ["idris", "890 Jump", "Polaris", "Javelin"]


the_ships = ships[0]
print("\nDein Schiff:", the_ships)


new_array = ships[1:]
new_array = " | ".join(map(str, new_array)) #Explanation: map(str, new_list) converts each number to a string and join() combines them into one string separated by "" what u put in there 
print("\nverbleibend:", new_array) # 1:(nichts) betrifft alle nach 0 (idris) im array / 1:7 z.b. alles von 1-6 (7 ausgeschlossen) im array


print("Exiting program...")
for TIMER in range(10, 0, -1):  # parameter: start, stop, step (step = wie zb -1 / +1 default ist +1)
        print(f" -> {TIMER} ", end="\r")    # \r = cariage return -> überschreibt aktuelle zeile / end="" das alles auf einenr zeile bleibt
        time.sleep(1)
        
        


#War eine Übung





