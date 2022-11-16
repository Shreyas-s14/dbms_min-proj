-- Creating the database:
CREATE database dbms_mini_project;
-- Creating the tables:
CREATE TABLE student(
    roll_no int(10) NOT NULL,
    name varchar(50) NOT NULL,
    branch varchar(50) NOT NULL,
    year int(10) NOT NULL,
    PRIMARY KEY (roll_no)
);