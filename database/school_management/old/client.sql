/*
 Navicat Premium Dump SQL

 Source Server         : ali_pishnamaz
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 07/07/2025 20:07:14
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for client
-- ----------------------------
DROP TABLE IF EXISTS "client";
CREATE TABLE "client" (
  "clientNo" INTEGER PRIMARY KEY AUTOINCREMENT,
  "fName" TEXT,
  "lName" TEXT,
  "tel" INTEGER,
  "prefType" TEXT,
  "maxRent" REAL,
  "email" TEXT
);

-- ----------------------------
-- Records of client
-- ----------------------------

PRAGMA foreign_keys = true;
