SELECT name FROM language

SELECT film.title, film.description, language.name
FROM film
INNER JOIN language ON film.language_id = language.language_id

SELECT film.title, film.description, language.name
FROM film
RIGHT OUTER JOIN language 
ON film.language_id = language.language_id


CREATE TABLE customer_review(
   review_id serial PRIMARY KEY,
   film_id int NOT NULL,
   FOREIGN KEY (film_id) REFERENCES film(film_id) ON DELETE CASCADE,
   language_id int,
   FOREIGN KEY (language_id) REFERENCES language(language_id),
   title VARCHAR(50),
   score int,
   review_text TEXT,
   last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP)