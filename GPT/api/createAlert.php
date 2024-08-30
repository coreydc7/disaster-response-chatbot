<?php
    include "db_info.php";

    $connection = new mysqli($serverName, $userName, $password, $database);

    if ($connection -> connect_error) {
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
    $severity = $data['severity'];
    $location = $data['location'];
    $description = $data['description'];

    // Create SQL Prepared Statement
    $response;
    $sql = "INSERT INTO NDR_alerts (alert_type, alert_description, severity, location) VALUES ('$type', '$description', '$severity', '$location')";
    if ($connection->query($sql) === true) {
        // Send response
        echo json_encode([
            'status' => 'success',
            'message' => "Success! Type: $type. Severity: $severity. Location: $location. Description: $description."
        ]);
    } else {
        echo json_encode([
            'status' => 'failed',
            'message' => "Failed to create alert."
        ]);
    }

    