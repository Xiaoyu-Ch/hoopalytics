import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), '../data/nba.sqlite')

db = sqlite3.connect(db_path)

cursor1 = db.cursor()
cursor2 = db.cursor()

cursor1.execute("SELECT * FROM game;")
cursor2.execute("SELECT * FROM draft_combine_stats;")

game_data = cursor1.fetchall()
combine_data = cursor2.fetchall()

print(game_data)
print(combine_data)

