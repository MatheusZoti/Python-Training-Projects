import os
import requests

url = input("Escreva a URL do site, ex: google.com.br \n")
wordlist = open("wordlist.txt")

for item in wordlist:
  item = item.strip()
  subpage = f"https://{url}/{item}"
  r = requests.get(subpage)

  if r.status_code == 200:
    print(f"               A pagina '{url}/{item}' existe! \n")
  else:
    continue