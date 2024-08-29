from openai import OpenAI
import mysql.connector
from mysql.connector import Error
import json
import os
from dotenv import load_dotenv


# Establish connection with GPT Project. Project API Key must be stored as an environment variable
client = OpenAI()

# Keeps a log of all messages between the user and GPT
messages = [{"role": "system", "content": "You are a disaster response assistant assisting people affected by Natural Disasters. Your goal is to provide quick and effective help, similar to a 911 dispatcher. You have many important jobs. The first is to give people safe evacuation instructions and direct them to the nearest shelter or relief centers when they are in danger. The second is to be sympathetic and offer emotional support. The third is to provide safety instructions for basic first aid for injuries like cuts, burns, fractures, or CPR, while always directing to connect with emergency services if needed."},]

# Load environment variables
BASEDIR = os.path.abspath(os.path.dirname(__file__)) # Finds current directory
load_dotenv(os.path.join(BASEDIR, '.env'))

## Establishes a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

## Start of GPT Functions
# Finds open shelters for a given location
def find_nearby_shelter(location):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT * FROM NDR_shelters
        WHERE location LIKE %s
        AND is_open = TRUE
        AND current_occupancy < capacity;
        """
        cursor.execute(query, (f"%{location}%",))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        # Output results
        print(f"Displaying all local shelters closures for: {location} \n")
        for entry in results:
            print(f"Location: {entry['location']} \n Address: {entry['address']} \n Shelter_name: {entry['shelter_name']} Max capacity: {entry['capacity']} \n Current occupancy: {entry['current_occupancy']} \n")
    return []

# Finds all active alerts for a given location
def get_active_alerts(location):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT * FROM NDR_alerts
        WHERE location LIKE %s AND is_active = TRUE
        """
        cursor.execute(query, (f"%{location}%",))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        # Output results
        print(f"Displaying all emergency alerts for: {location} \n")
        for entry in results:
            print(f"Location: {entry['location']} \n Severity: {entry['severity']} \n Issued at: {entry['issued_at']} \n Type: {entry['alert_type']} \n Description: {entry['alert_description']} \n")
    return []

def get_active_road_closures(location):
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT * FROM NDR_road_closures 
        WHERE location LIKE %s AND is_active = TRUE
        """
        cursor.execute(query, (f"%{location}%",))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        
        # Output results
        print(f"Displaying all road closures for: {location} \n")
        for entry in results:
            print(f"Location: {entry['location']} \n Road name: {entry['road_name']} \n Closure start: {entry['closure_start']} \n Expected reopen: {entry['expected_reopen']} \n Reason: {entry['reason']} \n")
    return []

## Describes the functions to GPT
tools = [
    {
        "type": "function",
        "function": {
            "name": "find_nearby_shelter",
            "description": "Dispkays a list of emergency shelters or relief centers for a particular location. Call this whenever a user expresses they are in danger, requests emergency shelter, or to be directed to the nearest relief center.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location of a user. This must be either the name of a city, or a two-letter state code.",
                    },
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_active_alerts",
            "description": "Get any active emergency alerts for a particular location. Call this whenever a user asks for any active alerts or updates on a particular natural disaster affecting a certain location.",        
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location of a user. This must be either the name of a city, or a two-letter state code.",
                    },
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        }
    },
    {
        "type" : "function",
        "function": {
            "name": "get_active_road_closures",
            "description": "Get any active road closures for a particular location. Call this whenever a user asks for the status of roads, road closures, or any updates on the road conditions for a particular location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location of a user. This must be either the name of a city, or a two-letter state code.",
                    },
                },
                "required": ["location"],
                "additionalProperties": False,
            },
        }
    }
]

## Main function to handle conversation with GPT and appending messages to history
def talk_to_gpt(user_input):
    messages.append({
                "role": "user",
                "content": user_input
            })
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools
    )
    
    ## check if GPT Response indicates that a function should be called and call it.
    if(response.choices[0].message.tool_calls != None): 
        if(response.choices[0].message.tool_calls[0].function.name == 'find_nearby_shelter'):
            tool_call = response.choices[0].message.tool_calls[0]
            arguments_json = tool_call.function.arguments # Extract the arguments from GPT response object
            arguments = json.loads(arguments_json)
            
            location = arguments.get('location')
            find_nearby_shelter(location) # Call the function with the extracted location
        if(response.choices[0].message.tool_calls[0].function.name == 'get_active_alerts'):
            tool_call = response.choices[0].message.tool_calls[0]
            arguments_json = tool_call.function.arguments
            arguments = json.loads(arguments_json)
                        
            location = arguments.get('location')
            get_active_alerts(location)
        if(response.choices[0].message.tool_calls[0].function.name == 'get_active_road_closures'):
            tool_call = response.choices[0].message.tool_calls[0]
            arguments_json = tool_call.function.arguments
            arguments = json.loads(arguments_json)
            
            location = arguments.get('location')
            get_active_road_closures(location)
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
        if(response != None): # Only print message content if it exists, as other output may come from function calls
            print(response)
        
if __name__ == "__main__":
    main()