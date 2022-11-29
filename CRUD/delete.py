import streamlit as st
import mysql.connector
from database import remove_player, remove_clan
from func import cname_hash

def delete_player():
    username=st.text_input("Username")
    if st.button("Delete"):
        if username == "":
            st.error("Name cannot be empty")
        else:
            try:
                remove_player(cname_hash(username))
            except ValueError:
                st.error("Player does not exist")
            else:
                st.success("Player removed")

def delete_clan():
    clan_name=st.text_input("Clan Name")
    if st.button("Delete"):
        if clan_name == "":
            st.error("Name cannot be empty")
        else:
            try:
                remove_clan(cname_hash(clan_name))
            except mysql.connector.Error as err:
                if err.errno == 1451:
                    st.error("Clan still has members")
            except ValueError:
                st.error("Clan does not exist")
            else:
                st.success("Deleted clan successfully")
