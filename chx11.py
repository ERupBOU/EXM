import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phonck(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return {"error": f"Invalid phone number format: {phone_number}"}

    try:
        region = geocoder.description_for_number(parsed_number, "en")
        operator = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
    except (phonenumbers.phonenumberutil.NumberParseException, IndexError):
        return {"error": f"Failed to retrieve information for phone number: {phone_number}"}

    return {
        "phone_number": phone_number,
        "region": region,
        "operator": operator,
        "time_zones": ", ".join(time_zones)
    }

def main_menu():
    while True:
        print("Choose an action:")
        print("1. Get phone number information")
        print("2. Return to main menu")
        print("3. Exit")

        choice = input("Enter the number of your choice (1-3): ")

        if choice == "1":
            phone_number = input("Enter a phone number in international format: ")
            phone_number_info = get_phone_info(phone_number)
            if "error" in phone_number_info:
                print(phone_number_info["error"])
            else:
                print(f"Phone number: {phone_number_info['phone_number']}")
                print(f"Region: {phone_number_info['region']}")
                print(f"Operator: {phone_number_info['operator']}")
                print(f"Time zones: {phone_number_info['time_zones']}")
        elif choice == "2":
            continue
        elif choice == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()