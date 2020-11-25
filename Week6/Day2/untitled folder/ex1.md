SELECT count(*) FROM film WHERE rating = 'G' or rating = 'PG-13';

SELECT rating, count(*) FROM film GROUP BY rating

SELECT * FROM film WHERE rating='G' or rating='PG-13'


UPDATE customer
SET first_name = 'Michael', last_name = 'Nemni', email='michael.nemni@gmail.com', create_date='2020-11-23'
WHERE customer_id = 1


ex2

UPDATE students
SET dob='1998-11-02'
WHERE last_name='Benichou'

UPDATE students
SET last_name='Guez'
WHERE last_name='Grez'

DELETE FROM students WHERE first_name = 'Lea' and last_name = 'Benichou'

SELECT count(*) FROM students

SELECT count(*) FROM students WHERE dob>'1/01/2000'

ALTER students
ADD math_grad SMALLINT;

UPDATE students
SET math_grade = 80
WHERE id=1;

SELECT count(*) FROM students WHERE math_grade>83;

INSERT INTO students(first_name, last_name, dob, math_grade)
VALUES('Omer', 'Simpson', '1980-10-03', 70);

SELECT SUM(math_grade)
FROM students;

SELECT first_name, last_name from customers ORDER BY first_name LIMIT 2;
