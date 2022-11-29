import streamlit as st
import mysql.connector
from database import *
from func import cname_hash

def create_player():
    col1,col2=st.columns(2)
    with col1:
        username=st.text_input("Username")
        clan_name=st.text_input("Clan Name")
        region=st.text_input("Region")
    with col2:
        level = st.number_input("Level", value = 8, min_value = 0)
        trophies = st.number_input("Trophies", min_value = 0)
        exp = st.number_input("Xp", min_value = 0)
        coins = st.number_input("Coins", min_value = 0)

    player_id = cname_hash(username)
    clan_id = cname_hash(clan_name)
    if st.button("Add"):
        if username == "":
            st.error("Name cannot be empty")
        elif clan_name == "":
            st.error("Clan name cannot be empty")
        elif region == "":
            st.error("Region cannot be empty")
        else:
            try:
                session_id = assign_session(region)
                league_id = map_level_leagueid(level)
                add_player(player_id,username,clan_id,league_id,session_id, trophies, exp, coins, level)
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    st.error("Player already exists")
                if err.errno == 1452:
                    st.error("Clan doesn't exist")
            except TypeError:
                st.error("Region doesn't exist")
            else:
                st.success("Player added successfully")

def create_clan():
    col1,col2=st.columns(2)
    with col1:
        clan_name=st.text_input("Clan Name")
        clan_id = cname_hash(clan_name)
    with col2:
        level = st.number_input("Level Requirement", min_value = 0, format = "%d")
    if st.button("Add"):
        if clan_name == "":
            st.error("Name cannot be empty")
        else:
            try:
                add_clan(clan_id, level)
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    st.error("Clan already exists")
                if err.errno == 1644:
                    st.error(err)
            else:
                st.success("Clan added successfully (Clan ID = "+str(clan_id)+")")
