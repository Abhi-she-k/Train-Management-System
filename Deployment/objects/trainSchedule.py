from datetime import datetime, timedelta
import json

class trainSchedule():
    def __init__(self, scheduleId) -> None:
        self.scheduleId = scheduleId
        self.trains = []

    def addTrains(self, train):

      with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'r') as f:
        data = json.load(f)

      new_train = {
        "id": train.name,
        "route": train.getStatAsList(),
        "times": train.times,
        "depart" : train.depart
      }

      for system in data["systems"]:
        if system["id"] == self.scheduleId:
          system["trains"].append(new_train)
          break
  
      with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'w') as f:
        json.dump(data, f, indent=4)
        self.trains.append(train)



    def removeTrain(self, train):
      remTrain = {
        "id": train.name,
        "route": train.getStatAsList(),
        "times": train.getTimesAsList()
      }
      
      with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'r') as f:
          data = json.load(f)
  
      for system in data["systems"]:
          if system["id"] == self.scheduleId:
              for t in system["trains"]:
                  if t["id"] == train.name:
                      system["trains"].remove(remTrain)
  
      with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'w') as f:
          json.dump(data, f, indent=4)
          self.trains.remove(train)

    def update(self, oldTrain, newTrain):
      for i in range(len(self.trains)):
        if(self.trains[i] == oldTrain):
          self.trains[i] = newTrain
      return self.trains

    def calculateTrip(self, train, start, end):
        return train.calculateTrip(start, end)
      
    def checkConflicts(self, checkTrain):
      checkStations = checkTrain.stations
      for train in self.trains:
        stations = train.stations
        for station in stations:
          if(station in checkStations):
            checkTT = datetime.strptime(checkTrain.schedule[station], '%H:%M')
            originalTT = datetime.strptime(train.schedule[station], '%H:%M')
            diff = abs(checkTT - originalTT)
            if(diff < timedelta(minutes=5)):
              print("Cannot Add Train")
              return False
      return True
    
    def viewTrainSchedule(self):
      print(self.scheduleId)
      for trains in self.trains:
        trains.print()
      print(" ")
    
    def findRoute(self, startStation, endStation):
      isRoute = False
      r = []
      for t in self.trains:
        station = t.getStatAsList()
        if (startStation in station) and (endStation in station):
          t.print()
          r.append(t)
          isRoute = True
      if isRoute == False:
        print("No routes matching this criteria")
      return r