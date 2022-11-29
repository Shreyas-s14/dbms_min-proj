-- USE CURSOR TO UPDATE THE RECORDS IN THE TABLE
DROP PROCEDURE IF EXISTS update_trophies;
DELIMITER $$
CREATE PROCEDURE update_trophies(IN username VARCHAR(20), IN trophies INT)
BEGIN
DECLARE player_id INT;
DECLARE C1 CURSOR FOR SELECT player_id FROM player_408 WHERE username = username;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET player_id = 0;
OPEN C1;
FETCH C1 INTO player_id;
IF player_id = 70 THEN
INSERT INTO player_408(username) VALUES(username);
SET player_id = LAST_INSERT_ID();
END IF;
UPDATE progress_408 SET trophies = trophies WHERE player_id = player_id;
CLOSE C1;
END $$
