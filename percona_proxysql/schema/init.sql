-- create database social_network
CREATE DATABASE IF NOT EXISTS social_network CHARACTER
SET utf8 COLLATE utf8_general_ci;
CREATE USER IF NOT EXISTS 'proxyuser' @'%' IDENTIFIED BY 's3cr3TL33tPr0xyP@ssw0rd';
GRANT ALL PRIVILEGES ON *.* To 'proxyuser' @'%';
FLUSH PRIVILEGES;