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
        return render_template('index.html')

@app.route('/', methods=['POST'])
def chat():     
    user_input = request.form.get('textbox')
    bot_response=brain.predict(str(user_input), dictionary, False)
    print("ChatBot: " + bot_response)
    return render_template('index.html', textbox=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
