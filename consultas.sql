
-- 1. Top 10 países más poblados
SELECT name_common, population
FROM countries
ORDER BY population DESC
LIMIT 10;

-- 2. Población media por región
SELECT region, AVG(population) AS avg_population
FROM countries
WHERE region IS NOT NULL
GROUP BY region
ORDER BY avg_population DESC;

-- 3. Número de países por región
SELECT region, COUNT(*) AS total_countries
FROM countries
WHERE region IS NOT NULL
GROUP BY region
ORDER BY total_countries DESC;

-- 4. País con mayor superficie por región
SELECT c.region, c.name_common, c.area
FROM countries c
JOIN (
    SELECT region, MAX(area) AS max_area
    FROM countries
    WHERE region IS NOT NULL
    GROUP BY region
) m
ON c.region = m.region AND c.area = m.max_area
ORDER BY c.region;

-- 5. Países con más de 100 millones de habitantes
SELECT name_common, population
FROM countries
WHERE population > 100000000
ORDER BY population DESC;