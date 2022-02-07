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

    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player INNER JOIN team ON player.team_id = team.team_id")

    player = cursor.fetchall()

    print("\n -- DISPLAYING PLAYER RECORDS -- ")

    for player in player:
        print("\n\n Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}".format(player[0], player[1], player[2], player[3]))

    input("\n Press any key to continue... ")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_denied_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
