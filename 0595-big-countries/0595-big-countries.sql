# Write your MySQL query statement below
select w.name,w.population,w.area from World w
where w.area >= 3*power(10,6) or w.population >= 25*power(10,6)