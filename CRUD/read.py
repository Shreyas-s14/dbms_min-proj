import streamlit as st
import mysql.connector
from database import view_all_players,get_clan_info,get_league_info
import pandas as pd

def read():
    st.subheader("Read")
    with st.expander("View all players"):
        df=pd.DataFrame(view_all_players(),columns=['Username','League','Level','Trophies','Experience','Coins','Server Region'])
        df['Server Region'] = df['Server Region'].apply(lambda x: x.title())
        st.dataframe(df)
    with st.expander("Clan Information"):
        df=pd.DataFrame(get_clan_info(),columns=['Clan ID','Number of members','Level Requirement','Average Trophies','Average Experience','Average Level','Total Coins'])
        st.dataframe(df)
    with st.expander("League Information"):
        df=pd.DataFrame(get_league_info(),columns=['League', 'Number of Players', 'Level Requirement'])
        st.dataframe(df)
