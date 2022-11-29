import streamlit as st
import mysql.connector
from database import *
from func import cname_hash


def update_player():
    username=st.text_input("Username")
    player_id = cname_hash(username)
    if username != "":
        res = fetch_player(player_id)
    else:
        res = (0,0,0)
    exp=st.text_input("EXP", value = res[0])
    trophies=st.text_input("Trophies", value = res[1])
    coins=st.text_input("Coins", value = res[2])
    if st.button("Update"):
        if username == "":
            st.error("Name cannot be empty")
        else:
            try:
                updt_player(player_id,exp,coins,trophies)
            except ValueError:
                st.error("No changes were made")
            else:
                st.success("Player updated successfully")

def update_clan():
        clan_name=st.text_input("Clan Name")
        clan_id = cname_hash(clan_name)
        if clan_name != "":
            res = fetch_clan(clan_id)
        else:
            res = ""
        lvl_req=st.text_input("Level Requirement", value = res)
        if st.button("Update"):
            if clan_name == "":
                st.error("Name cannot be empty")
            else:
                try:
                    updt_clan(clan_id, lvl_req)
                except ValueError:
                    st.error("No changes were made")
                else:
                    st.success("Player updated successfully")
