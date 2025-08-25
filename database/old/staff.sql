/*
 Navicat Premium Dump SQL

 Source Server         : ali_pishnamaz
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/07/2025 20:18:33
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS "staff";
CREATE TABLE "staff" (
  "staffNo" INTEGER PRIMARY KEY AUTOINCREMENT,
  "fName" TEXT,
  "lName" TEXT,
  "position" TEXT,
  "sex" TEXT,
  "DOB" TEXT,
  "salary" REAL,
  "branchNo" INTEGER,
  FOREIGN KEY ("branchNo") REFERENCES "branch" ("branchNo") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO "staff" VALUES (1, 'Zahra', 'Panahi', 'Boss', 'female', '1973/08/24', 10.0, 4);
INSERT INTO "staff" VALUES (2, 'Ali', 'Panahi', 'Cashier', 'male', '1976/03/22', 15.0, 4);
INSERT INTO "staff" VALUES (3, 'Mostafa', 'Zarei', 'Cashier', 'male', '1983/12/12', 11.0, 1);
INSERT INTO "staff" VALUES (4, 'Mahdi', 'Tavakoli', 'Cashier', 'male', '1990/03/21', 20.0, 3);
INSERT INTO "staff" VALUES (5, 'Reza', 'Hashemi', 'Cashier', 'male', '1970/11/11', 22.0, 2);
INSERT INTO "staff" VALUES (6, 'Sara', 'Mirmohammadali', 'Store management', 'female', '1968/12/19', 9.0, 2);
INSERT INTO "staff" VALUES (7, 'Fatemeh', 'Heydari', 'Store management', 'female', '1969/10/27', 15.0, 4);
INSERT INTO "staff" VALUES (8, 'Mojgan', 'Pourhossein', 'Store management', 'female', '1985/02/09', 19.0, 1);
INSERT INTO "staff" VALUES (9, 'Jaleh', 'Hoorakhsh', 'Store management', 'female', '1977/07/17', 16.0, 3);
INSERT INTO "staff" VALUES (10, 'Ahmad', 'Abedzadeh', 'Costumer service', 'male', '1970/03/02', 24.0, 2);
INSERT INTO "staff" VALUES (11, 'Gelareh', 'Pourbehroozi', 'Costumer service', 'female', '1988/08/10', 8.0, 4);
INSERT INTO "staff" VALUES (12, 'Kian', 'Fathi', 'Costumer service', 'male', '2000/01/04', 23.0, 3);
INSERT INTO "staff" VALUES (13, 'Ata', 'Deilami', 'Costumer service', 'male', '1984/12/21', 21.0, 1);
INSERT INTO "staff" VALUES (14, 'Sana', 'Shams', 'Logistics', 'female', '1983/02/22', 20.0, 3);
INSERT INTO "staff" VALUES (15, 'Hosein', 'Mirmohammadali', 'Logistics', 'male', '1968/12/19', 13.0, 2);
INSERT INTO "staff" VALUES (16, 'Kourosh', 'Baserisalehi', 'Logistics', 'male', '1999/06/02', 18.0, 4);
INSERT INTO "staff" VALUES (17, 'Nazanin', 'Sabouri', 'Logistics', 'female', '1989/08/13', 17.0, 1);
INSERT INTO "staff" VALUES (18, 'Abolfazl', 'Abedininasab', 'Corporate roles', 'male', '1969/02/07', 10.0, 4);
INSERT INTO "staff" VALUES (19, 'Roozbeh', 'Rezanasab', 'Corporate roles', 'male', '1972/04/24', 12.0, 3);
INSERT INTO "staff" VALUES (20, 'Azadeh', 'Moslempour', 'Corporate roles', 'female', '1974/04/25', 11.0, 1);
INSERT INTO "staff" VALUES (21, 'Yara', 'Ahmadi', 'Corporate roles', 'male', '1975/12/02', 9.0, 2);

-- ----------------------------
-- Auto increment value for staff
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 21 WHERE name = 'staff';

PRAGMA foreign_keys = true;
