import mysql.connector
from mysql.connector import errorcode
import streamlit
import plotly
from func import cname_hash
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mini_proj_408"
)
c = mydb.cursor(buffered=True)

#CREATE-------------------------------------------------------------------------
def map_level_leagueid(level):
    c.execute("SELECT league_id FROM league_408 WHERE lvl_req <= %s ORDER BY lvl_req DESC", (level,))
    return int(c.fetchone()[0])

def assign_session(region):
    c.execute("SELECT session_id FROM game_session_408 WHERE server_region = %s ORDER BY no_players ASC", (region.lower(),))
    return int(c.fetchone()[0])

def add_player(player_id,username,clan_id,league_id,session_id, trophies, exp, coins, level):
    c.execute("INSERT INTO player_408 (player_id,username,clan_id,league_id,session_id) VALUES (%s,%s,%s,%s,%s)",(player_id,username,clan_id,league_id,session_id))
    c.execute("INSERT INTO skills_408 (player_id,level, coins) VALUES (%s,%s,%s)",(player_id,level,coins))
    c.execute("INSERT INTO progress_408 (player_id,trophies, exp) VALUES (%s,%s,%s)",(player_id,trophies,exp))
    c.execute("UPDATE clan_408 SET no_members = no_members + 1 WHERE clan_id = %s", (clan_id,))
    c.execute("UPDATE game_session_408 SET No_players = No_players + 1 WHERE session_id = %s", (session_id,))
    mydb.commit()

def add_clan(clan_id, lvl_req):
    c.execute("INSERT INTO clan_408 (clan_id,no_members,lvl_req) VALUES (%s,%s,%s)", (clan_id,1,lvl_req))
    mydb.commit()

#READ---------------------------------------------------------------------------
def view_all_players():
    c.execute("""
SELECT player_408.username, league_408.league_name, skills_408.level, progress_408.trophies, progress_408.exp, skills_408.coins, game_session_408.server_region FROM player_408
INNER JOIN progress_408 ON progress_408.player_id = player_408.player_id
INNER JOIN skills_408 ON skills_408.player_id = player_408.player_id
INNER JOIN game_session_408 ON game_session_408.session_id = player_408.session_id
INNER JOIN league_408 ON league_408.league_id = player_408.league_id;
""")
    return c.fetchall()

def get_clan_info():
    c.execute("""
SELECT v1.clan_id, v1.no_members, v1.lvl_req, v1.trophies, v1.exp, v2.level, v2.coins FROM
(SELECT player_408.clan_id, clan_408.no_members, clan_408.lvl_req, AVG(progress_408.trophies) AS trophies, AVG(progress_408.exp) AS exp
FROM player_408
INNER JOIN progress_408 ON progress_408.player_id = player_408.player_id
INNER JOIN clan_408 ON clan_408.clan_id = player_408.clan_id
GROUP BY clan_408.clan_id) v1
INNER JOIN
(SELECT player_408.clan_id, AVG(skills_408.level) AS level, SUM(skills_408.coins) AS coins
FROM player_408
INNER JOIN skills_408 ON skills_408.player_id = player_408.player_id
INNER JOIN clan_408 ON clan_408.clan_id = player_408.clan_id
GROUP BY clan_408.clan_id) v2
ON v1.clan_id = v2.clan_id;
""")
    return c.fetchall()

def get_league_info():
    c.execute("SELECT league_name, No_players, lvl_req FROM league_408 ORDER BY lvl_req");
    return c.fetchall()

#UPDATE-------------------------------------------------------------------------
def fetch_player(player_id):
    c.execute(f"""SELECT progress_408.exp, progress_408.trophies, skills_408.coins FROM progress_408
INNER JOIN skills_408 ON progress_408.player_id = skills_408.player_id
WHERE progress_408.player_id = {player_id}
""")
    if(c.rowcount == 0):
        return ("","","")
    else:
        return c.fetchone()

def updt_player(player_id, exp, coins, trophies):
    query = "UPDATE progress_408 SET"
    start = 1
    if exp != "":
        query += f" exp = {exp}"
        start = 0
    if trophies != "":
        if start == 0:
            query += ","
        query += f" trophies = {trophies}"
    query += f" WHERE player_id = {player_id}"
    c.execute(query)
    if(c.rowcount == 0):
        raise ValueError("Empty response")
    if coins != "":
        c.execute(f"UPDATE skills_408 SET coins = {coins} WHERE player_id = {player_id}")
        if(c.rowcount == 0):
            raise ValueError("Empty response")
    mydb.commit()

def fetch_clan(clan_id):
    c.execute(f"SELECT lvl_req FROM clan_408 WHERE clan_id = {clan_id}")
    if(c.rowcount == 0):
        return ""
    else:
        return c.fetchone()[0]

def updt_clan(clan_id, lvl_req):
    c.execute(f"UPDATE clan_408 SET lvl_req = {lvl_req} WHERE clan_id = {clan_id}")
    if(c.rowcount == 0):
        return ValueError
    mydb.commit()

#DELETE-------------------------------------------------------------------------
def remove_player(player_id):
    c.execute("UPDATE clan_408 SET no_members = no_members - 1 WHERE clan_id = (SELECT clan_id from player_408 WHERE player_id = %s)", (player_id,))
    if(c.rowcount == 0):
        raise ValueError("Empty response")
    c.execute("UPDATE game_session_408 SET No_players = No_players - 1 WHERE session_id = (SELECT session_id from player_408 WHERE player_id = %s)", (player_id,))

    c.execute("DELETE FROM skills_408 WHERE player_id = %s",(player_id,))
    c.execute("DELETE FROM progress_408 WHERE player_id = %s",(player_id,))
    c.execute("DELETE FROM player_408 WHERE player_id = %s",(player_id,))
    mydb.commit()

def remove_clan(clan_id):
    c.execute("DELETE FROM clan_408 WHERE clan_id = %s",(clan_id,))
    if(c.rowcount == 0):
        raise ValueError("Empty response")
        return
    mydb.commit()


#GPQ----------------------------------------------------------------------------
def general_query(query):
    c.execute(query)
    if(c.rowcount != 0):
        res = c.fetchall()
        field_names = [i[0] for i in c.description]
        df = pd.DataFrame(res, columns = field_names)
        return df
    else:
        return "Query Successful"
