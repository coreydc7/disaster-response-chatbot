<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset="UTF-8">
    <meta name="description" content="Frontend database controller for NDR Chatbot">
    <meta name="keywords" content="OpenAI, Python, PHP, API">
    <meta name="author" content="Corey Collins">
    <link href="style.css" rel="stylesheet">
    <script src="script.js"></script>
    <title>NDR Database Controller</title>
</head>

<body>
<div id="alert_interface">
    <div id="createAlert">
        <h2 class="title">Submit a new Alert</h2>
        <label for="alert_type">Enter the alert type (Flood, Fire, Earthquake, etc):</label>
        <input type="text" id="alert_type">
        <label for="alert_severity">Enter the severity (Low, Moderate, High, Critical):</label>
        <input type="text" id="alert_severity">
        <label for="alert_location">Enter the location (ex. Houston, TX)</label>
        <input type="text" id="alert_location">
        <label for="alert_description">Enter the alert description:</label>
        <textarea name="paragraph_text" id="alert_description" cols="50" rows="10"></textarea>
        <button onClick="createAlert()">Create Alert</button>
        <div id="createAlert_response"></div>
    </div>

    <div id="createClosure">
        <h2 class="title">Submit a new road closure</h2>
        <label for="closure_name">Enter the road name</label>
        <input type="text" id="closure_name">
        <label for="closure_location">Enter the location (ex. Los Angeles, CA)</label>
        <input type="text" id="closure_location">
        <label for="closure_time">Enter the expected reopen time (ex. 2024-08-18 17:00:00)</label>
        <input type="text" id="closure_time">
        <label for="closure_description">Enter the description:</label>
        <textarea name="paragraph_text" id="closure_description" cols="50" rows="10"></textarea>
        <button onClick="createClosure()">Create Closure</button>
        <div id="createClosure_response"></div>
    </div>

    <div id="addServices">
        <h2 class="title">Add new emergency services</h2>
        <label for="service_type">Enter the service type</label>
        <input type="text" id="service_type">
        <label for="service_location">Enter the location (ex. San Francisco, CA)</label>
        <input type="text" id="service_location">
        <label for="service_number">Enter the contact number</label>
        <input type="text" id="service_number">
        <button onClick="addService()">Add Service</button>
        <div id="addService_response"></div>
    </div>

    <div id="addShelter">
        <h2 class="title">Add new shelter service</h2>
        <label for="shelter_name">Enter the shelter name</label>
        <input type="text" id="shelter_name">
        <label for="shelter_address">Enter the address </label>
        <input type="text" id="shelter_address">
        <label for="shelter_capacity">Enter the max capacity</label>
        <input type="text" id="shelter_capacity">
        <label for="shelter_location">Enter the location (ex. San Francisco, CA)</label>
        <input type="text" id="shelter_location">
        <button onClick="addShelter()">Add Shelter</button>
        <div id="addShelter_response"></div>
    </div>
</div>

</body>
</html>