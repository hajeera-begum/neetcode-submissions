-- Write your query below
SELECT customers.name FROM customers left join orders on  
customers.id = orders.customer_id where orders.customer_id is null

