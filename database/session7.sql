

-- SELECT * FROM staff
WHERE salary > SOME (SELECT salary FROM staff
WHERE branchNo IN(
SELECT branchNo FROM branch
WHERE street = 'azadi'
)
)


-- SELECT * FROM PropertyForRent
-- WHERE staffNo IN
-- (SELECT staffNo FROM staff
-- WHERE branchNo IN 
-- (SELECT branchNo FROM branch
-- WHERE street = 'azadi'))
