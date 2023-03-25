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
        for j in checkStations:
          if(j in stations):
            checkTT = datetime.strptime(checkTrain.schedule[j], '%H:%M')
            originalTT = datetime.strptime(checkTrain.schedule[j], '%H:%M')
            diff = abs(checkTT - originalTT)
            if(diff < timedelta(minutes=5)):
              return False
            else:
              return True
    
    def print(self):
      for trains in self.trains:
         print(trains.name + ": ")
         trains.print()
         print(" ")
      