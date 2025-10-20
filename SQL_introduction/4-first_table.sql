-- creates a table named 'first_table' in current db
-- should not fail even if table already exists
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
)
