import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phoneck():
    while True:
        phonnum = input("[?] Number >")
        try:
            parsed_number = phonenumbers.parse(phonnum)
            
          
            country = geocoder.description_for_number(parsed_number, "en")
            
          
            operator = carrier.name_for_number(parsed_number, "en")
            
            
            time_zone = timezone.time_zones_for_number(parsed_number)
            
           
            print("[+] Phone Number Information:")
            print(f"- Country: {country}")
            print(f"- Operator: {operator}")
            print(f"- Time Zone(s): {', '.join(time_zone)}")
            
            choice = input("[?] Do you want to check another number? (y/n) ")
            if choice.lower() == "n":
                print("[*] Returning to main menu...")
                return
        except phonenumbers.phonenumber.NumberParseException:
            print("[!] Invalid phone number format. Please try again.")