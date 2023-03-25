from route import *
from station import *
from train import *
from train import *
from user import *


stat1 = station(1,"Bloor-Yonge")
stat2 = station(2,"Sherbourne")
stat3 = station(3,"Castle Frank")

route = route()
route.addStation(stat1)
route.addStation(stat2)
route.addStation(stat3)
print(route)



