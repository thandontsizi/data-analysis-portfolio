-- Netflix Content Analysis Queries:

-- 1. Content Type Distribution:
SELECT
	type,
	COUNT(*) AS total_titles
FROM netflix_titles_cleaned
GROUP BY type
ORDER BY total_titles DESC;


-- 2. Top Countries:
SELECT
	country,
	COUNT(*) AS total_titles
FROM netflix_titles_cleaned
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;


-- 3. Content Per Year:
SELECT
	EXTRACT(YEAR FROM date_added) AS year_added,
	COUNT(*) AS total_titles
FROM netflix_titles_cleaned
WHERE date_added IS NOT NULL
GROUP BY year_added
ORDER BY year_added;


-- 4. Top Genres:
SELECT
	TRIM(genre) AS genre,
	COUNT(*) AS total_titles
FROM netflix_titles_cleaned,
LATERAL unnest(string_to_array(listed_in, ',')) AS genre
GROUP BY TRIM(genre)
ORDER BY total_titles DESC
LIMIT 10;


-- 5. Trend By Type:
SELECT
	EXTRACT(YEAR FROM date_added) AS year_added,
	type,
	COUNT(*) AS total_titles
FROM netflix_titles_cleaned
WHERE date_added IS NOT NULL
GROUP BY year_added, type
ORDER BY year_added, type;
