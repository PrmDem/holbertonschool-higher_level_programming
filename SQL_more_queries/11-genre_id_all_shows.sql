-- lists all show titles + genre id
-- if there is no genre, displays 'null'

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
