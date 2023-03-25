class train():
    def __init__(self, id, name, route, timeBetweenStat) -> None:
      self.id = id
      self.name = name
      self.route = route
      self.times = timeBetweenStat
      self.length = len(self.route.stations)

    def updateRoute(self, newRoute):
      self.route = newRoute

    def print(self):
      for i in range(self.length):
        print(self.route.stations[i])
        print("    |     ")
        print(self.times[i])
        print("    |     ")
      print(self.route.stations[self.length]
      
      
      
      
  