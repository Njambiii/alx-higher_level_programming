--  list all genres not linked to the show Dexter
SELECT DISTINCT `tv_genres`.`name` AS `name`
FROM `tv_show_genres`
INNER JOIN `tv_genres`
ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
WHERE `tv_show_genres`.`genre_id` NOT IN
(
SELECT`tv_show_genres`.`genre_id`
FROM `tv_show_genres`
INNER JOIN `tv_shows`
ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
INNER JOIN `tv_genres`
ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
WHERE `tv_shows`.`title` = 'Dexter'
)
ORDER BY `tv_genres`.`name` ASC;
