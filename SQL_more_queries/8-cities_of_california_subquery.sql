--
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND state.name = 'California'
ORDER BY cities.id ASC;

