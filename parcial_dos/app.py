from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL

app = Flask(__name__)

#my sql-mariadb connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = '221-3-pii'

mysql = MySQL(app)

#settings
app.secret_key = "myKey"

@app.route("/")
def index():
    return "Hello, running flask for pii univa class with luis guerra as professor, students: natasha torres and jorge vasquez"

@app.route("/about/")
def aboutUs():
    return render_template("about.html")

@app.route("/services/")
def services():
    return render_template("services.html")

@app.route("/nosotros/")
def nosotros():
    return redirect(url_for("aboutUs"))

@app.route("/users_list/")
def users_list():
    myCursor = mysql.connection.cursor()
    myCursor.execute('SELECT * FROM login')
    data = myCursor.fetchall()
    myCursor.close()
    return render_template('users_list.html', data = data)

@app.route("/users_insert/")
def users_insert():
    return render_template('users_insert.html')

@app.route("/users_update/<id>", methods = ['POST', 'GET'])
def users_update(id):
    myCursor = mysql.connection.cursor()
    sqlQuery = f"SELECT * FROM login WHERE id = {id}"
    myCursor.execute(sqlQuery)
    data = myCursor.fetchall()
    myCursor.close()
    print(data[0])
    return render_template('users_update.html', user = data[0])

@app.route("/insert_user/", methods=['POST'])
def insert_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        mycursor = mysql.connection.cursor()
        mycursor.execute("INSERT INTO login (email, password) VALUES (%s, %s)", (email, password))
        mysql.connection.commit()
        mycursor.close()
        print("Value inserted")
        return redirect(url_for('users_list'))

@app.route("/update_user/<id>", methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        email = request.form['email']
        status = request.form['status']
        sqlQuery = f"UPDATE login SET status = {status} WHERE id = {id}"
        mycursor = mysql.connection.cursor()
        mycursor.execute(sqlQuery)
        mysql.connection.commit()
        mycursor.close()
        return redirect(url_for('users_list'))

if __name__ == "__main__":
    app.run(port=5500, debug=True)