-- displays all rows with a valid name by descending score
-- score first, then name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
