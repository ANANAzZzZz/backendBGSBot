from flask import Flask
from flask import render_template
from flask import jsonify
import sqlite3
import json

app = Flask(__name__)

# db
connection = sqlite3.connect("db.db")
cursor = connection.cursor()

cursor.execute('SELECT * FROM Boardgame')
allBoardgames = cursor.fetchall()
connection.close()

@app.route('/')
def hello_world():
    return "Hello, World!"

count = 0
def find_all_boardgames():
    allBoardgames_list = []

    for boardgame in allBoardgames:
        print(boardgame)
        allBoardgames_dict = {
            'ID': boardgame[0],
            'Status': boardgame[1],
            'Name': boardgame[2],
            'Description': boardgame[3],
            'Middle_game_time': boardgame[4],
            'Min_players': boardgame[5],
            'Max_players': boardgame[6],
            'Age': boardgame[7],
            'Rools': boardgame[8],
            'Image': boardgame[9],
            'Rating': boardgame[10],
            'Price_per_day': boardgame[11],
            'Base_cost': boardgame[12],
            'Complexity': boardgame[13],
            'Category': boardgame[14],
        }
        allBoardgames_list.append(allBoardgames_dict)

    return allBoardgames_list

@app.route('/boardGames')
def loadMenu():
    return jsonify(find_all_boardgames())

if __name__ == "__main__":
    app.run()
