CREATE TABLE user_data (
    user_id BIGSERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    signup_date TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    account_balance NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    country_code CHAR(2) NOT NULL,
    favorite_number INTEGER,
    profile_text TEXT,
    checksum UUID NOT NULL
);
