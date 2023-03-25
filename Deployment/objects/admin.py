from user import *
from trainSchedule import *
import json
class admin(user):
    def __init__(self, firstName, lastName, userType, userId):
        super().__init__(firstName, lastName, userType, userId)
        self.trainSystems = {}
      
    def register(self):
      pass

    def login(self, userName, password):
      data = None
      with open("../adminInfo.json") as f: 
        data = json.load(f)
      #check if username exists and password matches given username's password
      for admin in data["admins"]:
        if userName == admin["name"] && password == admin["password"]:
          return True
      return False 

    def authenticate(self):
      pass

    def forgotCredentials(self):
      pass

    def logout(self):
      pass

    def changeUsername(self, newUser):
      self.userName = newUser

    def changePassword(self, newPassword):
      self.password = newPassword

    def createSchedule(self, scheduleID):
      newSchedule = trainSchedule(scheduleID)
      self.trainSystems[scheduleID] = newSchedule

    def addToSchedule(self, scheduleID, train):
      
      trainSchedule =  self.trainSystems[scheduleID]
      trainSchedule.addTrains(train)

    def checkConflicts(scheduleID):
      trainSchedule =  self.trainSystems[scheduleID]
      trainSchedule.checkConficts
      
      
      
      
      
      
      
      