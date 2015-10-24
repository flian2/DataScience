-- SELECT count(*) FROM(
-- 	SELECT DISTINCT docid FROM Frequency
-- 	WHERE term="world"
-- 	INTERSECT
-- 	SELECT DISTINCT docid FROM Frequency
-- 	WHERE term="transactions"
-- );

SELECT count(*) FROM(
	SELECT docid FROM Frequency
	WHERE term="world"
	INTERSECT
	SELECT docid FROM Frequency
	WHERE term="transactions"
);

