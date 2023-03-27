import json
from route import *
from station import *
from user import *
from admin import *
from trainSchedule import *
from train import *
from user import *

systemObjects = []
curAdmin = admin(None)

def createObjects():
  with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'r') as f:
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
        print(times)
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
  createObjects()
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

  for train in r:
    time = train.calculateTrip(startStation.strip(), endStation.strip())
    times.append([time, train.schedule[startStation.strip()], train.schedule[endStation.strip()]])

  sorted(times)
  
  for t in times:
    print(startStation.strip() + " -----> " + endStation.strip() + ": " , abs(round(t[0])) , "min, " , t[1] , "-" , t[2])
  print(" ")

def admin_login():
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")
  valid = curAdmin.login(username,password)
  if !valid:
    print("Wrong username or password")
    return
  loggedIn = True
  print("Logged in as: {}").format(username)
  while loggedIn:
    print("1. Create Schedule ")
    print("2. Add to Schedule ")
    print("3. Remove From Schedule ")
    print("4. Logout")

    admin_choice = input("Please enter your choice(1-4): ")
    if admin_choice == '1':
      scheduleID = input("Create a schedule ID: ")
      curAdmin.createSchedule(scheduleID)
      
    elif admin_choice == '2':
      scheduleID = input("Enter a schedule ID: ")
      trainID = input("Enter a train ID: ") 
      trainExists = False
      train = None 
      # Get train object
      for i in systemObjects:
        for j in i.trains:
          if j.name == trainID:
            train = j 
            trainExists = True
      if !trainExists: 
        print("Error: Train not found")
        return
      curAdmin.addToSchedule(scheduleID, train)
      
    elif admin_choice == '3':
      scheduleId = input("Enter a schedule ID: ")
      trainId = input("Enter a train ID: ")
      trainExists = False
      train = None
      # Get train object
      for i in systemObjects:
        for j in i.trains:
          if j.name == trainID:
            train = j
            trainExists = True
      if !trainExists:
        print("Error: Train not found")
        return
      curAdmin.removeFromSchedule(scheduleId, train)
      
    elif admin_choice == '4':
      print("Loggin out...")
      curAdmin.logout()
      loggedIn = False
      print("Thank You for using the Train Management System. Returning to Main Menu.")
      
    else: 
      print("Invalid Input")
    
if __name__ == "__main__":
  createObjects()

  while True:
    print_menu()
    
    user_choice = input("Please enter your choice (1-6): ")
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
  
