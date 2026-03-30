from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from models import db, User, Credential

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(username=username, password=password.decode('utf-8'))
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.checkpw(request.form['password'].encode('utf-8'), user.password.encode('utf-8')):
            session['user_id'] = user.id
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        cred = Credential(site=request.form['site'],
                          username=request.form['username'],
                          password=request.form['password'],
                          user_id=session['user_id'])
        db.session.add(cred)
        db.session.commit()
    creds = Credential.query.filter_by(user_id=session['user_id']).all()
    return render_template('dashboard.html', creds=creds)

if __name__ == '__main__':
    app.run(debug=True)
