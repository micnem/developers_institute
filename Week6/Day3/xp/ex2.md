UPDATE film
SET language_id = 2
WHERE film_id<200

SELECT * FROM actor WHERE first_name = 'Penelope' and last_name = 'Monroe'

actor_id = 120

SELECT actor.first_name, actor.last_name, film.title
FROM actor 
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film_actor.film_id = film.film_id

SELECT COUNT(*) FROM rental
WHERE return_date is NULL

187 

SELECT *, film.title, film.rental_rate
FROM rental
INNER JOIN inventory
ON inventory.inventory_id = rental.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE return_date is NULL
ORDER BY rental_rate
LIMIT 30




SELECT actor.first_name, actor.last_name, film.title, film.description
FROM actor 
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film_actor.film_id = film.film_id
WHERE actor.first_name = 'Penelope' and actor.last_name = 'Monroe' and film.description LIKE '%Sumo%'

Park Citizen

SELECT actor.first_name, actor.last_name, film.title, category.name
FROM actor 
INNER JOIN film_actor
ON actor.actor_id = film_actor.actor_id
INNER JOIN film
ON film_actor.film_id = film.film_id
INNER JOIN film_category
ON film.film_id = film_category.film_id
INNER JOIN category
ON category.category_id = film_category.category_id



WHERE film.length<60 and category.name = 'Documentary' and film.rating = 'R'

Cupboard Sinner

SELECT f.title, f.description, CONCAT(c.first_name, ' ', c.last_name) AS fullname, f.replacement_cost
FROM film f 
INNER JOIN inventory i ON f.film_id = i.film_id 
INNER JOIN rental r ON i.inventory_id = r.inventory_id
INNER JOIN customer c ON r.customer_id = c.customer_id
WHERE LOWER(title) LIKE '%boat%' OR LOWER(description) LIKE '%boat%'
AND c.first_name = 'Matthew' AND c.last_name =`` 'Mahan'
ORDER BY f.replacement_cost DESC