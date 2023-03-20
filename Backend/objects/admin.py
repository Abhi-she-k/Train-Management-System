class admin(user):
    def __init__(self, firstName, lastName, id, userName, password, email):
      self.firstName = firstName
      self.lastName = lastName
      self.id = id
      self.userName = userName
      self.password = password
      self.email = email 


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

    def changeUsername(self):
      pass

    def changePassword(self):
      pass