from flask import Flask, render_template, request, redirect
import conn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        #fetch all user data
        resultDetails = request.form
        user_name = resultDetails['user_name']
        user_email = resultDetails['user_email']
        conn.myCursor.execute("INSERT INTO tbl_users (user_name, user_email) VALUES(%s, %s)", (user_name, user_email))
        conn.myDb.commit()
        return redirect('/users')
    return render_template('home.html')

@app.route('/users')
def users():
    conn.myCursor.execute("SELECT * FROM tbl_users")
    userDetails = conn.myCursor.fetchall()
    return render_template('users.html', userDetails = userDetails)

@app.route('/delete/<user_id>')
def deleteUser(user_id):
    conn.myCursor.execute("DELETE FROM tbl_users WHERE user_id = " + user_id)
    conn.myDb.commit()
    return redirect('/users')

@app.route('/truncate')
def truncate():
    conn.myCursor.execute("TRUNCATE TABLE tbl_users")
    conn.myDb.commit()
    return render_template('truncate.html')

if __name__ == "__main__":
    app.run(debug = True)