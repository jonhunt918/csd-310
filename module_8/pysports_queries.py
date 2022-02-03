import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host () with database {}" .format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_denied_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
    
cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")
cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

teams = cursor.fetchall()
player = cursor.fetchall()

print("\n -- DISPLAYING TEAM RECORDS -- ")

for team in teams:
    print("Team ID: {}\n Team Name: {}\n Mascot {}\n".format(team[0], team[1], team[2]))

print("\n -- DISPLAYING PLAYER RECORDS -- ")

for player in player:
    print("Player ID: {}\n First Name {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))
