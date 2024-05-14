CREATE DATABASE IF NOT EXISTS safelinkdb;
USE safelinkdb;

CREATE TABLE IF NOT EXISTS policeOff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nameOfficer VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    passwordOfficer VARBINARY(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS prisoners (
    id INT PRIMARY KEY AUTO_INCREMENT,
    namePrisoner VARCHAR(255) NOT NULL,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8)
);

CREATE TABLE IF NOT EXISTS logs (
    id INT NOT NULL AUTO_INCREMENT,
    latitude DECIMAL(8, 2) NOT NULL,
    longitude DECIMAL(8, 2) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES prisoners(id)
);

INSERT INTO policeOff (name, email, passwordOfficer) VALUES 
    ('3am Rchayd', 'rchid15@police.tn', 'salmabenti'),
    ('3ammar', 'USA.3ammar@police.tn', 'salmamarti'),
    ('rjab', 'elba7ath@police.tn', 'chapati123'),
    ('saif', 'minion@police.tn', 'hayfa');

INSERT INTO prisoners (latitude, longitude, namePrisoner) VALUES 
    (37.77490000, -122.41940000, 'el jaghali'),
    (40.71280000, -74.00600000, 'shi9 mi9 fetri9'),
    (34.05220000, -118.24370000, 'el shama9ma9'),
    (37.77490000, -122.41940000, 'hmed satour'),
    (40.71280000, -74.00600000, 'el 3ou9'),
    (34.05220000, -118.24370000, 'bringa'),
    (37.77490000, -122.41940000, 'layka'),
    (40.71280000, -74.00600000, 'spisiron'),
    (34.05220000, -118.24370000, 'weld monjia'),
    (37.77490000, -122.41940000, 'el mokh tar'),
    (40.71280000, -74.00600000, 'siid jinyor'),
    (34.05220000, -118.24370000, 'siid l kbir');
