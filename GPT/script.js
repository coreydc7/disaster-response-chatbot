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

function createClosure() {
    const name = document.getElementById('closure_name').value.trim();
    const location = document.getElementById('closure_location').value.trim();
    const time = document.getElementById('closure_time').value.trim();
    const description = document.getElementById('closure_description').value.trim();

    const closureData = {
        name: name,
        time: time,
        location: location,
        description: description
    };

    // Send a POST request using Fetch API
    fetch('api/createClosure.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // Convert JS object into a JSON string
        body: JSON.stringify(closureData)
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
            handleCreateClosure(data);
        })
        // Handle any Fetch API errors
        .catch(error => console.error('Error:', error));
}

function handleCreateClosure(data) {
    var container = document.getElementById('createClosure_response');
    container.innerHTML = "";

    if(data.status == 'success') {
        container.innerHTML = "Successfully created closure. Closure is now active.";
    } else {
        container.innerHTML = "Error creating closure.";
    }
}

function addService() {
    const type = document.getElementById('service_type').value.trim();
    const location = document.getElementById('service_location').value.trim();
    const number = document.getElementById('service_number').value.trim();

    const serviceData = {
        type: type,
        location: location,
        number: number
    };

    // Send a POST request using Fetch API
    fetch('api/addService.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // Convert JS object into a JSON string
        body: JSON.stringify(serviceData)
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
            handleAddService(data);
        })
        // Handle any Fetch API errors
        .catch(error => console.error('Error:', error));
}

function handleAddService(data) {
    var container = document.getElementById('addService_response');
    container.innerHTML = "";

    if(data.status == 'success') {
        container.innerHTML = "Successfully added service. Service is now active.";
    } else {
        container.innerHTML = "Error adding service.";
    }
}

function addShelter() {
    const name = document.getElementById('shelter_name').value.trim();
    const address = document.getElementById('shelter_address').value.trim();
    const capacity = document.getElementById('shelter_capacity').value.trim();
    const location = document.getElementById('shelter_location').value.trim();

    const shelterData = {
        name: name,
        location: location,
        address: address,
        capacity: capacity
    };

    // Send a POST request using Fetch API
    fetch('api/addShelter.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // Convert JS object into a JSON string
        body: JSON.stringify(shelterData)
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
            handleAddShelter(data);
        })
        // Handle any Fetch API errors
        .catch(error => console.error('Error:', error));
}

function handleAddShelter(data) {
    var container = document.getElementById('addShelter_response');
    container.innerHTML = "";

    if(data.status == 'success') {
        container.innerHTML = "Successfully added shelter. Shelter is now active.";
    } else {
        container.innerHTML = "Error adding Shelter.";
    }
}