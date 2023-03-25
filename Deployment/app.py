
# move into app.py directory using cd and run app.py (flask run) in the terminal test

from flask import Flask, render_template
from objects import *
# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def register():
    return render_template('adminLogin.html')
    

  


if __name__ == "main":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)



