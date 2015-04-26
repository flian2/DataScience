SELECT DISTINCT docid FROM Frequency
WHERE term="world"
INTERSECT
SELECT DISTINCT docid FROM Frequency
WHERE term="transactions";
