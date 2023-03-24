# move into app.py directory using cd and run app.py (flask run) in the terminal

from flask import Flask, render_template
import os
# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == "main":
    app.run(host='0.0.0.0', port=30006, debug=True)



