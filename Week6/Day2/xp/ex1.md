EX1

q1

All items, ordered by price (lowest to highest).
	SELECT * FROM items ORDER BY price ASC

Items with a price above 80 (80 included), ordered by price (highest to lowest).
	SELECT * FROM items WHERE price>= 80 ORDER BY price DESC;

The first 3 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
	SELECT first_name, last_name FROM customers ORDER BY first_name LIMIT 3; 

All last names (no other columns!), in reverse alphabetical order (Z-A)
	SELECT last_name FROM customers ORDER BY last_name DESC;


q2

CREATE TABLE purchases(
transaction_id SERIAL,
customer_id INTEGER,
item_id INTEGER,
FOREIGN KEY (customer_id) REFERENCES customers(id),
FOREIGN KEY (item_id) REFERENCES items(id) )

All purchases joining with customer table:

SELECT customers.first_name, customers.last_name, items.item_name as item_bought, items.price as price 
FROM purchases
	INNER JOIN customers
		ON purchases.customer_id = customers.id
	INNER JOIN items
		ON purchases.item_id = items.id

All purchases made by specific customer:

SELECT customers.first_name, customers.last_name, items.item_name as item_bought, items.price as price 
FROM purchases
	INNER JOIN customers
		ON purchases.customer_id = customers.id
	INNER JOIN items
		ON purchases.item_id = items.id
WHERE customer_id = 4

All purchases made of specific items:

SELECT customers.first_name, customers.last_name, items.item_name as item_bought, items.price as price 
FROM purchases
	INNER JOIN customers
		ON purchases.customer_id = customers.id
	INNER JOIN items
		ON purchases.item_id = items.id
WHERE item_id = 1 or item_id = 2