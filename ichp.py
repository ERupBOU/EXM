import socket
import ipaddress

def ipck():
    while True:
        try:
            ipadr = input("[?] ip > ")
            
            ip_info = ipaddress.ip_address(ipadr)
            print(f"[+] IP Address: {ip_info.compressed}")
            print(f"[+] IP Version: {ip_info.version}")
            print(f"[+] IP Type: {ip_info.is_private}")
           
            try:
                hostname = socket.gethostbyaddr(ipadr)[0]
                print(f"[+] Hostname: {hostname}")
            except socket.herror:
                print("[-] Unable to resolve hostname")
           
            try:
                port = int(input("[?] Port (Press Enter to skip) > ") or "0")
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                result = sock.connect_ex((ipadr, port))
                if result == 0:
                    print(f"[+] Port {port} is open")
                else:
                    print(f"[-] Port {port} is closed")
                sock.close()
            except ValueError:
                print("[-] Invalid port number")
        except ValueError:
            print("[-] Invalid IP address")
        except KeyboardInterrupt:
            print("\n[!] Exiting...")
            break
        
        choice = input("[?] Do you want to check another IP? (y/n) ")
        if choice.lower() == "n":
            print("[*] Returning to main menu...")
            return

if __name__ == "__main__":
    ipck()