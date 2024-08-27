from openai import OpenAI
import requests
import geocoder

# Establish connection with Project. Project API Key must be stored as an environment variable
client = OpenAI()

# Keeps a log of all messages between the user and GPT
messages = [{"role": "system", "content": "You are a disaster response assistant assisting people affected by Natural Disasters. Your goal is to provide quick and effective help, similar to a 911 dispatcher. You have many important jobs. The first is to give people safe evacuation instructions and direct them to the nearest shelter or relief centers when they are in danger. The second is to be sympathetic and offer emotional support. The third is to provide safety instructions for basic first aid for injuries like cuts, burns, fractures, or CPR, while always directing to connect with emergency services if needed."},]

def find_nearby_shelter():
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
    for entry in shelters:
        print(entry + '\n')

# Describes a function to GPT
function_descriptions = [
    {
    "name": "find_nearby_shelter",
    "description": "Returns a list of emergency shelters or relief centers near a users current location. Call this whenever a user expresses they are in danger, requests emergency shelter, or to be directed to the nearest relief center."
    }
]

def talk_to_gpt(user_input):
    messages.append({
                "role": "user",
                "content": user_input
            })
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        functions=function_descriptions,
        function_call="auto",
        temperature=0.7
    )
    
    ## check if GPT Response indicates that a function should be called.
    if(response.choices[0].message.function_call != None): 
        if(response.choices[0].message.function_call.name == 'find_nearby_shelter'):
            find_nearby_shelter()
    return response.choices[0].message.content

def main():
    print("This is the ### - Natural Disaster Response Chatbot")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Stay safe! Goodbye.")
            break
    
        response = talk_to_gpt(user_input)
        print(response)
        
if __name__ == "__main__":
    main()