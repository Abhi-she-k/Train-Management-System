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
      calculateSchedule(self, self.stations[0], self.stations[length-1], depart)
      

    def updateRoute(self, newRoute, timeBetweenStat, name, departTime):
      self.id = id
      self.name = name
      self.route = newRoute
      self.time = timeBetweenStat
      self.length = len(self.newRoute.stations)
      calculateSchedule(newRoute[0],newRoute[length-1], departTime)
      
    def calculateSchedule(self, startStation, endStation, departTime):
    
      self.schedule[start] = departTime
      stations = self.route.stations
      
      for i in range(len(times))
        start = datetime.strptime(departTime, '%H:%M')
        end = start + timedelta(minutes=time[i])
        endTimeStr = end_time_obj.strftime('%H:%M')
        self.schedule[=stations[i+1]] = endTimeStr
        departTime = endTimeStr

            

    def calculateRoute(self, station1, station2,departTime):
      

    def print(self):
      for key, value in self.schedule.items():
        print(key, " : ", value)
      
      
      
      
      
  