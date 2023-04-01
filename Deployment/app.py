
# move into app.py directory using cd and run app.py (flask run) in the terminal test

from flask import Flask, render_template, request, redirect, url_for, flash

from objects.route import route
from objects.station import station
from objects.user import user
from objects.admin import admin
from objects.trainSchedule import trainSchedule
from objects.train import train

# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
curAdmin = admin(None, None, None, None)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def req_login():
    
    if request.method == 'POST':
        username = request.form.get('user-name')
        password = request.form.get('user-password')

        valid = curAdmin.login(username,password)
        if valid:
            print('login successful')
            return render_template('admin-home.html')
        else:
            print('login failed')
            return render_template('login.html', info='Invalid Info')
    
    return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('user-name')
        password = request.form.get('user-password')
        userkey = request.form.get('user-key')
        #password2 = request.form.get('user-password2')

        if len(password) < 6:
            flash('Password must be at least 6 characters long', category='error')
            #return render_template('signup.html', info='Password must be at least 6 characters long')
        elif not any(char.isupper() for char in password):
            flash('Password must have at least one upper case letter', category='error')
            #return render_template('signup.html', info='Password must have at least one upper case letter')
        elif not any(char.isdigit() for char in password):
            flash('Password must have at least one digit', category='error')
            #return render_template('signup.html', info='Password must have at least one digit')
        elif not any(char in '!@#$%^&*' for char in password):
            flash('Password must have at least one special character', category='error')
            #return render_template('signup.html', info='Password must have at least one special character')
        else:
            valid = curAdmin.register(username,password, userkey)
            if valid:
                flash('Account created sucessfully', category='success')
            else:
                flash('Unable to creat account', category='error')

    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)
