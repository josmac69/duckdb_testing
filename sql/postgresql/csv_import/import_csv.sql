COPY user_data(
    user_id,
    first_name,
    last_name,
    email,
    signup_date,
    last_login,
    is_active,
    account_balance,
    country_code,
    favorite_number,
    profile_text,
    checksum
)
FROM '/sql/postgresql/csv_import/data.csv' DELIMITER ',' CSV HEADER;