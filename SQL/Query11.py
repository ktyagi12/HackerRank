#Problem available at: https://www.hackerrank.com/challenges/weather-observation-station-6/problem
SELECT DISTINCT CITY from STATION where substr(CITY,1,1) in ('a','e','i','o','u');