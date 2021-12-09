import sqlite3
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


def connect_db():
    conn = sqlite3.connect('data.sqlite')
    return conn

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

#home
@app.route('/', methods = ['GET', 'POST'])
def home():
    conn = connect_db()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("SELECT * FROM User")
    Users = cur.fetchall()

    cur.execute("SELECT * FROM Armor")
    Armors = cur.fetchall()

    cur.execute("SELECT * FROM Bungie")
    Devs = cur.fetchall()

    cur.execute("SELECT * FROM Character")
    Chars = cur.fetchall()

    cur.execute("SELECT * FROM GameActivities")
    GAs = cur.fetchall()

    cur.execute("SELECT * FROM DLC ORDER BY DLC.order_r")
    DLCs = cur.fetchall()

    return render_template('home.html', Users = Users, Armors = Armors, Devs = Devs, Chars = Chars, GAs = GAs, DLCs = DLCs)

#query section
@app.route('/query', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def start_query():
    if request.method == 'POST':
        if(request.form['i_button'] == 'Insert'):
            conn = connect_db()
            cur = conn.cursor()
            myT = request.form['i_table']
            myV = request.form['i_val']
            cur.execute("INSERT INTO {0} VALUES ({1})".format(myT, myV))
            conn.commit()
            #print ('successful commit')
            return render_template('query.html')

        elif(request.form['i_button'] == 'Delete'):
            conn = connect_db()
            cur = conn.cursor()
            myT = request.form['d_table']
            myQ = request.form['d_query']
            cur.execute('DELETE FROM {0} WHERE {1}'.format(myT, myQ))
            conn.commit()
            #print ('successful commit')
            return render_template('query.html')

        elif(request.form['i_button'] == 'Select'):
            conn = connect_db()
            cur = conn.cursor()
            myV = request.form['s_val']
            myT = request.form['s_table']
            myQ = request.form['s_query']
            cur.execute('SELECT {0} FROM {1} WHERE {2}'.format(myV, myT, myQ))
            myOut = cur.fetchall()
            
            #print (myV + " " + myT + " " + myQ)
            #print (myOut)
            #print ('successful commit')
            return render_template('query.html', myOut = myOut)

        elif(request.form['i_button'] == 'Update'):
            conn = connect_db()
            cur = conn.cursor()
            myT = request.form['u_table']
            myV = request.form['u_val']
            myQ = request.form['u_query']
            cur.execute('UPDATE {0} SET {1} WHERE {2}'.format(myT, myV, myQ))
            conn.commit()
            #print ('successful commit')
            return render_template('query.html')
    else:
        return render_template('query.html')


#presets section
@app.route('/preset', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def preset():
    if request.method == 'POST':
        #select
        if(request.form['pre'] == 's1'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('SELECT DISTINCT Character.id, Armor.name FROM Character, Armor, User, DLC WHERE Armor.class = Character.class and User.id = Character.userID and User.dlcOwned >= DLC.order_r and Armor.season = DLC.season')
            pOut = cur.fetchall()
            return render_template('preset.html', pOut = pOut)

        elif(request.form['pre'] == 's2'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("SELECT Bungie.id, GameActivities.name FROM Bungie, DLC, GameActivities WHERE DLC.campaign = Bungie.season and DLC.campaign = GameActivities.dlc and DLC.season = 'Season of the Lost'")
            pOut = cur.fetchall()
            return render_template('preset.html', pOut = pOut)

        elif(request.form['pre'] == 's3'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("SELECT Armor.name, Armor.slot FROM Armor WHERE Armor.subclass = 'Void'")
            pOut = cur.fetchall()
            return render_template('preset.html', pOut = pOut)

        elif(request.form['pre'] == 's4'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute('SELECT User.id, count(Character.id) FROM User, Character WHERE User.id = Character.userID GROUP BY User.id HAVING count(Character.id) > 1')
            pOut = cur.fetchall()
            return render_template('preset.html', pOut = pOut)
               
                
        #update
        elif(request.form['pre'] == 'u1'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("UPDATE Character SET class = 'Titan' WHERE Character.id = 'Exo2'")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'u2'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("UPDATE Bungie SET vendor = 'Drifter', season = 'Forsaken' WHERE Bungie.id = 'Dev2'")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'u3'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("UPDATE Armor SET ornament = 'True' WHERE Armor.name = 'Omnioculus'")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'u4'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("UPDATE User SET status = 'Banned' WHERE User.id = 'Player#0001'")
            conn.commit()
            return render_template('preset.html')


        #insert
        elif(request.form['pre'] == 'i1'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO User VALUES ('Player#0002', 'Asia', '7', 'Clear')")
            conn.commit()
            return render_template('preset.html')
        
        elif(request.form['pre'] == 'i2'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO Bungie VALUES ('Dev4', 'Brother Vance', 'Curse of Osiris')")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'i3'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO GameActivities VALUES ('Eater of Worlds', 'Raid', 'Curse of Osiris', 'Season of the Curse of Osiris')")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'i4'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO Character VALUES ('Human2', 'Titan', 'Arc', 'Player#0001')")
            conn.commit()
            return render_template('preset.html')

        
        #delete
        elif(request.form['pre'] == 'd1'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("DELETE FROM GameActivities WHERE GameActivities.name = 'Lost Lost Sectors'")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'd2'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("DELETE FROM DLC WHERE DLC.order_r = '1'")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'd3'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("DELETE FROM Character WHERE userID in (SELECT User.id FROM User WHERE User.status = 'Banned')")
            conn.commit()
            return render_template('preset.html')

        elif(request.form['pre'] == 'd4'):
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("DELETE FROM Armor WHERE Armor.season = 'Season of the Red War'")
            conn.commit()
            return render_template('preset.html')

    return render_template('preset.html')

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app
