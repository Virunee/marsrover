import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))

import unittest
import utils
from planetau import Planetau

class TestPlanetau(unittest.TestCase):
  """Tests for Planetau from planetau.py"""

  def testInitWithValidInput(self):
    """Check planetau with valid arguments"""
    point = utils.Coordinates2D(5, 100)
    planetau = Planetau(point)
    self.assertEqual(planetau.maxCoordinates, point)

  def testInitWithInvalidInput(self):
    """Check planetau with invalid arguments"""
    point = utils.Coordinates2D(-100, 100)
    planetau = Planetau(point)
    self.assertNotEqual(planetau.maxCoordinates, point)
    self.assertEqual(planetau.maxCoordinates, None)

  def testInitWithIncorrectData(self):
    """Check planetau with invalid arguments"""
    self.assertRaises(ValueError, Planetau, "str")

  def testPointInPlanetau(self):
    """Check if point is in planetau"""
    planetau = Planetau(utils.Coordinates2D(5, 100))
    self.assertEqual(True, utils.Coordinates2D(5, 100) in planetau)
    self.assertEqual(False, utils.Coordinates2D(100, 5) in planetau)
    self.assertEqual(False, utils.Coordinates2D(-100, 5) in planetau)
    self.assertEqual(False, utils.Coordinates2D(100, -5) in planetau)
    self.assertEqual(False, "str" in planetau)

if __name__ == '__main__':
    unittest.main()