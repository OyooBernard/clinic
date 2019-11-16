from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
import re
app = Flask(__name__)


# Enter your database connection details below
# Enter your database connection details below
mysql = pymysql.connect(host='localhost',
                             user='root',
                             password='password',
                             db='clinic_dev',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Intialize MySQL
app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def home():
    if 'user' in session:
        # User is loggedin show them the home page
        return render_template('index.html', username=session['user']['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # user = request.form['email']
        # password = request.form['password']
        session['user'] = request.form
        # session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('auth/login.html')


if(__name__) == '__main__':
    app.run(debug=True)
