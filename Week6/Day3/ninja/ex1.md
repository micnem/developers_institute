SELECT film.title, film.rental_rate, customer.first_name, customer.last_name
FROM rental
INNER JOIN customer
ON customer.customer_id = rental.customer_id
INNER JOIN inventory
ON inventory.inventory_id = rental.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE return_date is NULL


