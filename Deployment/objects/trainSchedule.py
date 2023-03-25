from datetime import datetime, timedelta

class trainSchedule():
    def __init__(self, scheduleId) -> None:
        self.scheduleId = scheduleId
        self.trains = []

    def addTrains(self, train):
      self.trains.append(train)
      return self.trains

    def remove(self, train):
      self.trains.remove(train)
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
      