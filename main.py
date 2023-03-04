
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db
import sqlite3


main = Blueprint('main', __name__)

def conexion():
    
    conn=sqlite3.connect("PERFIL EMPRESA SA")
    conn.row_factory = sqlite3.Row
    return conn

@main.route('/') 
def index():
    return render_template('index.html')

@main.route('/profile') 
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


app = create_app() 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 
