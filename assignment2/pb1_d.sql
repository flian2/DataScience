SELECT count(*) FROM(
	SELECT docid  FROM Frequency
	WHERE term = "legal"
	UNION
	SELECT docid FROM Frequency
	WHERE term = "law"
	);

-- SELECT count(*) FROM(
-- 	SELECT docid  FROM Frequency
-- 	WHERE term = "legal"
-- 	-- UNION
-- 	-- SELECT docid FROM Frequency
-- 	-- WHERE term = "law"
-- 	);
