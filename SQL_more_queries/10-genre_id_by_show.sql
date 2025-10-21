-- for shows with at least one genre:
-- lists titles and genre ids from hbtn_0d_tvshows db

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title ASC;
