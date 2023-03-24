<<<<<<< HEAD:Deployment/app.py
# move into app.py directory using cd and run app.py (flask run) in the terminal test
=======
# move into app.py directory using cd and run app.py (flask run) in the terminal

>>>>>>> c4368f4f6d94479b5128118f8d82f8fc515c7692:Backend/Deployment/app.py
from flask import Flask, render_template
from objects import admin
# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def register():
    return render_template('adminLogin.html')
    

  


if __name__ == "main":
    app.run(host='0.0.0.0', port=30006, debug=True)



