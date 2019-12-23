import duckdb

"""Script to create Robust04 database scheme in DuckDB"""

folder = "/home/mick/ir/olddog"

sql = """
	DROP TABLE IF EXISTS terms; 
	DROP TABLE IF EXISTS dict; 
	DROP TABLE IF EXISTS docs;

	CREATE TABLE docs (
	    collection_id    VARCHAR(30),
	    id     INTEGER PRIMARY KEY,
	    len   INTEGER,
	    doc_length_small_int SMALLINT
    	);

	CREATE TABLE dict (
	    termid INTEGER PRIMARY KEY,
	    term VARCHAR(100),
	    df INTEGER
    	);

	CREATE TABLE terms (
	    termid    INTEGER,
	    docid     INTEGER,
	    count INTEGER
    	);


--	ALTER TABLE terms ADD CONSTRAINT "terms_dict_id_fkey" FOREIGN KEY (termid) REFERENCES dict (termid);
--	ALTER TABLE terms ADD CONSTRAINT "terms_doc_id_fkey" FOREIGN KEY (docid) REFERENCES docs (id);

"""

copy_docs = """ COPY docs
FROM '{}/docs.csv' 
WITH (DELIMITER '|')
"""

copy_dict = """ COPY dict
FROM '{}/dict.csv' 
WITH (DELIMITER '|')
"""

copy_terms = """ COPY terms
FROM '{}/terms.csv' 
WITH (DELIMITER '|') 
"""

def main():
    print("Creating DuckDB cursor...")
    cursor = duckdb.connect('robust04').cursor()
    print("Executing DDL SQL...")
    cursor.execute(sql)
    print("Executing DML SQL...")
    cursor.execute(copy_docs.format(folder))
    cursor.execute(copy_dict.format(folder))
    cursor.execute(copy_terms.format(folder))

if __name__ == "__main__":
    main()
