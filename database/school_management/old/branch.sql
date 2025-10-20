/*
 Navicat Premium Dump SQL

 Source Server         : ali_pishnamaz
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/07/2025 20:06:50
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for branch
-- ----------------------------
DROP TABLE IF EXISTS "branch";
CREATE TABLE "branch" (
  "branchNo" INTEGER PRIMARY KEY AUTOINCREMENT,
  "street" TEXT,
  "city" TEXT,
  "postalCode" INTEGER
);

-- ----------------------------
-- Records of branch
-- ----------------------------
INSERT INTO "branch" VALUES (1, 'Langari', 'tehran', 12345);
INSERT INTO "branch" VALUES (2, 'azadi', 'tehran', 1234567);
INSERT INTO "branch" VALUES (3, 'Valiasr', 'shiraz', 12344567);
INSERT INTO "branch" VALUES (4, 'enghelab', 'tehran', 12354567);
INSERT INTO "branch" VALUES (5, '7tir', 'tehran', 12345567);
INSERT INTO "branch" VALUES (6, 'sadi', 'esfahan', 41234567);
INSERT INTO "branch" VALUES (7, 'Langori', 'zabol', 34343434);
INSERT INTO "branch" VALUES (8, 'langar', 'abadan', 4545454);
INSERT INTO "branch" VALUES (9, 'azadi', 'abadan', 234234234);

-- ----------------------------
-- Auto increment value for branch
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 9 WHERE name = 'branch';

PRAGMA foreign_keys = true;
