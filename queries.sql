CREATE DATABASE fut;

USE fut;

CREATE TABLE player(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    club VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    postion CHAR(2) NOT NULL,
    nationality VARCHAR(100) NOT NULL,
    starting_player CHAR(1) NOT NULL
);

CREATE TABLE stats(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    season CHAR(4),
    goals INT,
    assists INT,
    id_player INT,
    FOREIGN KEY(id_player)
        REFERENCES player(id)
);