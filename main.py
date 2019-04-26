from flask import Flask
from flask import Flask, flash, redirect, render_template
from flask import request, session, abort
from sqlalchemy import create_engine, select
from sqlalchemy.sql import text
from database.make_database import Users
import os

app = Flask(__name__)

from bot.brain import Brain

brain = Brain()
model = brain.load_model()
corpus, dictionary = brain.create_corpus(save=True)
brain.fit_LDA(corpus, 40)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return chat()


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['username'] != '':
        session['logged_in'] = True
        query = "SELECT * FROM users;"
        engine = create_engine('sqlite:///bot.db', echo=True)
        connection = engine.connect()
        result = connection.execute(query)
        print(result)
        return chat()
    else:
        return home()


@app.route('/logout')
def logout():
    session['logged_in'] = False
    return home()

app.route('/chat')
def chat():     
    return render_template('chat.html')



@app.route('/process',methods=['POST'])
def process():
	user_input=request.form['user_input']

	bot_response=brain.predict(str(user_input), dictionary, False)
	print("ChatBot: " + bot_response)
	return render_template('chat.html', user_input=user_input,
		bot_response=bot_response
)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
