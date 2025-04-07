import requests # um die anfrage zu senden
import re # um zu prüfen, ob die domain gültig ist

def valid_domain(domain): # funktion um zu prüfen, ob die domain gültig ist
    pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' # regex ist ein muster, das die domain überprüft wie z.b. google.com oder google.de 
    return re.match(pattern, domain) is not None # wenn die domain dem muster entspricht, gibt es true zurück. Ausserdem ist "is not None" eine Überprüfung, ob die domain nicht leer ist. ALso ob der Benutzer auch wirklich eine domain eingegeben oder irgendwas anderes eingegeben hat.


while True:
    name_domain = input("Enter a domain to ping: ").strip() #Get the domain from the user 

    if not valid_domain(name_domain): # prüft mithilfe von der funktion valid_domain, ob die domain gültig ist
        print("Invalid domain format. Please enter a valid domain.") # gibt eine Fehlermeldung aus, wenn die domain ungültig ist
        continue # geht zurück zum anfang der schleife

    url = f"https://{name_domain}" # erstellt die url mit dem protokoll https:// und der domain, die der benutzer eingegeben hat aber nur wenn die domain gültig ist


    for i in range(5): # pingt die domain 5 mal
        try: 

            response = requests.get(url) # sendet eine GET-Anfrage an die URL

            if response.status_code == 200: # wenn die antwort 200 ist, gibt es eine erfolgreiche antwort zurück
                print(f"[{i+1}] 200") # printed die antwort 200
            else:
                print(f"[{i+1}] ({name_domain}) Status: {response.status_code}") # ansonsten gibt es den status code zurück, wenn die antwort nicht 200 ist beispiel 404, 500, 403 etc.
    

        except requests.exceptions.RequestException as f: 3 # wenn die anfrage fehlschlägt, gibt es eine fehlermeldung zurück
        print(f"[{i+1}] ({name_domain}) ungültig oder nicht erreichbar.") # gibt eine fehlermeldung zurück, wenn die domain ungültltig geschrieben ist oder nicht erreichbar ist

    break # Break the loop after 5 pings

# a programm that pings google.com 5 times and prints the status code of the response.
# If the request fails, it prints the error message.

#made by @NICO4O4 

