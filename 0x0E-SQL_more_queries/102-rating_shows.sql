-- lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT `tv_shows`.`title` AS `title`, SUM(`tv_show_ratings`.`rate`)
AS `rating`
FROM `tv_show_ratings`
INNER JOIN `tv_shows`
ON  `tv_shows`.`id` = `tv_show_ratings`.`show_id`
GROUP BY `tv_shows`.`title`
ORDER BY SUM(`tv_show_ratings`.`rate`) DESC;
