from flask import Flask
from flask import render_template
from flask import jsonify
import sqlite3
import json

app = Flask(__name__)

# db
connection = sqlite3.connect("db.db")
cursor = connection.cursor()

cursor.execute('SELECT * FROM Courier')
couriers = cursor.fetchall()
connection.close()

@app.route('/')
def hello_world():
    return "Hello, World!"

def getCouriers():
    couriers_list = []
    for courier in couriers:
        print(courier)

        couriers_dict = {
            'FIO': courier[0],
            'ID': courier[1],
            'Rating': courier[2]
        }

        couriers_list.append(couriers_dict)

    return couriers_list



@app.route('/couriers')
def loadMenu():
    return jsonify(getCouriers())

if __name__ == "__main__":
    app.run()
