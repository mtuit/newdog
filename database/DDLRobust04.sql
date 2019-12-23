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
