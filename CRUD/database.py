import mysql.connector
from mysql.connector import errorcode
import streamlit
import plotly

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mini_proj_408"
)
c = mydb.cursor()
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS player_408 (player_id INT ,username varchar(50),clan_id INT, league_id INT, session_id INT)")

def add_data(player_id,username,clan_id,league_id,session_id):
    c.execute("INSERT INTO player_408 (player_id,username,clan_id,league_id,session_id) VALUES (%s,%s,%s,%s,%s)",(player_id,username,clan_id,league_id,session_id))
    mydb.commit()

def view_all_players():
    c.execute("SELECT * FROM player_408")
    data = c.fetchall()
    return data

def view_one_player(player_id):
    c.execute("SELECT * FROM player_408 WHERE player_id = %s", (player_id,))
    data = c.fetchall()
    return data

def edit_details(player_id,username,clan_id,league_id,session_id):
    c.execute("UPDATE player_408 SET username = %s, clan_id = %s, league_id = %s, session_id = %s WHERE player_id = %s", (username,clan_id,league_id,session_id,player_id))
    mydb.commit()
    data=c.fetchall()
    return data

def delete_player(player_id):
    c.execute("DELETE FROM player_408 WHERE player_id = %s", (player_id,))
    mydb.commit()


