# allows end users to create a new record in the database for a table of their choice
#table: player_408
import streamlit as st
import mysql.connector
from database import add_data
import sys

def create():
    col1,col2=st.columns(2)
    with col1:
        player_id=st.number_input("Enter player_id")
        username=st.text_input("Enter username")
    with col2:
        clan_id=st.number_input("Enter clan_id")
        league_id=st.number_input("Enter league_id")
        session_id=st.number_input("Enter session_id")
    if st.button("Add"):
        add_data(player_id,username,clan_id,league_id,session_id)
        st.success(f"Data added successfully: {player_id},{username},{clan_id},{league_id},{session_id}")       
