/*
 Navicat Premium Dump SQL

 Source Server         : ali_pishnamaz
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/07/2025 20:16:45
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for PropertyForRent
-- ----------------------------
DROP TABLE IF EXISTS "PropertyForRent";
CREATE TABLE "PropertyForRent" (
  "propertyNo" INTEGER PRIMARY KEY AUTOINCREMENT,
  "street" TEXT,
  "city" TEXT,
  "postalcode" INTEGER,
  "type" TEXT,
  "rooms" INTEGER,
  "rent" REAL,
  "ownerNo" INTEGER,
  "staffNo" INTEGER,
  "branchNo" INTEGER,
  FOREIGN KEY ("ownerNo") REFERENCES "owner" ("ownerNo") ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY ("staffNo") REFERENCES "staff" ("staffNo") ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY ("branchNo") REFERENCES "branch" ("branchNo") ON DELETE SET NULL ON UPDATE CASCADE
);

-- ----------------------------
-- Records of PropertyForRent
-- ----------------------------
INSERT INTO "PropertyForRent" VALUES (1, 's1', 'c1', 123, 'v', 3, 10.0, 1, 1, 1);
INSERT INTO "PropertyForRent" VALUES (2, 's2', 'c2', 1234, 'h', 2, 5.0, 2, 9, 2);
INSERT INTO "PropertyForRent" VALUES (3, 's3', 'c3', 123, 'v', 4, 15.0, 3, 1, 3);
INSERT INTO "PropertyForRent" VALUES (4, 's4', 'c4', 123, 'h', 4, 20.0, 1, 5, 4);

-- ----------------------------
-- Auto increment value for PropertyForRent
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 4 WHERE name = 'PropertyForRent';

PRAGMA foreign_keys = true;
