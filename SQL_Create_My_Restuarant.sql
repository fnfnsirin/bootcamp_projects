--Restaurant Owners
-- 5 tables
--1xFact, 4xDimensions
--search google,how to add foreign key
--write SQL 3-5 queries analyze data
--1 subquery/with
.mode markdown
.header on
CREATE TABLE orders(
	order_id INT PRIMARY KEY,
	order_date date,
	customer_id INT,
	items TEXT,
	net_price REAL,
  	sales_id INT,
  	payment_methods TEXT,
FOREIGN KEY(customer_id) REFERENCES membership(customer_id)
FOREIGN KEY(items) REFERENCES cost(items)
FOREIGN KEY(sales_id) REFERENCES sales(sales_id)
FOREIGN KEY(payment_methods) REFERENCES payment(payment_methods)
  );
INSERT INTO orders VALUES
  (1,'2022-07-01',1,'Salmon Roll',129.0,1,1),
  (2,'2022-07-01',1,'Tonkatsu',150.0,1,1),
  (3,'2022-07-12',5,'Hamburger',89.0,2,1),
  (4,'2022-07-15',4,'Salmon Roll',129.0,4,1),
  (5,'2022-07-15',3,'Salmon Sushi',30.0,3,1),
  (6,'2022-07-20',2,'Tonkatsu',150.0,2,2),
  (7,'2022-07-20',2,'Salmon Roll',129.0,2,2),
  (8,'2022-07-20',2,'Jeju juice',59.0,1,2),
  (9,'2022-08-04',2,'Jeju juice',59.0,3,1),
  (10,'2022-08-10',1,'Salmon Roll',129.0,4,1),
  (11,'2022-08-10',4,'Salmon Roll',129.0,4,1),
  (12,'2022-08-15',3,'Tonkatsu',150.0,2,2),
  (13,'2022-08-22',5,'Salmon Roll',129.0,1,1),
  (14,'2022-08-22',5,'Jeju juice',59.0,3,1),
  (15,'2022-08-22',5,'Salmon Sushi',30.0,3,1),
  (16,'2022-08-31',1,'Salmon Roll',129.0,3,1)
  ;
CREATE TABLE membership(
  customer_id INT UNIQUE PRIMARY KEY,
  customer_name TEXT,
  phone_number TEXT,
  email TEXT,
  residence TEXT
);
INSERT INTO membership VALUES
  (1,'Brown','0667779990','brown@linefriends.com','Ladprao'),
  (2,'Sally','','sally@linefriends.com','Thonglor'),
  (3,'Choco','0889997890','choco@linefriends.com','Nontaburi'),
  (4,'Cony','0657894111','cony@linefriends.com','Thapra'),
  (5,'Leonard','0887669999','leonard@linefriends.com','');
create table cost(
  items TEXT primary KEY,
  cost_items REAL
 )
;
insert into cost VALUES
	('Salmon Roll',110.9),
    ('Tonkatsu',135.8),
    ('Hamburger',60.5),
    ('Salmon Sushi',17.6),
    ('Jeju juice',45.7)
;

CREATE table sales(
  sales_id INT PRIMARY KEY,
  shift_work TEXT,
  sale_name TEXT
 )
 ;
 insert into sales VALUES
 	(1,'Day Shift','Marry'),
    (2,'Day Shift','Vivy'),
    (3,'Night Shift','Tom'),
    (4,'Night Shift','Bob')   
;

create table payment(
  payment_methods TEXT PRIMARY KEY,
  payment_name TEXT
 );
 insert into payment VALUES
 ('1','Cash'),
 ('2','Credit Card')
;

SELECT
		menu,
		count(*) as n_items,
        SUM(net_price),
        round(SUM(net_price)-(cost_unit * count(*)),2) AS net_profit
        
FROM
(select	
  		orders.order_id,
    	orders.order_date,
        orders.items as menu,
    	orders.net_price as net_price,
    	cost.cost_items as cost_unit,
    	payment.payment_name,
    	sales.shift_work,
    	sales.sale_name,
    	membership.email as email_customers
	FROM orders 
		JOIN cost 			   on orders.items = cost.items
		JOIN payment 	   on orders.payment_methods = payment.payment_methods
		join sales 			  on orders.sales_id = sales.sales_id
		JOIN membership  on orders.customer_id = membership.customer_id
) as sub
group by 1
order by 2 DESC
;

select 
	strftime('%Y%m', orders.order_date) AS month_id,
    sum(net_price) as amount,
    count(*) as n_bill
from orders
GROUP by 1
;

SELECT  
	customer_name,
    count(*) as frequency,
    sum(orders.net_price) AS amount,
    email,
    residence
FROM membership
JOIN orders on membership.customer_id = orders.customer_id
GROUP by 1
order by 2 DESC,3 DESC;

select 
    sales.sale_name,
    COUNT(*) as n_transaction,
    sum(orders.net_price) as amt_sale,
    payment.payment_name
FROM orders 
Join sales on orders.sales_id = sales.sales_id
JOIN payment on orders.payment_methods = payment.payment_methods
group by 1,4
order by 1,2 DESC,3 DESC
;
