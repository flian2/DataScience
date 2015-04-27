
-- C = A*B
SELECT c FROM (
	SELECT row, col, (sum(prod)) as c
	FROM (
		SELECT (a.row_num) as row , (b.col_num) as col, (a.value*b.value) as prod
		FROM a,b
		WHERE a.col_num = b.row_num) 
	GROUP BY row, col
	) c
WHERE row = 2 AND col = 3;






-- cell(2,3)
-- SELECT sum(a.value*b.value) 
-- FROM  a,b
-- WHERE a.row_num = 2 AND b.col_num = 3 AND a.col_num = b.row_num;