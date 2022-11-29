import mysql.connector
from database import fetch_player
from func import cname_hash

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="miniproj_144"
)
c = mydb.cursor()


if __name__ == "__main__":
    print(fetch_player(cname_hash("kkk")))
