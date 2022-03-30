import phonenumbers
from phonenumbers import geocoder, carrier

number = "+51929202772"
ch_nmber = phonenumbers.parse(number, 'CH')
service_nmber = phonenumbers.parse(number, 'RO')

print(geocoder.description_for_number(ch_nmber, "en"))
print(carrier.name_for_number(service_nmber, "en"))