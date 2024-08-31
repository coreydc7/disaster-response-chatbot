<?php
include "db_info.php";

$connection = new mysqli($serverName, $userName, $password, $database);

if ($connection->connect_error) {
    die("Connection failed: " . $connection->connect_error);
}

$json = file_get_contents('php://input');
$data = json_decode($json, true); # Stores POST values in an associative array

// Check if the JSON is valid
if (json_last_error() !== JSON_ERROR_NONE) {
    // Handle invalid JSON
    http_response_code(400);
    echo json_encode(['error' => 'Invalid JSON payload']);
    exit;
}

$type = $data['type'];
$location = $data['location'];
$number = $data['number'];

// Create SQL Prepared Statement
$response;
$sql = "INSERT INTO NDR_emergency_services (service_type, contact_number, location) VALUES ('$type', '$number', '$location')";
if ($connection->query($sql) === true) {
    // Send response
    echo json_encode([
        'status' => 'success',
        'message' => "Success! Type: $type. Number: $number. Location: $location."
    ]);
} else {
    echo json_encode([
        'status' => 'failed',
        'message' => "Failed to add service."
    ]);
}