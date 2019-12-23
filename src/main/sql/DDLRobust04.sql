-- DDL to create Robust04 database scheme in MonetDB
-- For optimal loading times of the csv bulk data, add the foreign keys after loading the data. The data will still be checked if it does not violate
-- the data, however it is much quicker as opposed to check after every INSERT statement. 

START TRANSACTION;
SET SCHEMA "sys";
CREATE TABLE "sys"."docs" (
	"collection_id"    VARCHAR(30),
	"id"     INTEGER,
	"len"   INTEGER,
	"doc_length_small_int" SMALLINT,
	CONSTRAINT "docs_doc_id_pkey" PRIMARY KEY ("id")
);

CREATE TABLE "sys"."dict" (
	"termid" INTEGER,
	"term" VARCHAR(100),
	"df" INTEGER,
	CONSTRAINT "dict_termid" PRIMARY KEY ("termid")
);

CREATE TABLE "sys"."terms" (
	"termsid" INTEGER AUTO_INCREMENT,
	"termid"    INTEGER,
	"docid"     INTEGER,
	"count" INTEGER,
	PRIMARY KEY("termsid")
);

ALTER TABLE "sys"."terms" ADD CONSTRAINT "terms_dict_id_fkey" FOREIGN KEY ("termid") REFERENCES "sys"."dict" ("termid");

ALTER TABLE "sys"."terms" ADD CONSTRAINT "terms_doc_id_fkey" FOREIGN KEY ("docid") REFERENCES "sys"."docs" ("id");

COMMIT;
