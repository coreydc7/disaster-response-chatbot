-- This file describes the Schema used for the Database that the GPT interacts with
CREATE DATABASE NDR_Chatbot;
USE NDR_Chatbot;

-- Reset tables if needed
DROP TABLE NDR_alerts;
DROP TABLE NDR_road_closures;
DROP TABLE NDR_emergency_services;
DROP TABLE NDR_shelters;
DROP TABLE NDR_user_reports;

-- Stores all alerts
CREATE TABLE NDR_alerts (
    alert_id INT PRIMARY KEY AUTO_INCREMENT,
    alert_type VARCHAR(50) NOT NULL, -- Flood, Earthquake, Hurricane
    alert_description TEXT NOT NULL, -- Main details
    severity ENUM('Low','Moderate','High','Critical') NOT NULL,
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);

-- Stores information about road closures 
CREATE TABLE NDR_road_closures (
    closure_id INT AUTO_INCREMENT PRIMARY KEY,
    road_name VARCHAR(100) NOT NULL,
    reason VARCHAR(100) NOT NULL, -- Flooding, debris, etc
    closure_start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expected_reopen TIMESTAMP,
    location VARCHAR(100) NOT NULL, -- City or region
    is_active BOOLEAN DEFAULT TRUE
);

-- Stores contact details for local emergency services
CREATE TABLE NDR_emergency_services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,
    service_type VARCHAR(50) NOT NULL, -- Fire, Medical, Police
    contact_number VARCHAR(15) NOT NULL,
    available BOOLEAN DEFAULT TRUE, -- Is the service operational?
    location VARCHAR(100) NOT NULL -- City or region served
);

-- Stores information about available shelters
CREATE TABLE NDR_shelters (
    shelter_id INT AUTO_INCREMENT PRIMARY KEY,
    shelter_name VARCHAR(100) NOT NULL,
    address TEXT NOT NULL,
    capacity INT NOT NULL, -- Max capacity
    current_occupancy INT DEFAULT 0,
    is_open BOOLEAN DEFAULT TRUE,
    location VARCHAR(100) NOT NULL
);

-- Stores user-generated reports 
CREATE TABLE NDR_user_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL, -- Main user-supplied details
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR(100) NOT NULL,
    status ENUM('Pending', 'Resolved') DEFAULT 'Pending'
);


-- Reset table data if needed
delete from NDR_alerts;
delete from NDR_road_closures;
delete from NDR_emergency_services;
delete from NDR_shelters;
delete from NDR_user_reports;

-- The following is some imaginary table data to help demonstrate the functionality of the chatbot
INSERT INTO NDR_alerts (alert_type, alert_description, severity, location, is_active)
VALUES
('Flood', 'Continued heavy rainfall and severe flooding in the downtown area. Residents are advised to not enter until further notice.', 'Critical', 'Miami, FL', TRUE),
('Earthquake', 'The 6.5 magnitude earthquake that struck near San Francisco has concluded, however Aftershocks are still ongoing. Continue to stay indoors and avoid damaged buildings.', 'High', 'San Francisco, CA', TRUE),
('Hurricane', 'Hurricane Emily is in full effect with winds over 130 mph. Mandatory evacuations are still in effect for coastal areas.', 'Critical', 'Miami, FL', TRUE),
('Wildfire', 'The wildfire is still spreading rapidly due to high winds. Evacuations are still in progress for residents in the affected area.', 'High', 'Los Angeles, CA', TRUE),
('Tornado', 'The tornado has concluded near Tulsa.', 'Low', 'Tulsa, OK', TRUE);

INSERT INTO NDR_road_closures (road_name, reason, closure_start, expected_reopen, location, is_active)
VALUES
('I-45 North Freeway', 'Flooding', '2024-08-01 14:30:00', '2024-08-03 08:00:00', 'Houston, TX', TRUE),
('Golden Gate Bridge', 'Structural damage due to earthquake', '2024-08-02 09:00:00', NULL, 'San Francisco, CA', TRUE),
('US-1', 'Debris from hurricane', '2024-08-10 16:00:00', '2024-08-12 10:00:00', 'Miami, FL', FALSE),
('Mulholland Drive', 'Wildfire', '2024-08-15 11:00:00', NULL, 'Los Angeles, CA', TRUE),
('Highway 169', 'Tornado damage', '2024-08-16 13:00:00', '2024-08-18 17:00:00', 'Tulsa, OK', FALSE);

INSERT INTO NDR_emergency_services (service_type, contact_number, available, location)
VALUES
('Fire Department', '555-1234', TRUE, 'Houston, TX'),
('Medical Services', '555-5678', TRUE, 'San Francisco, CA'),
('Police Department', '555-8765', TRUE, 'Miami, FL'),
('Search and Rescue', '555-4321', TRUE, 'Los Angeles, CA'),
('Emergency Operations Center', '555-1010', TRUE, 'Tulsa, OK');

INSERT INTO NDR_shelters (shelter_name, address, capacity, current_occupancy, is_open, location)
VALUES
('Downtown Community Center', '123 Main St, Houston, TX', 300, 250, TRUE, 'Houston, TX'),
('Bay Area Shelter', '456 Elm St, San Francisco, CA', 150, 120, TRUE, 'San Francisco, CA'),
('Coastal High School', '789 Ocean Dr, Miami, FL', 500, 450, TRUE, 'Miami, FL'),
('Northside Recreation Center', '1011 Maple Ave, Los Angeles, CA', 200, 180, TRUE, 'Los Angeles, CA'),
('Southside Church', '1213 Pine St, Tulsa, OK', 100, 80, TRUE, 'Tulsa, OK');

INSERT INTO NDR_user_reports (description, location)
VALUES
('Power lines down on Maple Street.', 'Houston, TX'),
('Unable to contact family member in the affected area.', 'San Francisco, CA'),
('Trapped in a flooded home, need immediate rescue.', 'Miami, FL'),
('House damaged by wildfire, requesting assistance.', 'Los Angeles, CA'),
('Tornado destroyed our home, need shelter.', 'Tulsa, OK');
