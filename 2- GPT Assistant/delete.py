# import geocoder

# def get_gps_location():
#     g = geocoder.ip('me')
#     return g.latlng

# location = get_gps_location()
# print(f"GPS Location: {location[0]}, {location[1]}")
# print(type(location[0]))

# %%
# messages = [{"role": "system", "content": "You are a disaster response assistant."},]
# messages.append(
#             {
#                 "role": "user",
#                 "content": "asdf"
#             }
#         )

# %%
import geocoder
import requests

location = geocoder.ip('me').latlng
latitude = location[0]
longitude = location[1]

# Overpass API endpoint with a 5km radius around the coordinates
url = "https://overpass-api.de/api/interpreter"
# Overpass QL query to find shelters within 5km radius of the given location
query = f"""
[out:json];
node
[amenity=shelter](around:5000,{latitude},{longitude});
out body;
"""

# Making the request to the Overpass API
response = requests.get(url, params={'data': query})
data = response.json()
shelters = []
for element in data['elements']:
    if 'tags' in element:
        name = element['tags'].get('amenity')
        lat = element['lat']
        lon = element['lon']
        
        shelters.append(f"Amenity Type: {name}\nLocation: {lat}, {lon}\n")
print(shelters)
# %%
