#example
#python     project.py google.com yahoo.com

import os
import sys

def rodar_nmap():
  arg_urls = sys.argv[1:]
  
  for url in arg_urls:
    os.system(f"nmap {url}")
    print("\n -------------------------------------------------- \n")

rodar_nmap()