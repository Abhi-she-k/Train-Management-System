class station(train_station):

    def __init__(self, id, route_id) -> None:
        
        self.id = id
        self.route_id = route_id
        self.location_info = {}
      