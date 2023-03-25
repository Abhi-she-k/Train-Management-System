class trainSchedule():

    def __init__(self, scheduleId) -> None:
        self.scheduleId = scheduleId
        self.trains = []

    def addTrains(train):
      self.trains.append(train)
      return self.trains

    def remove(train):
      self.trains.remove(train)
      return self.trains

    def update(oldTrain, newTrain):
      for i in range(len(self.trains)):
        if(self.trains[i] == oldTrain):
          self.trains[i] = newTrain

      return self.trains
      
    def __str__(self):
      return self.trains