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
  print("Welcome to the Train Management System")
  print("1. View Train Schedules")
  print("2. Find Route")
  print("3. Admin Login")
  print("4. Exit")

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

def calculateRoute():
  startStation = input("Enter a starting station: ")
  endStation = input("Enter an ending station: ")
  print(" ")
  times = []
  for i in systemObjects:
    r = i.findRoute(startStation.strip(), endStation.strip())

  for train in r:
    time = train.calculateTrip(startStation.strip(), endStation.strip())
    times.append(time)

  sorted(times):
  
  for t in times:
    print(startStation.strip() + " -----> " + endStation.strip() + ": " + t)

def admin_login():
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")
  pass

if __name__ == "__main__":
  createObjects()

  while True:
    print_menu()
    
    user_choice = input("Please enter your choice (1-4): ")
  
    if user_choice == "1":
      view_train_schedule()
    if user_choice == "2":
      find_route()
    if user_choice == "3":
      calculate_route()
    if user_choice == "4":
      admin_login()
    if user_choice == "5":
      make_a_schedule()
    if user_choice == "6":
      print("Thank You for using the Train Admin System. Goodbye!")
      systemObjects = []
      break
  
