SELECT docid, sum(count)  FROM Frequency
GROUP BY docid
HAVING sum(count) > 300;