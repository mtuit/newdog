-- DML to load data ino the Robust04 database from csv tables

START TRANSACTION;  

COPY 529000 RECORDS INTO "sys"."docs" FROM '/home/mick/ir/olddog/docs.csv' DELIMITERS '|' BEST EFFORT;

COPY 923436 RECORDS INTO "sys"."dict" FROM '/home/mick/ir/olddog/dict.csv' DELIMITERS '|' BEST EFFORT;

COPY 99446587 RECORDS INTO "sys"."terms"("termid", "docid", "count") FROM '/home/mick/ir/olddog/terms.csv'("termid", "docid", "count") DELIMITERS '|' BEST EFFORT;

COMMIT;
