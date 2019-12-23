
CREATE TABLE docs (
	collection_id    VARCHAR(30),
	id     INTEGER,
	len   INTEGER,
	doc_length_small_int SMALLINT,
	CONSTRAINT docs_doc_id_pkey PRIMARY KEY (id)
);

CREATE TABLE dict (
	termid INTEGER,
	term VARCHAR(100),
	df INTEGER,
	CONSTRAINT dict_termid PRIMARY KEY (termid)
);

CREATE TABLE terms (
	termsid INTEGER AUTO_INCREMENT,
	termid    INTEGER,
	docid     INTEGER,
	count INTEGER,
	PRIMARY KEY(termsid)
);

ALTER TABLE terms ADD CONSTRAINT terms_dict_id_fkey FOREIGN KEY (termid) REFERENCES dict (termid);

ALTER TABLE terms ADD CONSTRAINT terms_doc_id_fkey FOREIGN KEY (docid) REFERENCES docs (id);

