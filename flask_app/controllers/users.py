from flask_app import app
from flask_app.models.user import User
from flask import render_template, request, redirect, session
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login_reqister():
    return render_template('index.html')

@app.route('/dash')
def home():
    return render_template('home.html')

@app.route('/register', methods = ["POST"])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)

    data = {
        "first_name": request.form['first_name'], 
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
        "password": pw_hash
    }

    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/dash')

