import streamlit as st
import mysql.connector
from database import remove_player, remove_clan
from func import cname_hash

def delete_player():
    # username=st.text_input("Username")
    player_id=st.number_input("Player ID")
    if st.button("Delete"):
        if player_id == 0:
            st.error("ID cannot be empty")
        else:
            try:
                remove_player(player_id)
            except ValueError:
                st.error("Player does not exist")
            else:
                st.success("Player removed")

def delete_clan():
    #clan_name=st.text_input("Clan Name")
    clan_id=st.number_input("Clan ID")
    if st.button("Delete"):
        if clan_id == 0:
            st.error("ID cannot be empty")
        else:
            try:
                remove_clan(clan_id)
            except mysql.connector.Error as err:
                if err.errno == 1451:
                    st.error("Clan still has members")
            except ValueError:
                st.error("Clan does not exist")
            else:
                st.success("Deleted clan successfully")
