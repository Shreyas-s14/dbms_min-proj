-- Creating the database:
CREATE database mini_proj_408;
-- Creating the tables:
CREATE TABLE LEAGUE_408(
league_id INT NOT NULL,
league_name VARCHAR(20) NOT NULL,
--league_level INT NOT NULL,
No_players INT NOT NULL,
lvl_req INT NOT NULL,
PRIMARY KEY(league_id)
);
CREATE TABLE GAME_SESSION_408(
session_id INT NOT NULL,
start_time TIME NOT NULL,
No_players INT NOT NULL,
server_region VARCHAR(20) NOT NULL,
PRIMARY KEY(session_id)
);

CREATE TABLE CLAN_408(
clan_id INT NOT NULL,
no_members INT NOT NULL,
lvl_req INT NOT NULL,
PRIMARY KEY(clan_id)
);
--PLAYER ENTITY
CREATE TABLE PLAYER_408(
player_id INT NOT NULL,
username VARCHAR(20) NOT NULL,
clan_id INT NOT NULL,
league_id INT NOT NULL,
session_id INT NOT NULL,
PRIMARY KEY(player_id),
FOREIGN KEY(clan_id) REFERENCES CLAN_408(clan_id),
FOREIGN KEY(league_id) REFERENCES LEAGUE_408(league_id),
FOREIGN KEY(session_id) REFERENCES GAME_SESSION_408(session_id)
);

--SKILLS ENTITY
CREATE TABLE SKILLS_408(
    player_id INT NOT NULL,
    level INT NOT NULL,
    coins INT NOT NULL,
    FOREIGN KEY(player_id) REFERENCES PLAYER_408(player_id)
);
-- Progress Entity
CREATE TABLE PROGRESS_408(
    player_id INT NOT NULL,
    --session_id INT NOT NULL,
    trophies INT NOT NULL,
    exp INT ,    
    FOREIGN KEY(player_id) REFERENCES PLAYER_408(player_id)
);



-- test:
CREATE TABLE attack_408(
    player_id INT NOT NULL,
    session_id INT NOT NULL,
    player2_id INT NOT NULL,
    XP INT NOT NULL,
    FOREIGN KEY(player_id) REFERENCES PLAYER_408(player_id),

    FOREIGN KEY(session_id) REFERENCES GAME_SESSION_408(session_id),
    FOREIGN KEY(player2_id) REFERENCES PLAYER_408(player_id)

);






