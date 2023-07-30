import phonenumbers
from phonenumbers import geocoder
from key import keys




number = input("Enter phone number with country code:")


check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number, " : ", number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print("Service provider : ",carrier.name_for_number(service_provider, "en"))


from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(keys)
query = str(number_location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
timezone = results[0]['annotations']['timezone']['name']
currency_name = results[0]['annotations']['currency']['name']
currency_symbol = results[0]['annotations']['currency']['symbol']
flag = results[0]['annotations']['flag']
print("Time-Zone : ",timezone)
print("Currency : ",currency_name)
print("Symbol : ",currency_symbol)
print("latitude: ",lat)
print("longitude: ",lng)


import folium
map_location = folium.Map(location = [lat,lng], zoom_start=8)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")

import webbrowser
# here insert the relative path of your mylocation.html file 
url = " realtive path " 
webbrowser.open_new(url)