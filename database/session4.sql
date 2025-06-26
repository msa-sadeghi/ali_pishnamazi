-- SELECT COUNT(DISTINCT salary) FROM staff
-- WHERE salary > 10
-- 
-- SELECT * FROM viewing
-- WHERE viewDATE BETWEEN 2010 AND 2012

-- SELECT branchNo, COUNT(staffNo) count, SUM(salary) salary  FROM staff
-- GROUP BY branchNo
-- HAVING COUNT(staffNo) > 1
-- ORDER BY salary DESC

-- SELECT * FROM staff
-- WHERE branchNo = 
-- (SELECT branchNo FROM branch
-- WHERE LOWER(street) = 'langari')

SELECT *, salary - (SELECT AVG(salary) FROM staff) diff FROM staff
WHERE salary > 
(SELECT AVG(salary) FROM staff)

