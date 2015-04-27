SELECT load_extension('./libsqlitefunctions.dylib');


SELECT  value/(rowMod*colMod)
FROM(	
	SELECT row, col, sum(prod) as value, 
	(SELECT sqrt(sum(square(c.count))) FROM Frequency c
	WHERE c.docid = row) as rowMod,
	(SELECT sqrt(sum(square(d.count))) FROM Frequency d
	WHERE d.docid = col) as colMod
	FROM (
		SELECT (a.docid) as row , (b.docid) as col, (a.count) as a_value, (b.count) as b_value, (a.count*b.count) as prod
		FROM Frequency a,Frequency b
		WHERE a.term = b.term AND a.docid <= b.docid
		) 
	GROUP BY row, col
	)
WHERE row = "10080_txt_crude" AND col="17035_txt_earn";
	


