
import json
# move into app.py directory using cd and run app.py (flask run) in the terminal test
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta

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
systemObjects = []
pathTrainSchedule = 'objects/trainSchedule.json'
pathAdminInfo = 'objects/adminInfo.json'

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
def login():
    numSystems = len(systemObjects)

    if request.method == 'POST':
        
        username = request.form.get('user-name')
        password = request.form.get('user-password')

        valid = curAdmin.login(username,password)
        if valid:
            info = {}
    
            for i in systemObjects:
                stations = {}
                for j in i.getTrains():
                    stations[j.getName()] = j.getSchedules()
                info[i.getScheduleId()] = stations
            
            return render_template('admin_home.html', user=username, password=password, systems=numSystems, info=info)
        else:
            flash('Invalid Information', category='error')
    
    return render_template('login.html')
    
@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('user-name')
        password1 = request.form.get('user-password1')
        password2 = request.form.get('user-password2')
        userkey = request.form.get('user-key')

        if len(password1) < 6:
            flash('Password must be at least 6 characters long', category='error')
        elif not any(char.isupper() for char in password1):
            flash('Password must have at least one upper case letter', category='error')
        elif not any(char.isdigit() for char in password1):
            flash('Password must have at least one digit', category='error')
        elif not any(char in '!@#$%^&*' for char in password1):
            flash('Password must have at least one special character', category='error')
        elif password1 != password2:
            flash('Passwords must match', category='error')
        else:
            valid = curAdmin.register(username,password1, userkey)
            if valid:
                flash('Account created sucessfully. Redirecting to login in 3 seconds...', category='success')
                return render_template('signup.html'), {"Refresh": "3; url=/login"}
            else:
                flash('Unable to create account', category='error')

    return render_template('signup.html')

@app.route('/logout')
def logout():
    curAdmin.logout()
    flash('Logged out successfully', category='success')
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/find_route', methods=['GET', 'POST'])
def route1():
    info = {}

    if request.method == 'POST':
        startStation = request.form.get('start-station')
        endStation = request.form.get('end-station')
        stations = []
        for i in systemObjects:
            x = (i.findRoute(startStation.strip(), endStation.strip()))
            if x != []:
                stations.append(x)

        for i in stations:
            for j in i:
                info[j.getName()] = j.getSchedules()
        return render_template('find_route.html', info=info)
    
    return render_template('find_route.html', info=info)

@app.route('/schedules')
def schedules():

    info = {}
    
    for i in systemObjects:
        stations = {}
        for j in i.getTrains():
            stations[j.getName()] = j.getSchedules()
        info[i.getScheduleId()] = stations
    
    return render_template('schedules.html', info=info)

@app.route('/eta', methods=['GET', 'POST'])
def eta():
    if request.method == 'POST':    
        startStation = request.form.get('start-station')
        endStation = request.form.get('end-station')
    
        times = []
        trains = []
        for i in systemObjects:
            r = (i.findRoute(startStation.strip(), endStation.strip()))
            if r != []:
                trains.append(r)
        
        for i in trains:
            for j in i:
                estTime = j.calculateTrip(startStation.strip(), endStation.strip())
                startTime = j.getSchedules().get(startStation.strip())
                endTime = j.getSchedules().get(endStation.strip())

                times.append([j.getName(), j.getSchedules(), estTime, startStation, endStation, startTime, endTime])
        
        return render_template('eta.html', times=times)

    return render_template('eta.html')

@app.route('/create_system', methods=['GET', 'POST'])
def create_system():

    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))
    if request.method == 'POST':    
        scheduleID = request.form.get('system-id')

        newSystem = trainSchedule(scheduleID)
        systemObjects.append(newSystem)

        with open(pathTrainSchedule, 'r') as f:
            data = json.load(f)

        new_system = {
            "id": scheduleID,
            "trains": []
        }

        data["systems"].append(new_system)

        with open(pathTrainSchedule, 'w') as f:
            json.dump(data, f, indent=4)

        flash('System created successfully', category='success')
    
    return render_template('create_system.html')

@app.route('/remove_system', methods=['GET', 'POST'])
def remove_system():
    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))
    if request.method == 'POST':    
        systemID = request.form.get('system-id')
        sysExists = False
        sys = None
        for i in systemObjects:
            if i.getScheduleId() == systemID:
                systemObjects.remove(i)
                sys = i
                sys.removeSystem()
                sysExists = True
                flash('System successfully removed', category='success')
            
        if not sysExists:
            flash('System not found', category='error')

    return render_template('remove_system.html')

@app.route('/create_schedule', methods=['GET', 'POST'])
def create_schedule():
    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))

    arr = []
    valid_sys = False

    if request.method == 'POST':    
        systemID = request.form.get('system-id')
        departTime = request.form.get('depart-time')
        trainName = request.form.get('train-name')
        stations = request.form.get('stations')
        timeBetweenStat = request.form.get('time-between-stations')

        for i in systemObjects:
          if(i.scheduleId == systemID.strip()):
            sys = i
            valid_sys = True
        # Checking to see if the system is valid
        if(valid_sys == False):
            flash('Not a valid system', category='error')
        # Checking to see if the departTime is valid
        if not datetime.strptime(departTime, '%H:%M'):
            flash('Invalid departure time. Time must in in format 09:45', category='error')
        #Checking to see if stations input is valid
        stats = stations.strip().split('\r\n')
        final_stats = [string.strip() for string in stats if string.strip()]
        if not all(isinstance(elem, str) for elem in final_stats):
            flash('Invalid Station Input. Stations can only contain strings', category='error')
        if not all(len(elem) <= 20 for elem in final_stats):
            flash('Invalid Station Input.', category='error')
        #Checking to see if time between stations input is valid
        times = timeBetweenStat.strip().split('\r\n')
        final_times = [string.strip() for string in times if string.strip()]
        if not all(elem.isdigit() for elem in final_times):
            flash('Invalid Time Input', category='error')
        if not all(len(elem) < 3 for elem in final_times):
            flash('Invalid Time Input.', category='error')
        #Checking to see if user input the correct number of station and times
        if(len(final_times) != (len(final_stats) - 1) ):
            flash('Times do not match', category='error')
        
        timeBet = [int(elem) for elem in final_times]

        newRoute = route()
        for i in range(len(final_stats)):
          newRoute.addStation(station(i, final_stats[i]))  
        newTrain = train(trainName.strip(), newRoute, timeBet, departTime)
        sys.addTrains(newTrain)
        sys.viewTrainSchedule()
        print("Train added")
        flash('Train added successfully', category='success')    

    return render_template('create_schedule.html')

@app.route('/remove_from_schedule', methods=['GET', 'POST'])
def remove_from_schedule():

    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))

    if request.method == 'POST':    
        trainId = request.form.get('train-id')
        trainExists = False
        t = None
        sys = None

        for i in systemObjects:
            for j in i.getTrains():
                if j.getName() == trainId:
                    t = j
                    trainExists = True
                    sys = i
                    flash('Train successfully removed from schedules', category='success')

        if not trainExists:
            flash('Train not found', category='error')
        else:
            sys.removeTrain(t)

    return render_template('remove_from_schedule.html')

@app.route('/admin_home', methods=['POST'])
def admin_home():
    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))

    info = {}
    username = ""
    print("admin home")
    if request.method == 'POST':
        print("POST")
        if request.form['submit_button'] == 'Change Username':
            print("change user")
            return render_template('change_username.html')
        elif request.form['submit_button'] == 'Change Password':
            print("change pass")
            return render_template('change_password.html')
        else:
            pass # unknown

    return render_template('admin_home.html', user=username, info=info)

@app.route('/change_username', methods=['GET', 'POST'])
def change_username():

    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))

    print("change username function")
    if request.method == 'POST':    
        userName = request.form.get('user-name')
        password = request.form.get('user-password')
        newUserName = request.form.get('user-newName')

        print("changing username")
        valid = curAdmin.changeUsername(username,password,newUserName)
        if valid:
            print("changed")
            flash('Username changed successfully', category='success')
            return render_template('change_username.html')
            #return render_template('change_username.html'), {"Refresh": "3; url=/home"}
        else:
            print("error")
            flash('Invalid Information', category='error')
            return render_template('change_username.html')

    return render_template('change_username.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():

    if not curAdmin.getLoggedIn():
        return redirect(url_for('home_page'))

    if request.method == 'POST':    
        userName = request.form.get('user-name')
        password = request.form.get('user-password')
        newPassword = request.form.get('user-newPassword')

        if len(newPassword) < 6:
            flash('Password must be at least 6 characters long', category='error')
        elif not any(char.isupper() for char in newPassword):
            flash('Password must have at least one upper case letter', category='error')
        elif not any(char.isdigit() for char in newPassword):
            flash('Password must have at least one digit', category='error')
        elif not any(char in '!@#$%^&*' for char in newPassword):
            flash('Password must have at least one special character', category='error')
        elif newPassword == password:
            flash('Password can not be the same', category='error')
        else:
            valid = curAdmin.changePassword(username,password, newPassword)
            if valid:
                flash('Password changed successfully', category='success')
                return render_template('change_password.html'), {"Refresh": "3; url=/home"}
            else:
                flash('Unable to change password', category='error')
    
    return render_template('change_password.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000), debug=True)
