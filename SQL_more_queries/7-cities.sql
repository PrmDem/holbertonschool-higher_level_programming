-- creates 'cities' table with id, name, and state_id
-- primary key = 'id', foreign key = 'state_id'
-- VARCHAR(256) name can't be null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT PRIMARY KEY AUTO_INCREMENT,
    state_id INT NOT NULL,
    CONSTRAINT FK_REFER FOREIGN KEY (state_id)
    REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
