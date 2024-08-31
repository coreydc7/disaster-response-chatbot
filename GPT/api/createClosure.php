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

$name = $data['name'];
$time = $data['time'];
$location = $data['location'];
$reason = $data['description'];

// Create SQL Prepared Statement
$response;
$sql = "INSERT INTO NDR_road_closures (road_name, reason, expected_reopen, location) VALUES ('$name', '$reason', '$time', '$location')";
if ($connection->query($sql) === true) {
    // Send response
    echo json_encode([
        'status' => 'success',
        'message' => "Success! Name: $name. Reason: $reason. Reopen: $time. Location: $location."
    ]);
} else {
    echo json_encode([
        'status' => 'failed',
        'message' => "Failed to create closure."
    ]);
}