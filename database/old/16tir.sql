-- CREATE TABLE "client" (
--   "clientNo" SERIAL PRIMARY KEY ,
--   "fName" VARCHAR(30),
--   "lName" VARCHAR(30),
--   "tel" INT,
--   "prefType" VARCHAR(30),
--   "maxRent" float,
--   "email" VARCHAR(30)
-- );

-- CREATE TABLE "owner" (
--   "ownerNo" SERIAL PRIMARY KEY,
--   "fName" VARCHAR(50),
--   "lName" VARCHAR(50),
--   "address" VARCHAR(50),
--   "tel" INT,
--   "email" VARCHAR(50),
--   "password" VARCHAR(50)
-- );

-- ----------------------------
-- Records of owner
-- ----------------------------
-- INSERT INTO "owner" VALUES (1, 'f1', 'l1', 'addr1', 1, 'e1', 'p1');
-- INSERT INTO "owner" VALUES (2, 'f2', 'l2', 'addr2', 2, 'e2', 'p2');
-- INSERT INTO "owner" VALUES (3, 'f3', 'l3', 'addr3', 3, 'e3', 'p3');
-- INSERT INTO "owner" VALUES (4, 'f4', 'l4', 'addr4', 4, 'e4', 'p4');
-- INSERT INTO "owner" VALUES (5, 'f5', 'l5', 'addr5', 5, 'e5', 'p5');
-- CREATE TABLE "staff" (
--   "staffNo" SERIAL PRIMARY KEY,
--   "fName" VARCHAR(50),
--   "lName" VARCHAR(50),
--   "position" VARCHAR(50),
--   "sex" VARCHAR(5),
--   "DOB" VARCHAR(50),
--   "salary" FLOAT,
--   "branchNo" INT,
--   FOREIGN KEY ("branchNo") REFERENCES "branch" ("branchNo") ON DELETE NO ACTION ON UPDATE NO ACTION
-- );


-- CREATE TABLE "PropertyForRent" (
--   "propertyNo" SERIAL PRIMARY KEY,
--   "street" VARCHAR(50),
--   "city" VARCHAR(50),
--   "postalcode" INT,
--   "type" VARCHAR(50),
--   "rooms" INT,
--   "rent" FLOAT,
--   "ownerNo" INT,
--   "staffNo" INT,
--   "branchNo" INT,
--   FOREIGN KEY ("ownerNo") REFERENCES "owner" ("ownerNo") ON DELETE SET NULL ON UPDATE CASCADE,
--   FOREIGN KEY ("staffNo") REFERENCES "staff" ("staffNo") ON DELETE SET NULL ON UPDATE CASCADE,
--   FOREIGN KEY ("branchNo") REFERENCES "branch" ("branchNo") ON DELETE SET NULL ON UPDATE CASCADE
-- );


-- CREATE TABLE "viewing" (
--   "clientNo" SERIAL PRIMARY KEY,
--   "propertyNo" INT,
--   "viewDATE" VARCHAR(50),
--   "comment" TEXT,
--   FOREIGN KEY ("propertyNo") REFERENCES "PropertyForRent" ("propertyNo") ON DELETE NO ACTION ON UPDATE NO ACTION
-- );



