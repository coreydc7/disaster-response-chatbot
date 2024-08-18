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
location = geocoder.ip('me').latlng
latitude = location[0]
longitude = location[1]
# %%
