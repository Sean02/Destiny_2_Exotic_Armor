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

    cur.execute("SELECT * FROM DLC")
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
@app.route('/preset')
def preset():
    return render_template('preset.html')

if __name__ == "__main__":
    #app.debug = True
    #app.run(debug=True)
    app.run() #run app
