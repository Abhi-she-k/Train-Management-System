import json
from trainSchedule import *

class rider(user):
    def __init__(self):
        super().__init__(id)

    def viewSchedule(self, nameOfSystem):
      # data = None
      # with open("trainSchedule.json") as f:
      #   data = json.load(f)

      schedule = self.getSchedule(nameOfSystem)
      print(schedule)
       
    def getSchedule(self, nameOfSystem):
      with open('C:/Users/abhis/Desktop/cps406/Train-Management-System/Deployment/objects/trainSchedule.json', 'r') as f:
      data = json.load(f)

      trains = []
      for system in data["systems"]:
        if system["name"] == nameOfSystem:
          for train in system["trains"]:
            train_info = [train["id"]]
            for i in range(len(train["route"])):
              station_info = [train["route"][i], train["times"][i]]
              train_info.append(station_info)
              trains.append(train_info)
    return trains
  
    def findRoute(self):
        

    def viewMaps(self):
        pass

    def viewExtraInfo(self):
        pass