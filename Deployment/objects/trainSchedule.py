from datetime import datetime, timedelta
import json

class trainSchedule():
    def __init__(self, scheduleId) -> None:
        self.scheduleId = scheduleId
        self.trains = []

    def addTrains(self, train):
      
      newTrain = { "id": train.name,
                   "route": train.stations,
                   "times": train.schedule
                 }
      self.trains.remove(train)
      with open("../../trainSchedule.json") as f:
        data = json.load(f)
      for system in data["systems"]:
          if system["id"] == self.scheduleId:
            system["trains"].append(new_train)
      updated_json = json.dumps(data)
      self.trains.append(train)
      return self.trains

    def remove(self, train):

      
      
      return self.trains

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
      