import requests

for i in range(5):
    try:
        response = requests.get("http://www.google.com") #change the URL you want to ping

        if response.status_code == 200:
            print(f"[{i+1}] 200")
    
    except requests.exceptions.RequestException as f:
        # if the request fails, print the error message
        print(f"[{i+1}] Error: {f}")

# a programm that pings google.com 5 times and prints the status code of the response.
# If the request fails, it prints the error message.

#made by @NICO4O4 