-- creates table force_name with INT id, VARCHAR(256) name
-- name column cannot be null
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
