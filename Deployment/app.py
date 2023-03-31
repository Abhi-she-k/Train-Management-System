
# move into app.py directory using cd and run app.py (flask run) in the terminal test

from flask import Flask, render_template, request, redirect, url_for
from objects import *
# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def req_login():
    #data = request.form
    #print(data)
    
    userName = request.form.get('user-name')
    password = request.form.get('user-password')

    print(userName)
    print(password)
    
    #success = admin.login(userName, password)
    #print(success)
    #if success:
    #  print('login successful')
      #return render_template('admin-home.html')
    #else:
    #    print('login failed')
      #return render_template('login.html', info='Invalid Info')
    return render_template('login.html')

    
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        userName = request.form.get('user-name')
        password1 = request.form.get('user-password1')
        password2 = request.form.get('user-password2')

    if len(password) < 6:
        return render_template('signup.html', info='Password must be at least 6 characters long')
    elif not any(char.isupper() for char in password):
        return render_template('signup.html', info='Password must have at least one upper case letter')
    elif not any(char.isdigit() for char in password):
        return render_template('signup.html', info='Password must have at least one digit')
    elif not any(char in '!@#$%^&*' for char in password):
        return render_template('signup.html', info='Password must have at least one special character')
    else:
        return render_template('admin-home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)
