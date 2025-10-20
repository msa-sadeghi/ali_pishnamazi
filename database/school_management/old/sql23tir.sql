-- SELECT * FROM "PropertyForRent"
-- WHERE "staffNo" IN
-- (SELECT "staffNo" FROM staff
-- WHERE "branchNo" =
-- (SELECT "branchNo" FROM branch
-- WHERE street = 'Sadi'))

-- SELECT * FROM staff
-- WHERE salary > ALL (SELECT salary FROM staff WHERE "branchNo" = 1)

-- SELECT * FROM client c, viewing v
-- WHERE c."clientNo" =  v."clientNo"

-- SELECT * FROM client c JOIN viewing v
-- ON c."clientNo" =  v."clientNo"

SELECT * FROM client JOIN viewing USING clientno

SELECT * FROM client NATURAL JOIN viewing;

SELECT * FROm "PropertyForRent"






