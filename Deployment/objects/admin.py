from user import *
from trainSchedule import *
# from user import user
# from trainSchedule import trainSchedule
import json
path = '/Users/abhishekpaul/Desktop/CPS406/Train-Management-System/Deployment/objects/adminInfo.json'

class admin(user):
    def __init__(self, firstName, lastName, userType, userId):
      self.trainSystems = {}
      self.loggedIn = False
      
    def register(self, userName, password, adminKey):
      data = None
      with open(path, 'r') as f:
        data = json.load(f)
      if not adminKey == data["adminKey"]:
        return False
      newAdmin = {
        "username" : userName,
        "password" : password
      }
      data["admins"].append(newAdmin)
      with open(path, 'w') as f:
        json.dump(data, f, indent=4)
      return True

    def login(self, userName, password):
      data = None
      with open(path) as f: 
        data = json.load(f)
      #check if username exists and password matches given username's password
      for admin in data["admins"]:
        if userName == admin["username"] and password == admin["password"]:
          self.loggedIn = True
          return True
      return False 

    # def authenticate(self):
    #   pass

    # def forgotCredentials(self):
    #   pass

    def logout(self):
      self.loggedIn = False

    def changeUsername(self, newUser):
      self.userName = newUser

    def changePassword(self, userName, newPassword):
      self.password = newPassword

    def createSchedule(self, scheduleID):
      newSchedule = trainSchedule(scheduleID)
      self.trainSystems[scheduleID] = newSchedule

    def addToSchedule(self, scheduleID, train):
      trainSchedule =  self.trainSystems[scheduleID]
      if(trainSchedule.checkConflicts(train) == True):        
        trainSchedule.addTrains(train)
        print("Train Added")

    def removeFromSchedule(self, scheduleID, train):
      trainSchedule =  self.trainSystems[scheduleID]       
      trainSchedule.removeTrain(train)
      print("Train removed")
      
