
# move into app.py directory using cd and run app.py (flask run) in the terminal test

from flask import Flask, render_template
from objects import *
# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/login', methods=['POST','GET'])
def req_login():
    userName = request.form['username']
    password = request.form['password']
    
    success = login(userName, password)
    if success:
      return render_template('admin-home.html')
    else:
      return render_template('login.html',info='Invalid Info')
    
@app.route('/signup', methods=['POST','GET'])
def sign_up():
    userName = request.form['username']
    password = request.form['password']

    
  


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)



