SELECT count(*) FROM (
	SELECT docid, sum(count)  FROM Frequency
	GROUP BY docid
	HAVING count(docid) > 300
	);

-- select documents whose sum of counts are greater than 300