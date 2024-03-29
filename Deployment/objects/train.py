from datetime import datetime, timedelta

class train():
    def __init__(self, name, route, timeBetweenStat, depart) -> None:
      self.name = name
      self.route = route
      self.times = timeBetweenStat
      self.length = len(self.route.stations)
      self.stations = self.route.stations
      self.schedule = {}
      self.depart = depart
      self.calculateSchedule(depart)
      
      
    def calculateSchedule(self, departTime):
      start = self.stations[0].name
      self.schedule[start] = departTime
      stations = self.route.stations
      
      for i in range(len(self.times)):
        start = datetime.strptime(departTime, '%H:%M')
        end = start + timedelta(minutes=self.times[i])
        endTimeStr = end.strftime('%H:%M')
        self.schedule[stations[i+1].name] = endTimeStr
        departTime = endTimeStr

      return self.schedule

    def calculateTrip(self, startStation, endStation):
      startTime = self.schedule[startStation]
      endTime = self.schedule[endStation]

      start = datetime.strptime(startTime, '%H:%M')
      end = datetime.strptime(endTime, '%H:%M')
      diff = end - start
      diffMinutes = diff.total_seconds() / 60

      return abs(round(diffMinutes))


    def getStatAsList(self):
      li = [] 
      for i in self.route.stations:
          li.append(i.name)

      return li

    def getTimesAsList(self):
      return list(self.schedule.values())
      
    def printTrain(self):
      print(" ")
      print(self.name+":")
      print("-" * 50)

      for key, value in self.schedule.items():
        print(str(key) + " ----- " + value)
      print("-" * 50)
    
    def getSchedules(self):
      return self.schedule
      
    def getName(self):
      return self.name
    
    def getTimes(self):
      return self.times
      