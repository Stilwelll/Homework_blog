from app import app
from flask import render_template

@app.route('/')
def index():
    title = 'Home'
    return render_template('index.html', title=title)

@app.route('/favorite5')
def favorite5():
    title = 'Favorite 5'
    return render_template('favorite5.html', title=title)

