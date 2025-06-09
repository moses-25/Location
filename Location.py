import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier

# Enter phone number with country code
number = input("Enter phone number with country code: ")

# Parsing string to phone number
phone_number = phonenumbers.parse(number)

# Printing the timezone using timezone module
time_zone = timezone.time_zones_for_number(phone_number)
print("TimeZone : " + str(time_zone))

# Printing the geolocation of the given phone number using geocoder module
geo_location = geocoder.description_for_number(phone_number, "en")
print("Location : " + geo_location)

# Printing the service provider using carrier module
service = carrier.name_for_number(phone_number, "en")
print("Service Provider : " + service)