SELECT origin, COUNT(*) AS nb_fans
FROM bands
JOIN fans ON bands.id = fans.band_id
GROUP BY origin
ORDER BY nb_fans DESC;
