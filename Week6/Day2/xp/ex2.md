SELECT * from customer;

SELECT (first_name, last_name) as full_name FROM customer;

SELECT create_date FROM customer GROUP BY create_date;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

SELECT address, district, phone FROM address WHERE district='Texas' 

SELECT * FROM film WHERE film_id=15 or film_id=150;

SELECT * FROM film WHERE title='Inglorious Basterds';

SELECT * FROM film WHERE title LIKE 'I% B%';

SELECT * FROM film ORDER BY rental_rate LIMIT 10;

SELECT * FROM film ORDER BY rental_rate LIMIT 10 OFFSET 10;


SELECT (customer.first_name, customer.last_name) as customer_name, payment.amount, payment.payment_date
FROM customer
INNER JOIN payment ON customer.customer_id=payment.customer_id
ORDER BY customer.customer_id;

SELECT title FROM film WHERE film_id not in (SELECT film_id FROM inventory);

SELECT city.city as city_name, country.country as country_name
FROM city
INNER JOIN country ON city.country_id=country.country_id;

