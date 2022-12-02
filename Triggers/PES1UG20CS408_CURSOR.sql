--
DROP PROCEDURE IF EXISTS update_trophies;
DELIMITER $$
CREATE PROCEDURE update_trophies(IN uname VARCHAR(20), IN new_trophies INT)
BEGIN
    DECLARE cont INT default 0;
    DECLARE pid INT;
    DECLARE C1 CURSOR FOR SELECT player_408.player_id FROM player_408 WHERE player_408.username=uname;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET cont = 1;
    -- SELECT player_408.player_id FROM player_408;

    OPEN C1;
    l1: LOOP
        FETCH C1 INTO pid;
        if cont=1 THEN
            leave l1;
        end if;
        -- select C1;
        select pid;
        UPDATE progress_408 SET trophies=new_trophies WHERE player_id = pid;
    END LOOP l1;
    CLOSE C1;
END $$
DELIMITER ;

call update_trophies('jesse', 999);