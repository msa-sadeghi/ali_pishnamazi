-- INSERT  INTO staff 
-- VALUES (DEFAULT,'reza', 'rezaei', 'developer', 'M', '2012-05-07', 10000, 1);

-- SELECT  * FROM staff;
-- UPDATE staff 
-- SET position = 'developer'
-- WHERE "fName" = 'sara'

-- ALTER TABLE staff 
-- RENAME COLUMN "staffNo" To staffno

-- CREATE TABLE IF NOT EXISTS test(
-- 	sex VARCHAR(1) CHECK(sex IN ('M', 'F', 'O')) DEFAULT 'F'
-- );
-- CHECK salary BETWEEN 1 AND 2


-- INSERT INTO test
-- VALUES ('M');

ALTER TABLE test ALTER sex SET DEFAULT 'F'
ALTER TABLE test ALTER sex DROP DEFAULT 
ALTER TABLE test ADD COLUMN age INT DEFAULT 25
INSERT INTO test VALUES ('F')
SELECT * FROM test
ALTER TABLE test DROP COLUMN age

DROP TABLE test