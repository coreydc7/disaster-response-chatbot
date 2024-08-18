# Allows for sending multiple messages to GPT using user input
from openai import OpenAI

client = OpenAI()

def talk_to_gpt(user_input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a disaster response assistant."},
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0.7
    )
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