-- GET AVG NO OF TROPHIES FOR EACH PLAYER BELONGING TO A CLAN
select avg(trophies) from PROGRESS_408 where player_id in (select player_id from PLAYER_408 where clan_id = 23456);

-- get count of players in a clan
select count(player_id) from PLAYER_408 where clan_id = 23458;