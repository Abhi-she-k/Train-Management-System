from route import *
from station import *
from user import *
from admin import *
from trainSchedule import *
from train import *
from user import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testRoute(self):
      r = route()
      s1 = station(1, "Kennedy")
      s2 = station(2, "Warden")
      # Test addStation
      self.assertEqual(r.addStation(s1), [s1])
      self.assertEqual(r.addStation(s2), [s1, s2])
      # Test removeStation
      self.assertEqual(r.removeStation(s1), [s2])

    def testTrain(self):
      r = route()
      r.addStation(station(1, "Kennedy"))
      r.addStation(station(2, "Warden"))
      r.addStation(station(3, "Coxwell"))            
      t = train("testTrain", r, [10,3], "12:30")
      newR = route()
      newR.addStation(station(5, "Union"))
      newR.addStation(station(6, "Queen"))
      # Test calculateSchedule
      self.assertEqual(t.calculateSchedule("12:30"), {"Kennedy": "12:30", "Warden": "12:40", "Coxwell": "12:43"})
      # Test calculateTrip
      self.assertEqual(t.calculateTrip("Kennedy", "Warden"), 10)
      self.assertEqual(t.calculateTrip("Kennedy", "Coxwell"), 13)
      self.assertEqual(t.calculateTrip("Warden", "Coxwell"), 3)
      
      
    def testTrainSchedule(self):
      s = trainSchedule("testSchedule")
      r = route()
      r2 = route()
      r.addStation(station(1,"Union"))
      r.addStation(station(2,"King"))
      r.addStation(station(3,"Queen"))
      r2.addStation(station(7,"Union"))
      r2.addStation(station(8,"Queen"))
      r2.addStation(station(9,"Spadina"))
      t = train("train1",r,[10,3], "9:30") 
      t2 = train("train2",r2,[15,3], "3:30")
  
      # Test addTrains
      s.addTrains(t)
      self.assertEqual(s.trains, [t])
      s.removeTrain(t)
      self.assertEqual(s.trains, [])
      
      # Test checkConflicts
      s.addTrains(t)
      self.assertFalse(s.checkConflicts(t))
      self.assertTrue(s.checkConflicts(t2))
      s.addTrains(t2)
      # Test findRoute
      self.assertEqual(s.findRoute("Union", "Queen"), [t,t2])
      self.assertEqual(s.findRoute("Queen", "Union"), [])

    def testAdmin(self):
      a = admin(None,None,None,None)
      
      # Test register
      self.assertTrue(a.register("admin3", "password3","admin321"))
      self.assertFalse(a.register("newadmin", "testpass", ""))
      self.assertTrue(a.register("newadmin", "testpass", "las;kdjf"))
      
      # Test login
      self.assertTrue(a.login("admin1", "conductor1234"))
      self.assertFalse(a.login("",""))
      self.assertTrue(a.login("admin2", "railway456"))
      self.assertFalse(a.login("oaspdlkjhf", "la;skdjf"))

if __name__ == '__main__':
    unittest.main()








