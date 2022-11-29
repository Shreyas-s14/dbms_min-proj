-- Set operations: DO LATER

--1) Union of people based in India and Europe
(Select player_408.username,game_session_408.server_region
FROM player_408
INNER JOIN game_session_408
ON player_408.session_id = game_session_408.session_id
WHERE game_session_408.server_region = 'India')
UNION
(Select player_408.username,game_session_408.server_region
FROM player_408
INNER JOIN game_session_408
ON player_408.session_id = game_session_408.session_id
WHERE game_session_408.server_region = 'Europe');

--2) List of players not in a particular clan
Select player_408.username, clan_408.clan_id FROM player_408,clan_408
WHERE player_408.clan_id = clan_408.clan_id
EXCEPT
Select player_408.username, clan_408.clan_id FROM player_408,clan_408
WHERE player_408.clan_id = clan_408.clan_id AND clan_408.clan_id = 242747;

--2) Use the intersect operator to find the players who are in the same clan as the player with username 'pekka'
Select player_408.username, clan_408.clan_id FROM player_408,clan_408
WHERE player_408.clan_id = clan_408.clan_id 
MINUS
Select player_408.username, clan_408.clan_id FROM player_408,clan_408
WHERE player_408.clan_id = clan_408.clan_id AND player_408.username = 'maniac';


SELECT player_408.username from player_408 where player_408.player_id=