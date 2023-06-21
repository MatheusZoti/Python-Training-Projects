import os
import requests

url = input("Escreva a URL do site:\n")
wordlist = open("wordlist.txt")

for item in wordlist:
    item = item.strip()

    if "http://" not in url and "https://" not in url:
        subpage = f"https://{url}/{item}"
    else:
        if "/" not in url:
            subpage = f"{url}/{item}"
        else:
            subpage = f"{url}{item}"

    try:
        r = requests.get(subpage)
        if r.status_code == 200:
            print(f"A página '{subpage}' existe!\n")
            
    except:
        print(f"Ocorreu um erro ao conectar à página '{subpage}'\n")
        break
