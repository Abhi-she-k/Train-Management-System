from route import *
from station import *
from train import *
from train import *
from user import *
from trainSchedule import *

stations1 = ["Kipling", "Islington", "Royal York", "Old Mill", "Jane", "Runnymede", "HighPark", "Keele", "Dundas West"]
stations2 = ["Christie", "Bathurst", "Spadina", "St. George", "Bay", "Bloor-Yonge", "Sherbourne", "Castle Frank", "Broadview" ]
stations3 = ["Chester", "Pape", "Donlands", "Greenwood", "Coxwell", "Woodbine", "Main Street", "Victoria Park", "Warden"]

route1 = route()
route2 = route()
route3 = route()

for i in range(len(stations1)):
    stat1 = station(i, stations1[i])
    stat2 = station(i, stations2[i])
    stat3 = station(i, stations3[i])
    route1.addStation(stat1)
    route2.addStation(stat2)
    route3.addStation(stat3)

train1 = train("line1Train", route1, [2,3,4,2,2,1,2,6], "5:00")
train2 = train("line2Train", route2, [8,5,3,2,1,1,1,3], "1:30")
train3 = train("line3Train", route3, [1,10,2,3,1,9,9,7], "6:45")

mySchedule = trainSchedule(1)
mySchedule.addTrains(train1)
mySchedule.addTrains(train2)
mySchedule.addTrains(train3)
mySchedule.print()






