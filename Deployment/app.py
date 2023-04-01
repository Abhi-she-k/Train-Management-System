
import json
# move into app.py directory using cd and run app.py (flask run) in the terminal test
from flask import Flask, render_template, request, redirect, url_for, flash

from objects.route import route
from objects.station import station
from objects.user import user
from objects.admin import admin
from objects.trainSchedule import trainSchedule
from objects.train import train
#from objects.createObjects import createObjects

# template = os.path.abspath('~/public/Frontend/templates')
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
curAdmin = admin(None, None, None, None)
systemObjects = []

def createObjects():
  with open('objects/trainSchedule.json', 'r') as f:
    data = json.load(f)

  for system in data['systems']:
    
    systemId = system['id']
    scheduleObject = trainSchedule(systemId)
    
    for t in system['trains']:
        name = t['id']
        route1 = t['route']
        r = route()
        for i in range(len(route1)):
          stat = station(i, route1[i])
          r.addStation(stat)
        times = t['times']
        depart = t['depart']
      
        trainObject = train(name, r, times, depart)
        scheduleObject.trains.append(trainObject) 
    systemObjects.append(scheduleObject)

createObjects()

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
            #flash('Logged in Successfully', category='success')
            return render_template('admin-home.html')
        else:
            flash('Invalid Information', category='error')
    
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
                flash('Account created sucessfully. Redirecting to login in 3 seconds...', category='success')
                return render_template('signup.html'), {"Refresh": "3; url=/login"}

            else:
                flash('Unable to create account', category='error')

    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/find_route', methods=['GET', 'POST'])
def route():
    if request.method == 'POST':
        startStation = request.form.get('start-station')
        endStation = request.form.get('end-station')

        stations = []
        for i in systemObjects:
            x = (i.findRoute(startStation.strip(), endStation.strip()))
            if x != []:
                stations.append(x)

        # info = {}
        # for i in stations:
        #     for j in i:
        #         info[j.getName()] = j.getSchedules()

        info = {"brand": "Ford", "model": "Mustang", "year": 1964}
        return render_template('find_route.html', info=info)
        
        # s = stations[0][0].getSchedules()

        # for key, value in s.items():
        #     print(key, value)

        # for i, j in s:
        #     print(i, j)

        #stations[0].printTrain()
        
    return render_template('find_route.html')

@app.route('/schedules')
def schedules():
    return render_template('schedules.html')

@app.route('/eta')
def eta():
    return render_template('eta.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)
