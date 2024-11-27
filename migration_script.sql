<module 'app.models.data_models.client' from 'C:\\Users\\Kir\\Desktop\\callmaster\\app\\models\\data_models\\client.py'>
<module 'app.models.data_models.main' from 'C:\\Users\\Kir\\Desktop\\callmaster\\app\\models\\data_models\\main.py'>
<module 'app.models.data_models.specialist' from 'C:\\Users\\Kir\\Desktop\\callmaster\\app\\models\\data_models\\specialist.py'>
BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 4ba42083f33a

CREATE TABLE clients (
    id SERIAL NOT NULL, 
    first_name VARCHAR NOT NULL, 
    last_name VARCHAR NOT NULL, 
    middle_name VARCHAR NOT NULL, 
    email VARCHAR NOT NULL, 
    phone_number VARCHAR NOT NULL, 
    password VARCHAR NOT NULL, 
    timestamp TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (email), 
    UNIQUE (phone_number)
);

CREATE INDEX ix_clients_id ON clients (id);

CREATE TABLE specialists (
    id SERIAL NOT NULL, 
    first_name VARCHAR NOT NULL, 
    last_name VARCHAR NOT NULL, 
    middle_name VARCHAR NOT NULL, 
    email VARCHAR NOT NULL, 
    phone_number VARCHAR NOT NULL, 
    password VARCHAR NOT NULL, 
    timestamp TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (email), 
    UNIQUE (phone_number)
);

CREATE INDEX ix_specialists_id ON specialists (id);

CREATE TABLE specialities (
    id SERIAL NOT NULL, 
    name VARCHAR NOT NULL, 
    timestamp TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id)
);

CREATE INDEX ix_specialities_id ON specialities (id);

CREATE TABLE many_to_many_specialist_specialication (
    id SERIAL NOT NULL, 
    specialist_id INTEGER, 
    specialization_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(specialist_id) REFERENCES specialists (id), 
    FOREIGN KEY(specialization_id) REFERENCES specialities (id)
);

INSERT INTO alembic_version (version_num) VALUES ('4ba42083f33a') RETURNING alembic_version.version_num;

COMMIT;

