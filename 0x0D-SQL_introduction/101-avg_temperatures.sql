-- script that displays the average temperature (Fahrenheit) by city ordered by temperatur

SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
