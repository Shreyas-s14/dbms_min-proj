import streamlit as st
import mysql.connector
from database import view_all_players, view_one_player
import plotly.express as px
import pandas as pd

def read():
    st.subheader("Read")
    st.write("View all players")
    result = view_all_players()
    df=pd.DataFrame(result,columns=['player_id','username','clan_id','league_id','session_id'])
    # st.write(result)
    # st.write("View one player")
    # player_id = st.number_input("Enter player_id")
    # result = view_one_player(player_id)
    # st.write(result)
    with st.expander("View all players"):
        st.dataframe