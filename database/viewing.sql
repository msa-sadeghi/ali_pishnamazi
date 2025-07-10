/*
 Navicat Premium Dump SQL

 Source Server         : ali_pishnamaz
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/07/2025 20:19:52
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for viewing
-- ----------------------------
DROP TABLE IF EXISTS "viewing";
CREATE TABLE "viewing" (
  "clientNo" INTEGER PRIMARY KEY AUTOINCREMENT,
  "propertyNo" INTEGER,
  "viewDATE" TEXT,
  "comment" TEXT,
  FOREIGN KEY ("propertyNo") REFERENCES "PropertyForRent" ("propertyNo") ON DELETE NO ACTION ON UPDATE NO ACTION
);

-- ----------------------------
-- Records of viewing
-- ----------------------------
INSERT INTO "viewing" VALUES (1, 1, '2010', 'good');
INSERT INTO "viewing" VALUES (2, 2, '2012', 'bad');
INSERT INTO "viewing" VALUES (3, 3, '2022', 'great');

-- ----------------------------
-- Auto increment value for viewing
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 3 WHERE name = 'viewing';

PRAGMA foreign_keys = true;
