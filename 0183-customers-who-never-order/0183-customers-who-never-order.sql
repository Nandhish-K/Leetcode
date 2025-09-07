-- SELECT c.name AS Customers
-- FROM Customers c
-- LEFT JOIN Orders o
--     ON c.id = o.CustomerId
-- WHERE o.CustomerId IS NULL;
SELECT c.name AS Customers
FROM Customers c
where c.id not in  
(
    select customerId from Orders
);

