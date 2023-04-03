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
      self.assertEqual(r.addStation(s1), [s1])
      self.assertEqual(r.addStation(s2), [s1, s2])
      self.assertEqual(r.removeStation(s1), [s2])

    def testAdmin(self):
      a = admin(None,None,None,None)
      # Test login
      self.assertTrue(a.login("admin1", "conductor1234"))
      self.assertFalse(a.login("",""))
      self.assertTrue(a.login("admin1", "railway456"))
      self.assertFalse(a.login("oaspdlkjhf", "la;skdjf"))

      
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()








