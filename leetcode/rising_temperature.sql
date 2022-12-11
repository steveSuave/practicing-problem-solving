-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
-- Table: Weather

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the primary key for this table.
-- This table contains information about the temperature on a certain day.

SELECT
    w.id
FROM
    Weather w
WHERE
    w.temperature > (
        SELECT
            i.temperature
        FROM
            Weather i
        WHERE
            i.recordDate = w.recordDate - INTERVAL 1 DAY);
