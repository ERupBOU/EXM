import socket
import ipaddress

def ipck():
    try:
        ip_address = ipaddress.ip_address(ip_or_domain)
        ip_address = str(ip_address)
    except ValueError:
        try:
            ip_address = socket.gethostbyname(ip_or_domain)
        except socket.gaierror:
            return {"error": f"Failed to determine IP address from '{ip_or_domain}'"}
    
    try:
        hostname, aliases, addresses = socket.gethostbyaddr(ip_address)
        return {
            "ip": ip_address,
            "hostname": hostname,
            "aliases": aliases,
            "addresses": addresses
        }
    except socket.herror:
        return {"error": f"Failed to get information for IP address '{ip_address}'"}

def main():
    while True:
        print("\nChoose an action:")
        print("1. Get IP address information")
        print("2. Exit")

        choice = input("[?] Enter the number of the action: ")

        if choice == "1":
            ip_or_domain = input("Enter an IP address or domain name: ")
            ip_info = get_ip_info(ip_or_domain)
            if "error" in ip_info:
                print(ip_info["error"])
            else:
                print(f"IP Address: {ip_info['ip']}")
                print(f"Hostname: {ip_info['hostname']}")
                print(f"Aliases: {', '.join(ip_info['aliases'])}")
                print(f"Addresses: {', '.join(ip_info['addresses'])}")
        elif choice == "2":
            print("...")
            return
        else:
            print("Invalid choice. Please try again.")
