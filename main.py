import phonenumbers
import opencage
import folium
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


mynumber = phonenumbers.parse(number)
location = geocoder.description_for_number(mynumber, "en")
print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

key = "511be5f37f0a4d798c93ecb0091d8f59"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]["geometry"]["lat"]
lng = results[0]["geometry"]["lng"]

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup =location).add_to(myMap)

myMap.save("myloaction.html")

