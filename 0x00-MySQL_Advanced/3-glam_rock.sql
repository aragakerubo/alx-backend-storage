SELECT band_name,
ABS(SUBSTRING_INDEX(lifespan, ' - ', 1) - SUBSTRING_INDEX(lifespan, ' - ', -1))
AS lifespan
FROM bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
