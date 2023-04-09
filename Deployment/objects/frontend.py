import json
from route import *
from station import *
from user import *
from admin import *
from trainSchedule import *
from train import *
import os
import sys

systemObjects = []
curAdmin = admin(None,None,None,None)
abs_path = os.path.join('objects/', 'trainSchedule.json')
path  = 'C:/Users/abhishekpaul/Desktop/CPS406/Train-Management-System/Deployment/objects/trainSchedule.json'

def createObjects():
  with open(path, 'r') as f:
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

def print_menu():
  #"Print Options to terminal"
  print(" ")
  print("Welcome to the Train Management System")
  print("1. View Train Schedules")
  print("2. Find Route")
  print("3. Calculate ETA")
  print("4. Admin Login")
  
  print("5. Exit")

def view_train_schedule():
  #Print all Trains in train schedule
  for i in systemObjects:
    i.viewTrainSchedule()

def find_route():
  startStation = input("Enter a starting station: ")
  endStation = input("Enter an ending station: ")
  print(" ")
  for i in systemObjects:
    i.findRoute(startStation.strip(), endStation.strip())

def calculate_route():
  startStation = input("Enter a starting station: ")
  endStation = input("Enter an ending station: ")
  print(" ")
  print("Estimated Times: ")
  times = []
  for i in systemObjects:
    r = i.findRoute(startStation.strip(), endStation.strip())
    for t in r:
      time = t.calculateTrip(startStation.strip(), endStation.strip())
      times.append([time, t.schedule[startStation.strip()], t.schedule[endStation.strip()]])

  times.sort()
  
  for t in times:
    print(startStation.strip() + " -----> " + endStation.strip() + ": " , abs(round(t[0])) , "min, " , t[1] , "-" , t[2])
  print(" ")

def admin_login():
    
    valid_sys = False
    stations = []
    timeBet = []
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    valid = curAdmin.login(username,password)
    if not valid:
      print("Wrong username or password")
      return
    loggedIn = True
    print("Logged in as: " + username)

    while loggedIn:
      stations = []
      timeBet = []
      print(" ")
      print("1. Create Schedule ")
      print("2. Create System ")
      print("3. Remove From Schedule ")
      print("4. Remove System ")
      print("5. View Train Schedules ")
      print("6. Logout")
      print(" ")
      admin_choice = input("Please enter your choice(1-5): ")
 
      if admin_choice == '1':  
        system = input("Enter System Name: ")
        for i in systemObjects:
          if(i.scheduleId == system):
            sys = i
            valid_sys = True
        if(valid_sys == False):
          print("Not a Valid System")
        else:
          departureTime = input("Enter the Departure Time (hh:mm): ")
          name = input("Name of Train: ")

          while(True): 
            stat = input("Enter Stations (Press / to exit): ")
            if(stat == "/"):
              break
            stations.append(stat)
            print(stations)
          while(True):
            bet = input("Enter ETA between stations (Press / to exit): ")
            if(bet == "/"):
              break
            timeBet.append(int(bet))
            print(timeBet)
            if(len(timeBet) >= len(stations)):
              print("Too many times!")
              break
          if(len(timeBet) == len(stations)-1):
            newRoute = route()
            for i in range(len(stations)):
              newRoute.addStation(station(i, stations[i]))  
            newTrain = train(name, newRoute, timeBet, departureTime)
            sys.addTrains(newTrain)
            sys.viewTrainSchedule()
            print("Train added")
            print(" ")
          else:
            print("Times do not match")
          valid_sys = False

        
      elif admin_choice == '2':
        scheduleID = input("Enter a System ID: ")
        newSystem = trainSchedule(scheduleID)
        systemObjects.append(newSystem)
        
        with open(path, 'r') as f:
          data = json.load(f)

        new_system = {
            "id": scheduleID,
            "trains": []
        }

        data["systems"].append(new_system)

        with open(path, 'w') as f:
          json.dump(data, f, indent=4)
      
      elif admin_choice == '3':
        trainId = input("Enter a train ID: ")
        trainExists = False
        t = None
        sys = None
        for i in systemObjects:
          for j in i.trains:
            if j.name == trainId:
              t = j
              trainExists = True
              sys = i
        if not trainExists:
          print("Error: Train not found")
        else:
          sys.removeTrain(t)

      elif admin_choice == '4':
        sysId = input("Enter a System ID: ")
        sysExists = False
        sys = None
        for i in systemObjects:
          if i.scheduleId == sysId:
            systemObjects.remove(i)
            sys = i
            sys.removeSystem()
            sysExists = True
            
        if not sysExists:
          print("Error: System not found")
          return
        
      elif admin_choice == '5':
          view_train_schedule()

      elif admin_choice == '6':
        print("")
        print("Loggin out...")
        curAdmin.logout()
        loggedIn = False
        print("Thank You for using the Train Management System. Returning to Main Menu.")
        print("")
      else: 
        print("Invalid Input")

try:    
  if __name__ == "__main__":
    createObjects()

    while True:
      print_menu()
      
      user_choice = input("Please enter your choice (1-5): ")
      print(" ")
    
      if user_choice == "1":
        view_train_schedule()
      elif user_choice == "2":
        find_route()
      elif user_choice == "3":
        calculate_route()
      elif user_choice == "4":
        admin_login()
      elif user_choice == "5":
        print("Thank You for using the Train Management System. Goodbye!")
        systemObjects = []
        break
      else:
        print("Invalid Input")
except KeyboardInterrupt:
  print("Exiting........")
  systemObjects = []
  import sys
  sys.exit()
