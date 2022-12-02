-- Inser trigger for player_408 to check for level requirement of clan and league
-- drop trigger if exists player_408_lvl_req_check;
-- create trigger player_408_lvl_req_check
-- before insert on PLAYER_408
-- for each row
-- begin
-- if ( (select lvl_req from CLAN_408 where clan_id = new.clan_id) > (select level from SKILLS_408 where player_id = new.player_id) ) then
--     signal sqlstate '45000' set message_text = 'Player level is not high enough to join clan';
-- end if;
-- if ( (select lvl_req from LEAGUE_408 where league_id = new.league_id) > (select level from SKILLS_408 where player_id = new.player_id) ) then
--     signal sqlstate '45000' set message_text = 'Player level is not high enough to join league';
-- end if;
-- end;

-- Update trigger for player_408 to check for level requirement of clan and league
drop trigger if exists player_408_lvl_req_check_update;
delimiter //
create trigger player_408_lvl_req_check_update
before update on PLAYER_408
for each row
begin
if ( (select lvl_req from CLAN_408 where clan_id = new.clan_id) > (select level from SKILLS_408 where player_id = new.player_id) ) then
    signal sqlstate '45000' set message_text = 'Player level is not high enough to join clan';
end if;
if ( (select lvl_req from LEAGUE_408 where league_id = new.league_id) > (select level from SKILLS_408 where player_id = new.player_id) ) then
    signal sqlstate '45000' set message_text = 'Player level is not high enough to join league';
end if;
end//
delimiter ;
