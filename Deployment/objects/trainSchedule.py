from datetime import datetime, timedelta
import json

class trainSchedule():
    def __init__(self, scheduleId) -> None:
        self.scheduleId = scheduleId
        self.trains = []

    def addTrains(self, train):

      if(checkConficts(train) == True):
        with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'r') as f:
          data = json.load(f)
  
        new_train = {
          "id": train.name,
          "route": train.getStatAsList(),
          "times": train.getTimesAsList()
        }
  
        for system in data["systems"]:
          if system["id"] == self.scheduleID:
              system["trains"].append(new_train)
    
        with open('C:/Users/abhis/Desktop/cps406/Train-Management- System/Deployment/objects/trainSchedule.json', 'w') as f:
          json.dump(data, f, indent=4)
          self.trains.append(train)
      else:
        return False


    def remove(self, train):
      with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'r') as f:
          data = json.load(f)
  
      for system in data["systems"]:
          if system["id"] == self.scheduleID:
              for train in system["trains"]:
                  if train["id"] == train_id:
                      system["trains"].remove(train)
  
      with open('C:/Users/abhis/Desktop/cps406/Train-Management- System/Deployment/objects/trainSchedule.json', 'w') as f:
          json.dump(data, f, indent=4)

    def update(self, oldTrain, newTrain):
      for i in range(len(self.trains)):
        if(self.trains[i] == oldTrain):
          self.trains[i] = newTrain
      return self.trains

    def calculateTrip(self, train, start, end):
        return train.calculateTrip(start, end)
      
    def checkConficts(self, checkTrain):
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

    def print(self):
      for trains in self.trains:
         print(trains.name + ": ")
         trains.print()
         print(" ")
      