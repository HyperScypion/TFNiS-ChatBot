from flask import Flask
from flask import Flask, flash, redirect, render_template
from flask import request, session, abort
from sqlalchemy.orm import sessionmaker
from database.make_database import Users
import os

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['username'] != '':
        session['logged_in'] = True
        Session = sessionmaker()
        Session.configure(bind='sqlite///bot.db')
        session_db = Session()
        user = Users(id=1, nick=request.form['username'])
        session_db.add(user)
        print(user)
        return 'chat'
    else:
        return home()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

# @app.route('/chat')
# def chat():


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
