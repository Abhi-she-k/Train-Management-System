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
      

    def updateRoute(self, newRoute, timeBetweenStat, name, departTime):
      self.id = id
      self.name = name
      self.route = newRoute
      self.time = timeBetweenStat
      self.length = len(self.newRoute.stations)
      self.calculateSchedule(departTime)
      
    def calculateSchedule(self, departTime):
      start = self.stations[0]
      self.schedule[start] = departTime
      stations = self.route.stations
      
      for i in range(len(self.times)):
        start = datetime.strptime(departTime, '%H:%M')
        end = start + timedelta(minutes=self.times[i])
        endTimeStr = end.strftime('%H:%M')
        self.schedule[stations[i+1]] = endTimeStr
        departTime = endTimeStr

    def print(self):
      for key, value in self.schedule.items():
        print(key, " : ", value)
      
      
      
      
      
  