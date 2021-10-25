CREATE TABLE IF NOT EXISTS employee (
    id SERIAL PRIMARY KEY,
    rfc VARCHAR(13) UNIQUE,
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    start_date TIMESTAMP DEFAULT NOW(),
    birthday TIMESTAMP,
    profile_picture TEXT,
    job_position VARCHAR(50),
    pronouns = VARCHAR(4)
);
