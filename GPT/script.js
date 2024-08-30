function createAlert() {
    const type = document.getElementById('alert_type').value.trim();
    const severity = document.getElementById('alert_severity').value.trim();
    const location = document.getElementById('alert_location').value.trim();
    const description = document.getElementById('alert_description').value.trim();

    const alertData = {
        type: type,
        severity: severity,
        location: location,
        description: description
    };

    // Send a POST request using Fetch API
    fetch('api/createAlert.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // Convert JS object into a JSON string
        body: JSON.stringify(alertData)
    })
        .then(response => {
            if (!response.ok) {
                // Handle HTTP errors
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); // Parse JSON response
        })
        .then(data => {
            // Handle the response data
            handleCreateAlert(data);
        })
        // Handle any Fetch API errors
        .catch(error => console.error('Error:', error));
}

function handleCreateAlert(data) {
    var container = document.getElementById('createAlert_response');
    container.innerHTML = "";

    if(data.status == 'success') {
        container.innerHTML = "Successfully created Alert. Alert is now active.";
    } else {
        container.innerHTML = "Error creating alert.";
    }
    
}