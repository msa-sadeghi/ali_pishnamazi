-- SELECT * FROM branch
-- WHERE LOWER(city) = 'tehran' AND street = 'azadi'

-- SELECT city, count(*) AS count FROM branch
-- GROUP BY city

SELECT city FROM branch
GROUP BY city ORDER BY city DESC