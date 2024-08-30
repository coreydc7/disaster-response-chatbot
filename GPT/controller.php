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
        <h2 class="title">Create a new Alert</h2>
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
</div>

</body>
</html>