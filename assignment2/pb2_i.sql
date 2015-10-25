-- SELECT load_extension('./libsqlitefunctions.dylib');

CREATE VIEW IF NOT EXISTS newFreq AS
	SELECT * FROM Frequency
	UNION
	SELECT 'q' as docid, 'washington' as term, 1 as count 
	UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
	UNION 
	SELECT 'q' as docid, 'treasury' as term, 1 as count;



-- SELECT row, col, sum(prod) as value
-- FROM (
-- 	  SELECT (a.docid) as row , (b.docid) as col, (a.count*b.count) as prod
-- 	  FROM newFreq a, newFreq b
-- 	  WHERE a.term = b.term AND a.docid = 'q' AND b.docid != 'q'
-- 		) 
-- GROUP BY row, col;

-- SELECT c from 
SELECT max(value)
FROM	(
	SELECT row, col, sum(prod) as value
	-- (SELECT sqrt(sum(square(c.count))) FROM newFreq c
	-- WHERE c.docid = row) as rowMod,
	-- (SELECT sqrt(sum(square(d.count))) FROM newFreq d
	-- WHERE d.docid = col) as colMod
	FROM (
		SELECT (a.docid) as row , (b.docid) as col, (a.count) as a_value, (b.count) as b_value, (a.count*b.count) as prod
		FROM newFreq a, newFreq b
		WHERE a.term = b.term AND a.docid = 'q' AND b.docid != 'q'
		) 
	GROUP BY row, col
	);



