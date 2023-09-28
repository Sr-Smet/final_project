# Задание 1

SELECT login, COUNT("Orders". "inDelivery") FROM "Couriers" INNER JOIN "Orders" ON "Couriers"id = "Orders". "courierld" GROUP BY
1,"Orders". "inDelivery" HAVING "Orders". "inDelivery" = true;


# Задание 2

SELECT track, CASE WHEN finished = true THEN '2' WHEN cancelled = true THEN '-1' WHEN "inDelivery" = true THEN '1' ELSE 'O' END AS
Статус FROM "Orders";