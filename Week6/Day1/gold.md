CREATE DATABASE bootcamp;

CREATE TABLE students(
 id SERIAL PRIMARY KEY,
 last_name VARCHAR (50) NOT NULL,
 first_name VARCHAR (50) NOT NULL,
 dob DATE NOTNULL

)

INSERT INTO students(first_name, last_name, dob)
VALUES ('Marc', 'Benichou', '1998-11-02');
VALUES ('Yoan', 'Cohen', '2010-12-03');
VALUES ('Lea', 'Benichou', '1987-07-27');
VALUES ('Amelia', 'Dux', '1996-04-07');
VALUES ('David', 'Grez', '2003-06-14');
VALUES ('Omer', 'Simpson', '1980-10-03');

SELECT * from students
SELECT first_name, last_name from student
SELECT first_name, last_name from students where id = 2
SELECT first_name, last_name from students where first_name = 'Marc' and last_name = 'Benichou'
SELECT first_name, last_name from students where first_name = 'Marc' or last_name = 'Benichou'

SELECT first_name FROM students WHERE first_name LIKE '%a%'
SELECT first_name FROM students WHERE first_name LIKE 'A%'
SELECT first_name FROM students WHERE first_name LIKE '%a'
SELECT first_name FROM students WHERE first_name LIKE '%a_'

SELECT first_name, last_name from students where id = 2 and id = 3

SELECT first_name, last_name, dob from students where dob >= '2000-01-01'

SELECT * from students ORDER BY dob DESC LIMIT 1
SELECT * from students LIMIT 3 OFFSET 2