-- Create a function to get player with equivalent level and league but not same clan
DROP PROCEDURE IF EXISTS players_below_trophy;
DELIMITER $$

CREATE PROCEDURE players_below_trophy(IN trophymax INT)
BEGIN
SELECT player_408.player_id,player_408.username, progress_408.trophies FROM player_408 JOIN 
progress_408 ON player_408.player_id=progress_408.player_id WHERE progress_408.trophies<=400 
ORDER BY progress_408.trophies DESC;
END $$
DELIMITER ;


