-- GET AVG NO OF TROPHIES FOR EACH PLAYER BELONGING TO A CLAN
select avg(trophies) from PROGRESS_408 where player_id in (select player_id from PLAYER_408 where clan_id = 23456);

-- get count of players in a clan
select count(player_id) from PLAYER_408 where clan_id = 23458;

-- sum of all trophies in a clan
select sum(trophies) from PROGRESS_408 where player_id in (select player_id from PLAYER_408 where clan_id = 23458);

-- max coins in a view of league and clan
select max(coins) from SKILLS_408 where player_id in (select player_id from PLAYER_408 where clan_id in (select clan_id from CLAN_408 where lvl_req = 10));
