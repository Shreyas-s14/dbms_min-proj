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

--3)
SELECT SKILLS_408.coins , skills_408.level, player_408.username FROM skills_408 
INNER JOIN player_408 ON skills_408.player_id = player_408.player_id
intersect
SELECT SKILLS_408.coins , skills_408.level, player_408.username FROM skills_408
INNER JOIN player_408 ON skills_408.player_id = player_408.player_id
WHERE skills_408.level = 10;

--4) UNION ALL:
SELECT player_408.username, player_408.player_id FROM player_408
UNION ALL
SELECT player_408.username, player_408.player_id FROM player_408
WHERE player_408.player_id = 70;