-- displays scores and number of records with that score
-- creating a new column named 'number'
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
