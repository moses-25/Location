import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

print(f"{Fore.CYAN}{'📱 Phone Number Info Tool':^50}")
print(f"{Fore.YELLOW}{'-'*50}")

# Input from user
number = input(f"{Fore.GREEN}Enter phone number with country code (e.g. +2547...): ")

try:
    phone_number = phonenumbers.parse(number)

    # Check if the number is valid
    if not phonenumbers.is_valid_number(phone_number):
        print(f"{Fore.RED}❌ Invalid phone number!")
    else:
        # Time zone(s)
        time_zone = timezone.time_zones_for_number(phone_number)
        print(f"{Fore.MAGENTA}🕒 TimeZone: {Style.BRIGHT}{', '.join(time_zone)}")

        # Location
        geo_location = geocoder.description_for_number(phone_number, "en")
        print(f"{Fore.BLUE}📍 Location: {Style.BRIGHT}{geo_location}")

        # Carrier
        service = carrier.name_for_number(phone_number, "en")
        print(f"{Fore.YELLOW}📶 Service Provider: {Style.BRIGHT}{service if service else 'Unknown'}")

except phonenumbers.NumberParseException:
    print(f"{Fore.RED}❌ Error: Couldn't parse the phone number. Please enter a valid one.")