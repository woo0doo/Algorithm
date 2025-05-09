SELECT l.hour, nvl(count, 0) AS count

FROM (SELECT TO_CHAR(datetime, 'HH24') AS hour, count(*) AS count 
        FROM animal_outs 
        GROUP BY TO_CHAR(datetime, 'HH24') 
        ORDER BY hour) O
    RIGHT JOIN (SELECT LEVEL-1 AS hour FROM dual CONNECT BY LEVEL<=24) L
    ON L.hour = O.hour

ORDER BY L.hour;