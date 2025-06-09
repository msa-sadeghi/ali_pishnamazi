-- SELECT * FROM branch
-- WHERE LOWER(city) = 'tehran' AND street = 'azadi'

-- SELECT city, count(*) AS count FROM branch
-- GROUP BY city
SELECT street FROM branch
WHERE city IN
(SELECT city FROM branch
GROUP BY city)