-- 코드를 입력하세요
SELECT FP.PRODUCT_ID, FP.PRODUCT_NAME, SUM((PRICE*AMOUNT)) AS TOTAL_SALES
    FROM FOOD_PRODUCT FP
    JOIN FOOD_ORDER FO
    ON FP.PRODUCT_ID = FO.PRODUCT_ID
    WHERE TO_CHAR(FO.PRODUCE_DATE, 'YYYY-MM') = '2022-05'
    GROUP BY FP.PRODUCT_ID, FP.PRODUCT_NAME
    ORDER BY TOTAL_SALES DESC, PRODUCT_ID;
