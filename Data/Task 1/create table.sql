DROP TABLE IF EXISTS data_task;
DROP TABLE IF EXISTS summary_table;

CREATE TABLE IF NOT EXISTS data_task (
    id 		   NUMERIC,
    title      text,
    author     text,
    genre      text,
    publisher  text,
    year       int,
    price      TEXT,
    currency TEXT,
    price_numeric NUMERIC,
    price_in_usd NUMERIC
);

UPDATE data_task
SET currency = regexp_replace(price, '[0-9.,-]', '', 'g'),
    price_numeric = regexp_replace(price, '[^0-9.,-]', '', 'g')::numeric;

UPDATE data_task
SET price_in_usd =
    CASE
        WHEN currency = '$' THEN price_numeric
        WHEN currency = '€' THEN price_numeric * 1.2
        ELSE NULL
    END;

SELECT * FROM data_task;

CREATE TABLE summary_table AS 
SELECT year, COUNT(*) AS book_count, ROUND(AVG(price_in_usd),2) AS average_price
FROM data_task
GROUP BY year;

SELECT * FROM summary_table;

SELECT COUNT(*) FROM summary_table;
SELECT COUNT(*) FROM data_task;
