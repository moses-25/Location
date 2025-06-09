import phonenumbers
from phonenumbers import geocoder
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Sample prefix to county mapping for Kenya (you can expand this list)
prefix_to_county = {
    "254701": "Nairobi",
    "254702": "Mombasa",
    "254703": "Kisumu",
    "254704": "Nakuru",
    "254705": "Eldoret",
    "254707": "Thika",
    "254708": "Machakos",
    "254710": "Nairobi",
    "254711": "Nairobi",
    "254712": "Kisii",
    "254713": "Nyeri",
    "254714": "Meru",
    "254715": "Kakamega",
    "254717": "Kericho",
    "254718": "Embu",
    "254720": "Nairobi",
    "254722": "Mombasa",
    "254725": "Kisumu",
    "254728": "Nakuru",
    "254733": "Nairobi",
    "254734": "Mombasa",
    "254738": "Kisumu",
}

def get_county(phone_number_str):
    # Extract the first 6 digits after country code
    normalized = phone_number_str.replace("+", "").replace(" ", "")
    prefix = normalized[:6]  # e.g., "254715"
    return prefix_to_county.get(prefix, "Unknown County")

def print_location(phone_number_str):
    try:
        phone_number = phonenumbers.parse(phone_number_str)
        location = geocoder.description_for_number(phone_number, "en")
        county = get_county(phone_number_str)
        print(f"{Fore.YELLOW}[{phone_number_str}]{Style.RESET_ALL} ➤ Location: {Fore.CYAN}{location} | County: {Fore.GREEN}{county}")
    except phonenumbers.NumberParseException:
        print(f"{Fore.RED}Invalid phone number format: {phone_number_str}")

def main():
    print(f"{Fore.GREEN}{'='*50}")
    print(f"{Fore.MAGENTA}📍 Phone Number Location & County Tracker")
    print(f"{Fore.GREEN}{'='*50}{Style.RESET_ALL}")

    # Predefined phone numbers
    phone_numbers = [
        "+254754946327",
        "+254715458338",
        "+254717524008",
        "+254712458956"
    ]

    for num in phone_numbers:
        print_location(num)

    print(f"\n{Fore.BLUE}🔍 Check custom number location")
    user_input = input("Enter a phone number with country code (e.g. +2547XXXXXXX): ").strip()
    if user_input:
        print_location(user_input)

if __name__ == "__main__":
    main()