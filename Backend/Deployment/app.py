from flask import Flask, render_template
import os



# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == "main":
    app.run()



