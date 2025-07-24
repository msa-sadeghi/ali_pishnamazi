-- For each branch, list the staff numbers and names of staff who manage properties, including the city in 
-- which the branch is located and the properties that the staff manage.

-- SELECT * FROM "PropertyForRent" p, staff s, branch b
-- WHERE p."staffNo" = s."staffNo" AND b."branchNo" = s."branchNo"


-- SELECT * FROM "PropertyForRent" p
-- JOIN staff s ON p."staffNo" = s."staffNo"
-- JOIN branch b ON s."branchNo" = b."branchNo"

-- Find the number of properties handled by each staff member, along with the branch number of the 
-- member of staff.

SELECT s."branchNo", s."staffNo", COUNT(*) FROM "PropertyForRent" p
JOIN staff s ON s."staffNo" = p."staffNo"

SELECT "branchNo", COUNT(*) FROM branch
GROUP BY city, "branchNo"



