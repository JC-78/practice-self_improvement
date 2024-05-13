#pip3 install phonenumbers
import phonenumbers
from phonenumbers import geocoder
from test import number

#CH=Country History
ch_num=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_num,"en"))
