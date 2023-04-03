class route():
    def __init__(self) -> None:
      self.stations = []

    def addStation(self, newStation):
      self.stations.append(newStation)
      return self.station

    def removeStation(self, station):
      self.stations.remove(station)
      return self.station

    def print(self):
      for stations in self.stations:
        print(stations)
    