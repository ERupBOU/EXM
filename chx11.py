import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def phonck():
    parsed_number = phonenumbers.parse(phone_number)

    region = geocoder.description_for_number(parsed_number, "en")
    operator = carrier.name_for_number(parsed_number, "en")
    time_zone = timezone.time_zones_for_number(parsed_number)

    return {
        "phone_number": phone_number,
        "region": region,
        "operator": operator,
        "time_zone": ", ".join(time_zone)
    }

# Example usage
phone_number = input("Enter a phone number in international format: ")
phone_number_info = get_phone_number_info(phone_number)

print(f"Phone number: {phone_number_info['phone_number']}")
print(f"Region: {phone_number_info['region']}")
print(f"Operator: {phone_number_info['operator']}")
print(f"Time zone: {phone_number_info['time_zone']}")