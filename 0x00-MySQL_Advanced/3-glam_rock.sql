-- SELECT band_name, (IFNULL(split, YEAR(CURRENT_DATE())) - formed) AS lifespan
-- Lists all bands with Glam rock as their main style, ranked by their longevity.
-- Column names must be: band_name & lifespan

SELECT band_name, ifnull(split, 2022)-ifnull(formed, 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC
