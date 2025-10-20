-- lists all second_table scores >= 10
-- score column first, then name
-- goes from top score in descending order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
