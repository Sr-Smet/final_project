# Задание 1

SELECT login, COUNT ("Orders".id) AS Orders_count FROM "Couriers" JOIN "Orders" ON "Couriers".id="Orders"."courierId" WHERE "inDelivery" = true
 GROUP BY login;



# Задание 2

SELECT track, CASE WHEN finished = true THEN '2' WHEN cancelled = true THEN '-1' WHEN "inDelivery" = true THEN '1' ELSE 'O' END AS
Статус FROM "Orders";