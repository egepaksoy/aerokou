from geopy.geocoders import Nominatim

# initialize Nominatim API 
geolocator = Nominatim(user_agent="Geopy Library")

# Latitude & Longitude input
Latitude = "40.712178"
Longitude = "30.025861"

location = geolocator.reverse(Latitude+","+Longitude)

# Display
print(location.raw["address"])
