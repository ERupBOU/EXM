from ichp import ipck
from meed import metack
from chx11 import phoneck
from smbe import booom
from proxy_scraper import get_proxies
from usserc import userck
import os
from colorama import Fore, Style
from setingsc import cfgsck

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
key = "krnl32"

print(Fore.MAGENTA + Style.BRIGHT + """
 __          __                 
/\  _\    /\ \ /\ \     /'\_/\    
\ \ \L\_\  \ \\/'/'   /\      \   
 \ \  _\L   \/ > <     \ \ \__\ \  
  \ \ \L\ \    \/'/\\   \ \ \_/\ \ 
   \ \____/    /\_\\ \_\  \ \_\\ \_\
                               \/___/     \/_/ \/_/   \/_/ \/_/
    
""" + Style.RESET_ALL)

uskey = input("(?) key >")
if uskey == key:
    print("Wait...")

def set_logo():
    logo ='''
      __          __                 
/\  _\    /\ \ /\ \     /'\_/\    
\ \ \L\_\  \ \\/'/'   /\      \   
 \ \  _\L   \/ > <     \ \ \__\ \  
  \ \ \L\ \    \/'/\\   \ \ \_/\ \ 
   \ \____/    /\_\\ \_\  \ \_\\ \_\
                               \/___/     \/_/ \/_/   \/_/ \/_/
'''
    print(Fore.MAGENTA + Style.BRIGHT + logo + Style.RESET_ALL)

def menu_input():
    clear_console()
    set_logo()
    print('''

       > EXMMobile <

1. IP Checker
2. Ports scan
3. Phone Checker
4. Metadata img
5. Bomber SMS
6. Proxy Generator
7. Password Generator
8. Settings
''')

def main_menu():
    while True:
        menu_input()
        try:
            choice = int(input(Fore.GREEN + "[?] Choice : " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Error: Invalid input. Please enter a number." + Style.RESET_ALL)
            clear_console()
            continue

        if choice == 1:
            ipck()
        elif choice == 2:
            pscan()
        elif choice == 3:
            phoneck()
        elif choice == 4:
            metack()
        elif choice == 5:
            booom()
        elif choice == 6:
proxy_list = get_proxies()
for proxy in proxy_list:
    print(proxy)
        elif choice == 7:
            userck()
        elif choice == 8:
            cfgsck()
        elif choice == 99:
            clear_console()
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            sys.exit()
        else:
            print(Fore.RED + "Error: Invalid choice. Please try again." + Style.RESET_ALL)
            clear_console()

if __name__ == "__main__":
    clear_console()
    main_menu()
