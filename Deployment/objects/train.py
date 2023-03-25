class train():
    def __init__(self, id, name, route) -> None:
      self.id = id
      self.name = name
      self.route = route

    def updateRoute(self, newRoute):
      self.route = newRoute

    def print(self):
      self.route.print()
      
      
  