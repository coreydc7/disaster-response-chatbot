# GPT Implementation
This iteration of the NDR Chatbot utilizes a python script to connect with a fine-tuned GPT Project. These projects are managed using the OpenAI platform, and connected to using an API Key. Fine-tuning allows the chatbot to speak more directly, like a 911 dispatcher, while utilizing the functions available to it better.

As this is a technical demonstration, the chatbot will pull all its information about available shelters, alerts, road closures, user reports, nearby resources, etc. from a mock database whose schema is included. This is to demonstrate that the chatbot is able to perform API calls and work with real data from a live database, without needing to rely on real data. 

Currently, this chatbot is capable of:
1. Gathering the users GPS location and directing them to nearby shelter, whenever they express they are in danger. 
chatbot.py demonstrates the ability to detect intentions and utilize function calling to call specific functions based on what the user said. Currently this utilizes location permissions for the browser or mobile device to call an API to find shelters within a 5km radius of their GPS coordinates whenever the user expresses they are in danger or requests shelter directly.

2. Providing basic safety instructions and immediate first aid instruction for injuries like cuts, burns, fractures, or CPR, while still directing to connect with emergency services. Currently this uses the GPTs existing training, but could be combined with detecting intentions to give specific advice in specific situations.

3. Offering emotional support and being sympathetic. This could be expanded upon with detecting intentions to provide specific mental health resources and/or crisis counselors, however I'm not sure which services to recommend. 

------------------------------------------------------
How to use the chatbot:
1. Clone the repository
2. Create a .env file with the same fields as .env.example, and fill in the fields containing the database information, and API Key
3. run "python chatbot.py" in the GPT directory in order to start the chatbot

How to use the Frontend Database Controller:
1. After cloning the repository, create a new file "db_info.php" and update the database connection information, as seen in "db_info_example.php".
2. Run this command in the GPT directory to start the PHP server "php -S localhost:8000". PHP must be installed for this command to run.
3. Access the Frontend Controller at 'http://localhost:8000/controller.php'