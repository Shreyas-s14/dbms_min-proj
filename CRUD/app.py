import streamlit as st
import pandas as pd
from create import create_player,create_clan
from read import read
from update import update_player,update_clan
from delete import delete_player,delete_clan
from database import general_query

def main():
    st.title("Game Database")
    menu = ["Add Player", "Add Clan","Read", "Update Player", "Update Clan", "Delete Player","Delete Clan","CLI"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Add Player":
        st.subheader("Add Player")
        create_player()
    elif choice == "Add Clan":
        st.subheader("Add Clan")
        create_clan()
    elif choice == "Read":
        read()
    elif choice == "Update Player":
        update_player()
    elif choice == "Update Clan":
        update_clan()
    elif choice == "Delete Player":
        delete_player()
    elif choice == "Delete Clan":
        delete_clan()
    elif choice == "CLI":
        q = st.text_input("Query Input")
        if st.button("Execute"):
            res = general_query(q)
            st.dataframe(res)
    else:
        st.subheader("ERROR")

if __name__=='__main__':
    main()
