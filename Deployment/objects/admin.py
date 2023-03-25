import trainSchedule

class admin(user):
    def __init__(self, firstName, lastName, t, userId, userName, password, email):
      # super().__init__(firstName,lastName, t, userId)
      self.userName = userName
      self.password = password
      self.email = email 
      self.schedule = {}


    def register(self):
      pass

    def login(self, userName, password):
      pass

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

    def makeSchedule(scheduleID):
      newSchedule = trainSchedule(scheduleID)
      self.schedule[scheduleID] = newSchedule
      

    #paramter is a train object
    def addTrain(Train, scheduleID):
      schedule = self.schedule[scheduleID]
      (schedule.trains).append(train)
      self.schedule[scheduleID] = schedule

    def checkConflicts(self):
      #idk
      
      
      
      
      
      
      