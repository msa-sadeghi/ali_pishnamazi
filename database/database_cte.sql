-- CREATE TABLE users(
-- 	id SERIAL PRIMARY KEY,
-- 	username VARCHAR(50) NOT NULL,
-- 	email VARCHAR(100) NOT NULL
-- );

-- CREATE TABLE userprofiles(
-- 	id SERIAL PRIMARY KEY,
-- 	bio TEXT,
-- 	user_id INT UNIQUE REFERENCES users(id)
-- );

-- SELECT * FROM users
WITH new_user AS (
INSERT INTO users VALUES(DEFAULT, 'sara', 'sara@gmail.com')
RETURNING id
)

INSERT INTO userprofiles (bio, user_id)
SELECT  'blalal', id FROM new_user

SELECT * FROM userprofiles




