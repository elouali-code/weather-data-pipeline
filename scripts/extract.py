import requests
import json
import os

cities = ["Paris", "Geneva", "Annecy", "Lyon", "Marseille"]

os.makedirs("../raw", exist_ok=True)

for city in cities:
    url = f"https://wttr.in/{city}?format=j1"
    
    response = requests.get(url)
    data = response.json()
    
    with open(f"../raw/{city.lower()}.json", "w") as f:
        json.dump(data, f, indent=2)

print("Extraction terminée ")