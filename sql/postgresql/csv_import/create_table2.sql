CREATE TABLE probe_measurements (
    measurement_id BIGSERIAL PRIMARY KEY,
    probe_id INTEGER NOT NULL,
    measurement_time TIMESTAMP NOT NULL,
    temperature NUMERIC(5,2) NOT NULL,
    pressure NUMERIC(6,2) NOT NULL,
    humidity NUMERIC(5,2) NOT NULL,
    voltage NUMERIC(5,2) NOT NULL,
    current NUMERIC(5,2) NOT NULL,
    resistance NUMERIC(10,2) NOT NULL,
    sample_rate INTEGER NOT NULL
);
