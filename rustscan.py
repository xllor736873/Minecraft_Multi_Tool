import socket
import sys
import os
import time
from colorama import Fore, Back, Style

def port_scan(target):
    # Define a range of ports to scan
    ports = range(1, 65536)  # Scan ports 1 to 65535

    print(Fore.LIGHTRED_EX+f"{target} "+Fore.LIGHTBLUE_EX+"Sorgulanıyor"+Fore.LIGHTWHITE_EX+"... (uzun sürebilir, error olursa zaten terminale yazıyor)\n")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to 1 second for connection attempt

        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(Fore.LIGHTMAGENTA_EX+f"Port {port}: "+Fore.GREEN+"Açık!")
                time.sleep(10)
                os.system('clear')
                os.system('bash deneme.sh')
            sock.close()
        except socket.error as e:
            print(Fore.RED+f"An Error Occured: {e}")
            time.sleep(2)
            os.system('clear')
            os.system('bash deneme.sh')
        except socket.getaddrinfo:
            print(Fore.RED+"Domain vey IP Adresi Bulunamıyor!")
            time.sleep(2)
            os.system('clear')
            os.system('bash deneme.sh')

if __name__ == "__main__":
    target = input(""+Fore.LIGHTRED_EX+"IP Adresi "+Fore.LIGHTWHITE_EX+"veya "+Fore.LIGHTRED_EX+"Domain Adresi"+Fore.YELLOW+" Giriniz: "+Fore.LIGHTGREEN_EX)
    port_scan(target)
