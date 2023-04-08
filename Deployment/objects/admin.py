from objects.user import user
from objects.trainSchedule import trainSchedule
# from user import user
# from trainSchedule import trainSchedule
import json
path = 'objects/adminInfo.json'

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

    def changeUsername(self, oldUser, password, newUser):
      data = None
      userFound = False
      with open(path, 'r') as f:
        data = json.load(f)
      # Check if new username already exists
      for admins in data["admins"]:
        # Check for valid password
        if admins["username"] == oldUser:
          userFound = True
          if password != admins["password"]:
            return 1
        # Check if new username exists
        if admins["username"] == newUser:
          return 2
      # Change old username to new username
      if not userFound:
        return 3
      for i in range(len(data["admins"])):
        if data["admins"][i]["username"] == oldUser:
          data["admins"][i]["username"] = newUser

      with open(path, 'w') as f:
        json.dump(data, f, indent=4)
      return 0

    def changePassword(self, userName, oldpass, newPassword):
      data = None
      userFound = False
      with open(path, 'r') as f:
        data = json.load(f)
      # Check if user exists and valid password
      for admins in data["admins"]:
        if admins["username"] == userName:
          userFound = True
          if admins["password"] != oldpass:
            return 1
      if not userFound:
        return 2
      # Change old password to new password
      for i in range(len(data["admins"])):
        if data["admins"][i]["username"] == userName:
          data["admins"][i]["password"] = newPassword
      
      with open(path, 'w') as f:
        json.dump(data, f, indent=4)
      return 0

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
    
    def logOut(self):
      self.loggedIn = False

    def getLoggedIn(self):
      return self.loggedIn