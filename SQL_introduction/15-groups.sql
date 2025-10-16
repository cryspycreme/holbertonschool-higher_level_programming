--
ALTER TABLE second_table
ADD COLUMN number COUNT(score);

SELECT score, number
ORDER BY number DESC;

