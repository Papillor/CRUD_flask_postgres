from flask import render_template, request, redirect, url_for
from app import app
from app.__init__ import cur, conn

@app.route('/')
def index():
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    return render_template('index.html', books=books)