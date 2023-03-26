import json
from route import *
from station import *
from user import *
from admin import *
from trainSchedule import *
from train import *
from user import *

systemObjects = []

def createObjects():

  
  
  with open('trainSchedule.json', 'r') as f:
    data = json.load(f)
   
  systems = [] 

  for system in data['systems']:
    
    systemId = system['id']
    scheduleObject = trainSchedule(systemId)
    
    for train in system['trains']:
        name = train['name']
        route = train['route']
        r = route()
        for i in range(len(route)):
          stat = station(i, route[i])
          r.addStation(stat)
        times = train['times']
        depart = train['depart']
      
        trainObject = train(name, r,)
        scheduleObject.trains.append(trainObject)
    
    system.append(scheduleObject)


def print_menu():
  #"Print Options to terminal"
  print("Welcome to the Train Management System")
  print("1. View Train Schedules")
  print("2. Find Route")
  print("3. Admin Login")
  print("4. Exit")

def view_train_schedule():
  #Print all Trains in train schedule
  print("Train Schedule: ")
  data = None
  with open("trainSchedule.json") as f:
      data = json.load(f)
    
  for train in data['systems'][0]['trains']:
      str = ', '.join(train['route'])
      str = " | Train: " + train['id'] + " |" + "\n" + " | Routes: " + str + " |" + "\n" + " | Times: " + train['times'] + " | " 
      print(str)
      print(" ------------------------------------------------------")


def find_route():
  with open("trainSchedule.json", "r") as f:
    train_schedule = json.load(f)
  start = input("Pick a Starting Station: ")
  end = input("Pick a Ending Station: ")
  #check if start and end are in a existing route
  valid_stations = False
  for system in train_schedule["systems"]:
    for train in system["trains"]:
      if start in train["route"] and end in train["route"]:
        valid_stations = True
        print("Route ID: ", train["id"])
        print("Available Times: ", train["times"])
        break
    if valid_stations:
      break
  #Start and End Station not in any route
  if not valid_stations:
    print("No available routes from " + start + " to " + end)

def admin_login():
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")
  pass


#Main Loop
# while True:
#   print_menu()
#   user_choice = input("Please enter your choice (1-4): ")

#   if user_choice == "1":
#     view_train_schedule()
#   if user_choice == "2":
#     find_route()
#   if user_choice == "3":
#     admin_login()
#   if user_choice == "4":
#     print("Thank You for using the Train Admin System. Goodbye!")
#     break
  
createObjects()
print(systemObjects)