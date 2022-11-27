#importing all the required libraries
import streamlit as st
import plotly.express as px
import mysql.connector
#user defined: make py files for each
from create import create
from read import read
from update import update
from delete import delete

#connecting to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mini_proj_408"
)
c=mydb.cursor()

#main:
def main():
    st.title("Mini Project")
    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Create":
        st.subheader("Create")
        create()
    elif choice == "Read":
        read()
    elif choice == "Update":
        update()
    elif choice == "Delete":
        delete()
    else:
        st.subheader("Thank you:")

if __name__=='__main__':
    main()            