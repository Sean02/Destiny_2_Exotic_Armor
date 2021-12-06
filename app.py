import sqlite3
from flask import Flask, request, jsonify 
from flask_cors import CORS 

def connect_db():
    conn = sqlite3.connect('data.sqlite')
    return conn


#armor func
def insert_armor(armor):
    new_armor = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Armor VALUES (?,?,?,?,?,?)", 
                armor['name'], armor['class'], armor['subclass'], 
                armor['season'], armor['ornament'], armor['slot'])
        conn.commit()
        new_armor = get_armor_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    return new_armor
    
def get_armors():
    armors = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Armor")
        rows = cur.fetchall()

        for i in rows:
            armor = {}
            armor["armor_id"] = i["armor_id"]
            armor["name"] = i["name"]
            armor["class"] = i["class"]
            armor["subclass"] = i["subclass"]
            armor["season"] = i["season"]
            armor["ornament"] = i["ornament"]
            armor["slot"] = i["slot"]
            armors.append(armor)
    except:
        armors = []
    return armors

def get_armor_by_id(armor_id):
    armor = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Armor WHERE armor_id = ?", (armor_id,))
        row = cur.fetchone()

        armor["armor_id"] = row["armor_id"]
        armor["name"] = row["name"]
        armor["class"] = row["class"]
        armor["subclass"] = row["subclass"]
        armor["season"] = row["season"]
        armor["ornament"] = row["ornament"]
        armor["slot"] = row["slot"]
    except:
        armor = {}

    return armor

def update_armors(armor):
    updated_armor = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Armor SET name = ?, class = ?, subclass = ?, season = ?, ornament = ?, slot = ? WHERE armor_id = ?",
                (armor["name"], armor["class"], armor["subclass"], 
                armor["season"], armor["ornament"], armor["slot"], armor["armor_id"],))
        conn.commit()
        updated_armor = get_armor_by_id(armor["armor_id"])
    except:
        conn.rollback()
        updated_armor = {}
    finally:
        conn.close()
    return updated_armor

def delete_armors(armor_id):
    msg = {}
    try:
        conn = connect_db()
        conn.execute("DELETE FROM Armor WHERE armor_id = ?", (armor_id,))
        conn.commit() 
        msg["status"] = "Armor deleted successfully"   
    except:
        conn.rollback()
        msg["status"] = "Cannot delete armor"
    finally:
        conn.close()
    return msg



#dev func
def insert_dev(dev):
    new_dev = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Bungie (id, vendor, season) VALUES (?, ?, ?)", (dev['id'], dev['vendor'], dev['season']))
        conn.commit()
        new_dev = get_dev_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    
    return new_dev

def get_devs():
    dev = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Bungie")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            Dev_s = {}
            Dev_s["dev_id"] = i["dev_id"]
            Dev_s["id"] = i["id"]
            Dev_s["vendor"] = i["vendor"]
            Dev_s["season"] = i["season"]
            dev.append(Dev_s)

    except:
        dev = []

    return dev

def get_dev_by_id(dev_id):
    dev = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Bungie WHERE dev_id = ?", (dev_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        dev["dev_id"] = row["dev_id"]
        dev["id"] = row["id"]
        dev["vendor"] = row["vendor"]
        dev["season"] = row["season"]
    except:
        dev = {}

    return dev

def update_dev(dev):
    updated_Dev = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Bungie SET id = ?, vendor = ?, season = ? WHERE dev_id = ?",  
        (dev["id"], dev["vendor"], dev["season"], dev["dev_id"],))
        conn.commit()
        #return the user
        updated_Dev = get_dev_by_id(dev["dev_id"])

    except:
        conn.rollback()
        updated_Dev = {}
    finally:
        conn.close()

    return updated_Dev

def delete_dev(dev_id):
    msg = {}
    try:
        conn = connect_db()
        conn.execute("DELETE FROM Bungie WHERE dev_id = ?", (dev_id,))
        conn.commit() 
        msg["status"] = "Dev deleted successfully"   
    except:
        conn.rollback()
        msg["status"] = "Cannot delete dev"
    finally:
        conn.close()
    return msg



#char func
def insert_char(char):
    new_char = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Character VALUES (?,?,?,?)", 
                char['id'], char['class'], char['subclass'], 
                char['userID'])
        conn.commit()
        new_char = get_char_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    return new_char

def get_chars():
    chars = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Character")
        rows = cur.fetchall()

        for i in rows:
            char = {}
            char["char_id"] = i["char_id"]
            char["id"] = i["id"]
            char["class"] = i["class"]
            char["subclass"] = i["subclass"]
            char["userID"] = i["userID"]
            chars.append(char)
    except:
        chars = []
    return chars

def get_char_by_id(char_id):
    char = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Character WHERE char_id = ?", (char_id,))
        row = cur.fetchone()

        char["char_id"] = row["char_id"]
        char["id"] = row["id"]
        char["class"] = row["class"]
        char["subclass"] = row["subclass"]
        char["userID"] = row["userID"]

    except:
        char = {}

    return char

def update_chars(char):
    updated_char = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Character SET id = ?, class = ?, subclass = ?, userID = ? WHERE char_id = ?",
                (char["id"], char["class"], char["subclass"], 
                char["userID"], char["char_id"],))
        conn.commit()
        updated_char = get_char_by_id(char["char_id"])
    except:
        conn.rollback()
        updated_char = {}
    finally:
        conn.close()
    return updated_char

def delete_chars(char_id):
    msg = {}
    try:
        conn = connect_db()
        conn.execute("DELETE FROM Character WHERE char_id = ?", (char_id,))
        conn.commit() 
        msg["status"] = "Character deleted successfully"   
    except:
        conn.rollback()
        msg["status"] = "Cannot delete char"
    finally:
        conn.close()
    return msg



#users func
def insert_user(User):
    inserted_users = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO User (id, region, dlcOwned, status) VALUES (?, ?, ?, ?)", (User['id'], User['region'], User['dlcOwned'], User['status']))
        conn.comit()
        inserted_users = get_user_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    
    return inserted_users

def get_user():
    users = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM User")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            user = {}
            user["user_id"] = i["user_id"]
            user["id"] = i["id"]
            user["region"] = i["region"]
            user["dlcOwned"] = i["dlcOwned"]
            user["status"] = i["status"]
            users.append(user)

    except:
        users = []

    return users

def get_user_by_id(user_id):
    users = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM User WHERE user_id = ?", (user_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        users["user_id"] = row["user_id"]
        users["id"] = row["id"]
        users["region"] = row["region"]
        users["dlcOwned"] = row["dlcOwned"]
        users["status"] = row["status"]
    except:
        users = {}

    return users

def update_user(User):
    updated_User = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE User SET id = ?, region = ?, dlcOwned = ?, status = ? WHERE user_id = ?", (User["id"], User["region"], User["dlcOwned"], User["status"], User["user_id"],))
        conn.commit()
        #return the user
        updated_User = get_user_by_id(User["user_id"])

    except:
        conn.rollback()
        updated_User = {}
    finally:
        conn.close()

    return updated_User

def delete_user(user_id):
    message = {}
    try:
        conn = connect_db()
        conn.execute("DELETE from User WHERE user_id = ?", (user_id,))
        conn.commit()
        message["status"] = "User deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete user"
    finally:
        conn.close()

    return message



#Gameactivities func
def insert_GameActivites(GameActivities):
    inserted_GameActivities = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO GameActivities (name, type, dlc, season) VALUES (?, ?, ?, ?)", (GameActivities['name'], GameActivities['type'], GameActivities['dlc'], GameActivities['season']))
        conn.comit()
        inserted_GameActivities = get_GA_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    
    return inserted_GameActivities

def get_GameActivites():
    GA = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM GameActivities")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            GameActivites = {}
            GameActivites["GA_id"] = i["GA_id"]
            GameActivites["name"] = i["name"]
            GameActivites["type"] = i["type"]
            GameActivites["dlc"] = i["dlc"]
            GameActivites["season"] = i["season"]
            GA.append(GameActivites)

    except:
        GA = []

    return GA

def get_GA_by_id(GA_id):
    GA = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM GameActivities WHERE GA_id = ?", (GA_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        GA["GA_id"] = row["GA_id"]
        GA["name"] = row["name"]
        GA["type"] = row["type"]
        GA["dlc"] = row["dlc"]
        GA["season"] = row["season"]
    except:
        GA = {}

    return GA

def update_GameActivites(GameActivities):
    updated_GA = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE GameActivites SET name = ?, type = ?, dlc = ?, season = ? WHERE GA_id =?",  (GameActivities["name"], GameActivities["type"], GameActivities["dlc"], GameActivities["season"], GameActivities["GA_id"],))
        conn.commit()
        #return the user
        updated_GA = get_GA_by_id(GameActivities["GA_id"])

    except:
        conn.rollback()
        updated_GA = {}
    finally:
        conn.close()

    return updated_GA

def delete_GameActivites(GA_id):
    message = {}
    try:
        conn = connect_db()
        conn.execute("DELETE from GameActivities WHERE GA_id = ?", (GA_id,))
        conn.commit()
        message["status"] = "GA deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete GA"
    finally:
        conn.close()

    return message



#DLC func
def insert_DLC(DLC):
    inserted_DLC = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO DLC (season, seasonpass, subclass, order_r, campaign) VALUES (?, ?, ?, ?, ?)", (DLC['season'], DLC['seasonpass'], DLC['subclass'], DLC['order_r'], DLC['campaign']))
        conn.comit()
        inserted_DLC = get_DLC_by_id(cur.lastrowid)
    except:
        conn().rollback()
    finally:
        conn.close()
    
    return inserted_DLC

def get_DLC():
    DLCs = []
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM DLC")
        rows = cur.fetchall()

        # convert row objects to dictionary
        for i in rows:
            DLC = {}
            DLC["DLC_id"] = i["DLC_id"]
            DLC["season"] = i["season"]
            DLC["seasonpass"] = i["seasonpass"]
            DLC["subclass"] = i["subclass"]
            DLC["order_r"] = i["order_r"]
            DLC["campaign"] = i["country"]
            DLCs.append(DLC)

    except:
        DLCs = []

    return DLCs

def get_DLC_by_id(DLC_id):
    DLCs = {}
    try:
        conn = connect_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM DLC WHERE DLC_id = ?", (DLC_id,))
        row = cur.fetchone()

        # convert row object to dictionary
        DLCs["DLC_id"] = row["DLC_id"]
        DLCs["season"] = row["season"]
        DLCs["seasonpass"] = row["seasonpass"]
        DLCs["subclass"] = row["subclass"]
        DLCs["order_r"] = row["order_r"]
        DLCs["campaign"] = row["campaign"]
    except:
        DLCs = {}

    return DLCs

def update_DLC(DLC):
    updated_DLC = {}
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE DLC SET season = ?, seasonpass = ?, subclass = ?, order_r = ?, campaign = ? WHERE DLC_id =?", (DLC["season"], DLC["seasonpass"], DLC["subclass"], DLC["order_r"], DLC["campaign"], DLC["DLC_id"],))
        conn.commit()
        #return the user
        updated_DLC = get_DLC_by_id(DLC["DLC_id"])

    except:
        conn.rollback()
        updated_DLC = {}
    finally:
        conn.close()

    return updated_DLC

def delete_DLC(DLC_id):
    message = {}
    try:
        conn = connect_db()
        conn.execute("DELETE from DLC WHERE DLC_id = ?", (DLC_id,))
        conn.commit()
        message["status"] = "DLC deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete DLC"
    finally:
        conn.close()

    return message



app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#armor Flask
@app.route('/api/armors', methods=['GET'])
def api_get_armors():
    return jsonify(get_armors())

@app.route('/api/armors/<armor_id>', methods=['GET'])
def api_get_armor(armor_id):
    return jsonify(get_armor_by_id(armor_id))

@app.route('/api/armors/add',  methods = ['POST'])
def api_add_armor():
    armor = request.get_json()
    return jsonify(insert_armor(armor))

@app.route('/api/armors/update',  methods = ['PUT'])
def api_update_armor():
    armor = request.get_json()
    return jsonify(update_armors(armor))

@app.route('/api/armors/delete/<armor_id>',  methods = ['DELETE'])
def api_delete_armor(armor_id):
    return jsonify(delete_armors(armor_id))



#dev Flask
@app.route('/api/devs', methods=['GET'])
def api_get_devs():
    return jsonify(get_devs())

@app.route('/api/devs/<dev_id>', methods=['GET'])
def api_get_dev(dev_id):
    return jsonify(get_dev_by_id(dev_id))

@app.route('/api/devs/add',  methods = ['POST'])
def api_add_dev():
    dev = request.get_json()
    return jsonify(insert_dev(dev))

@app.route('/api/devs/update',  methods = ['PUT'])
def api_update_dev():
    dev = request.get_json()
    return jsonify(update_dev(dev))

@app.route('/api/devs/delete/<dev_id>',  methods = ['DELETE'])
def api_delete_dev(dev_id):
    return jsonify(delete_dev(dev_id))



#char
@app.route('/api/chars', methods=['GET'])
def api_get_chars():
    return jsonify(get_chars())

@app.route('/api/chars/<char_id>', methods=['GET'])
def api_get_char(char_id):
    return jsonify(get_char_by_id(char_id))

@app.route('/api/chars/add',  methods = ['POST'])
def api_add_char():
    char = request.get_json()
    return jsonify(insert_char(char))

@app.route('/api/chars/update',  methods = ['PUT'])
def api_update_char():
    char = request.get_json()
    return jsonify(update_chars(char))

@app.route('/api/chars/delete/<char_id>',  methods = ['DELETE'])
def api_delete_char(char_id):
    return jsonify(delete_chars(char_id))



#users Flask
@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_user())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add',  methods = ['POST'])
def api_add_user():
    User = request.get_json()
    return jsonify(insert_user(User))

@app.route('/api/users/update',  methods = ['PUT'])
def api_update_user():
    User = request.get_json()
    return jsonify(update_user(User))

@app.route('/api/users/delete/<user_id>',  methods = ['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))



#GameActivities Flask
@app.route('/api/GameActivities', methods=['GET'])
def api_get_GameActivities():
    return jsonify(get_GameActivites())

@app.route('/api/GameActivities/<GA_id>', methods=['GET'])
def api_get_GameActivity(GA_id):
    return jsonify(get_GA_by_id(GA_id))

@app.route('/api/GameActivities/add',  methods = ['POST'])
def api_add_GameActivities():
    GameActivities = request.get_json()
    return jsonify(insert_GameActivites(GameActivities))

@app.route('/api/GameActivities/update',  methods = ['PUT'])
def api_update_GameActivities():
    GameActivities = request.get_json()
    return jsonify(update_GameActivites(GameActivities))

@app.route('/api/GameActivities/delete/<GA_id>',  methods = ['DELETE'])
def api_delete_GameActivities(GA_id):
    return jsonify(delete_user(GA_id))



#DLC Flask
@app.route('/api/DLC', methods=['GET'])
def api_get_DLCs():
    return jsonify(get_DLC())

@app.route('/api/DLC/<DLC_id>', methods=['GET'])
def api_get_DLC(DLC_id):
    return jsonify(get_DLC_by_id(DLC_id))

@app.route('/api/DLC/add',  methods = ['POST'])
def api_add_DLC():
    DLC = request.get_json()
    return jsonify(insert_DLC(DLC))

@app.route('/api/DLC/update',  methods = ['PUT'])
def api_update_DLC():
    DLC = request.get_json()
    return jsonify(update_DLC(DLC))

@app.route('/api/DLC/delete/<DLC_id>',  methods = ['DELETE'])
def api_delete_DLC(DLC_id):
    return jsonify(delete_user(DLC_id))


if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app
