-- prob 1
SELECT count (*) FROM(
	SELECT *
	FROM Frequency
	WHERE Frequency.docid = "10398_txt_earn"
) x;