from ichp import ipck
from meet import metack
from chx11 import phoneck
from pasgen import passgen
import os
from colorama import Fore, Style

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

1. IP Checker [work]
2. Ports scan (ip checker)
3. Phone Checker [work]
4. Metadata img [work]
5. Bomber SMS [work]
6. Proxy Generator [ not work ]
7. Password Generator [work]
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
            ipck
        elif choice == 3:
            phoneck()
        elif choice == 4:
            metack()
        elif choice == 5:
            booom()
        elif choice == 6:
            print("error")
        elif choice == 7:
            passgen()
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
