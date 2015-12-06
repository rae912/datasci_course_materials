-- (h) similarity matrix 19
select sum(a.count*b.count) from Frequency a, Frequency b where a.docid='10080_txt_crude' and b.docid='17035_txt_earn' and a.term=b.term;

-- (i) keyword search 6
SELECT similarity
FROM (
     SELECT B.docid as secondDoc, sum(A.count*B.count) as similarity
     FROM 
        (SELECT *
        FROM frequency
        UNION SELECT 'q' as docid, 'washington' as term, 1 as count 
        UNION SELECT 'q' as docid, 'taxes' as term, 1 as count
        UNION SELECT 'q' as docid, 'treasury' as term, 1 as count) as A,
        (SELECT *
        FROM frequency
        UNION SELECT 'q' as docid, 'washington' as term, 1 as count 
        UNION SELECT 'q' as docid, 'taxes' as term, 1 as count
        UNION SELECT 'q' as docid, 'treasury' as term, 1 as count) as B
     WHERE A.term=B.term and A.docid='q'
     GROUP BY B.docid
)
ORDER BY -similarity
LIMIT 1
;