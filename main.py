from flask import Flask
from flask import render_template
from flask import jsonify
import sqlite3
import json
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, supports_credentials=True, resources={r"/boardGames": {"origins": "http://localhost:5000"}})

@app.route('/')
def hello_world():
    return "available links:\n /orders\n  /boardGames\n /owners /renters /boardGamesInCirculation /addBoardGame /addOrder /createOwner /createRenter /addBoardGameInCirculation /filterOrders"



def find_all_orders():
    # db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Order_info')
    allOrders = cursor.fetchall()
    connection.close()

    allOrders_list = []

    for order in allOrders:
        # print(owner)
        allOrders_dict = {
            'ID': order[0],
            'Status': order[1],
            'Order_time': order[2],
            'Addres_recive': order[3],
            'Addres_send': order[4],
            'ID_renter': order[5],
            'ID_boardgame': order[6],
            'ID_owner': order[7],
            'ID_courier': order[8],
        }
        allOrders_list.append(allOrders_dict)

    return allOrders_list


@app.route('/orders')
@cross_origin(supports_credentials=True, origin='http://localhost:5000', headers=['Content- Type', 'Authorization'])
def loadOrders():
    response = jsonify(find_all_orders())
    print(response.headers)
    return response

def find_all_boardgames():
    # db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Boardgame')
    allBoardgames = cursor.fetchall()
    connection.close()

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


def find_all_renters():
    # db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Renter')
    allRenters = cursor.fetchall()
    connection.close()

    allRenters_list = []

    for renter in allRenters:
        # print(owner)
        allRenters_dict = {
            'FIO': renter[0],
            'ID': renter[1],
            'rating': renter[2]
        }
        allRenters_list.append(allRenters_dict)

    return allRenters_list


@app.route('/renters')
@cross_origin(supports_credentials=True, origin='http://localhost:5000', headers=['Content- Type', 'Authorization'])
def loadRenters():
    response = jsonify(find_all_renters())
    print(response.headers)
    return response


def find_all_bgic():
    # db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Boardgame_in_circulation, Boardgame WHERE Boardgame_in_circulation.ID_boardgame = Boardgame.ID')
    bgins = cursor.fetchall()
    connection.close()

    allbgic_list = []

    for bgic in bgins:
        bgic_dict = {
            # ID_Renter, ID_Boardgame, ID_Owner, Status_boardgame, Boardgame_state
            'ID_Renter': bgic[0],
            'ID_Boardgame': bgic[1],
            'ID_Owner': bgic[2],
            'Status_boardgame': bgic[3],
            'Boardgame_state': bgic[4],
            'ID': bgic[5],
            'Status': bgic[6],
            'Name': bgic[7],
            'Description': bgic[8],
            'Middle_game_time': bgic[9],
            'Min_players': bgic[10],
            'Max_players': bgic[11],
            'Age': bgic[12],
            'Rools': bgic[13],
            'Image': bgic[14],
            'Rating': bgic[15],
            'Price_per_day': bgic[16],
            'Base_cost': bgic[17],
            'Complexity': bgic[18],
            'Category': bgic[19]
        }
        allbgic_list.append(bgic_dict)

    return allbgic_list


@app.route('/boardGamesInCirculation')
@cross_origin(supports_credentials=True, origin='http://localhost:5000', headers=['Content- Type', 'Authorization'])
def loadbgincs():
    response = jsonify(find_all_bgic())
    print(response.headers)
    return response


@app.route('/boardGames')
@cross_origin(supports_credentials=True, origin='http://localhost:5000', headers=['Content- Type', 'Authorization'])
def loadMenu():
    response = jsonify(find_all_boardgames())
    print(response.headers)
    return response


def find_all_owner():
    # db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Owner')
    allOwners = cursor.fetchall()
    connection.close()

    allOwners_list = []

    for owner in allOwners:
        # print(owner)
        allOwners_dict = {
            'FIO': owner[0],
            'ID': owner[1],
            'rating': owner[2]
        }
        allOwners_list.append(allOwners_dict)

    return allOwners_list


@app.route('/owners')
@cross_origin(supports_credentials=True, origin='http://localhost:5000', headers=['Content- Type', 'Authorization'])
def loadOwners():
    response = jsonify(find_all_owner())
    print(response.headers)
    return response

# args - name; des; url; complexity; category; price
# /addBoardGame?username=321&password=123
# /addBoardGame?Name=penis&Description=228&Image=http&Complexity=hard&Category=adult&Price=20
@app.route('/addBoardGame', methods=['GET', 'POST'])
def getData():
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT Count(*) FROM Boardgame')
    data = cursor.fetchall()
    connection.close()
    # get ID for new board using database

    ID = data[0][0]
    print(ID)
    Name = request.args.get('Name')
    Description = request.args.get('Description')
    Image = request.args.get('Image')
    Complexity = request.args.get('Complexity')
    Category = request.args.get('Category')
    Price = request.args.get('Price')

    # save to db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO BoardGame (ID, Name, Status, Description, Middle_game_time, Min_players, Max_players, Age, Rools, Image, Rating, Price_per_day, Base_cost, Complexity, Category) VALUES (?, ?, "0", ?, "0", "0", "0", "0", "0", ?, "0", ?, "0", ?, ?)' , (ID, Name, Description, Image, Price, Complexity, Category))
    except:
        connection.close()
        return "not ok"

    connection.commit()
    connection.close()

    print(Name, Description, Image, Complexity, Category, Price)

    return "ok"
@app.route('/createOwner', methods=['GET', 'POST'])
def createOwner():
    ID = request.args.get('ID')
    Name = request.args.get('Name')

    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO Owner (FIO, ID, Rating) VALUES (?, ?, "0")', (Name, ID))
    except:
        connection.close()
        return "not ok"

    connection.commit()
    connection.close()

    return "ok"

# ID_Owner; ID_boardgame
@app.route('/addBoardGameInCirculation', methods=['GET', 'POST'])
def addBoardGmaeInCirculation():
    ID_Boardgame = request.args.get('ID_Boardgame')
    ID_Owner = request.args.get('ID_Owner')

    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    try:
      cursor.execute('INSERT INTO Boardgame_in_circulation (ID_Renter, ID_Boardgame, ID_Owner, Status_boardgame, Boardgame_state) VALUES ("0", ?, ?, "0", "0")', (ID_Boardgame, ID_Owner))
    except:
        connection.close()
        return "not ok"

    connection.commit()
    connection.close()

    return "ok"

@app.route('/createRenter', methods=['GET', 'POST'])
def createRenter():
    ID = request.args.get("ID")
    Name = request.args.get('Name')

    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    try:
        cursor.execute('INSERT INTO Renter (FIO, ID, Rating) VALUES (?, ?, "0")', (Name, ID))
    except:
        connection.close()
        return "not ok"

    connection.commit()
    connection.close()

    return "ok"

# Order info: ID; Adress_recive; Order_time; ID_renter; ID_boardgame; ID_owner
@app.route('/addOrder', methods=['GET', 'POST'])
def getOrderData():
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    cursor.execute('SELECT Count(*) FROM Order_info')
    data = cursor.fetchall()
    connection.close()
    # get ID for new board using database

    ID = data[0][0]
    print(ID)

    Order_time = request.args.get('Order_time')
    Adress_recive = request.args.get('Adress_recive')
    ID_renter = request.args.get('ID_renter')
    ID_boardgame = request.args.get('ID_boardgame')
    ID_owner = request.args.get('ID_owner')

    # save to db
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO Order_info (ID, Status, Order_time, Addres_recive, Addres_send, ID_renter, ID_boardgame, ID_owner, ID_courier) VALUES (?, "0", ?, ?, "0", ?, ?, ?, "0")' , (ID, Order_time, Adress_recive, ID_renter, ID_boardgame, ID_owner))
    except:
        connection.close()
        return "not ok"

    connection.commit()
    connection.close()

    return "ok"

@app.route('/filterOrders', methods=['GET', 'POST'])
def filterOrders():
    connection = sqlite3.connect("db.db")
    cursor = connection.cursor()
    ID = request.args.get('ID')

    # try:
    # ID_boardgame(boardgame) ; ID_renter(renter)
    cursor.execute('SELECT * FROM Order_info INNER JOIN Boardgame ON Order_info.ID_boardgame == Boardgame.ID where Order_info.ID_owner == ?', (ID))
    # except:
    #     connection.close()
    #     return "not ok"

    allFilteredOrders = cursor.fetchall()
    connection.close()

    allFilteredOrders_list = []

    for filteredOrder in allFilteredOrders:
        # print(owner)
        allFilteredOrders_dict = {
            'ID': filteredOrder[0],
            'Status': filteredOrder[1],
            'Order_time': filteredOrder[2],
            'Addres_recive': filteredOrder[3],
            'Addres_send': filteredOrder[4],
            'ID_renter': filteredOrder[5],
            'ID_boardgame': filteredOrder[6],
            'ID_owner': filteredOrder[7],
            'ID_courier': filteredOrder[8],
            'ID': filteredOrder[9],
            'Status': filteredOrder[10],
            'Name': filteredOrder[11],
            'Description': filteredOrder[12],
            'Middle_game_time': filteredOrder[13],
            'Min_players': filteredOrder[14],
            'Max_players': filteredOrder[15],
            'Age': filteredOrder[16],
            'Rools': filteredOrder[17],
            'Image': filteredOrder[18],
            'Rating': filteredOrder[19],
            'Price_per_day': filteredOrder[20],
            'Base_cost': filteredOrder[21],
            'Complexity': filteredOrder[22],
            'Category': filteredOrder[23],
        }
        allFilteredOrders_list.append(allFilteredOrders_dict)

    return allFilteredOrders_list

# @app.route('/finish_order', methods=['GET', 'POST'])
# def finish_order():
#     connection = sqlite3.connect("db.db")
#     cursor = connection.cursor()
#     ID = request.args.get('ID')
#     connection.commit()
#     cursor.execute('UPDATE Order_info SET Status = "1" WHERE Order_info.ID == ?', (ID))
#
#     return "OK"

if __name__ == "__main__":
    app.run()

