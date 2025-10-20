/*
 Navicat Premium Dump SQL

 Source Server         : ali_pishnamaz
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/07/2025 20:12:51
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for owner
-- ----------------------------
DROP TABLE IF EXISTS "owner";
CREATE TABLE "owner" (
  "ownerNo" INTEGER PRIMARY KEY AUTOINCREMENT,
  "fName" TEXT,
  "lName" TEXT,
  "address" TEXT,
  "tel" INTERGER,
  "email" TEXT,
  "password" TEXT
);

-- ----------------------------
-- Records of owner
-- ----------------------------
INSERT INTO "owner" VALUES (1, 'f1', 'l1', 'addr1', 1, 'e1', 'p1');
INSERT INTO "owner" VALUES (2, 'f2', 'l2', 'addr2', 2, 'e2', 'p2');
INSERT INTO "owner" VALUES (3, 'f3', 'l3', 'addr3', 3, 'e3', 'p3');
INSERT INTO "owner" VALUES (4, 'f4', 'l4', 'addr4', 4, 'e4', 'p4');
INSERT INTO "owner" VALUES (5, 'f5', 'l5', 'addr5', 5, 'e5', 'p5');

-- ----------------------------
-- Auto increment value for owner
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 5 WHERE name = 'owner';

PRAGMA foreign_keys = true;
