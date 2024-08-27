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
    closure_start TIMESTAMP NOT NULL,
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

-- Stores user-generated reports of damage
CREATE TABLE NDR_user_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT NOT NULL, -- Main details
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    location VARCHAR(100) NOT NULL,
    status ENUM('Pending', 'Resolved') DEFAULT 'Pending'
);


-- The following is some imaginary table data to help demonstrate the functionality of the chatbot

-- Reset table data if needed
delete from NDR_alerts;
delete from NDR_road_closures;
delete from NDR_emergency_services;
delete from NDR_shelters;
delete from NDR_user_reports;