import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))

import unittest
import utils
from rovercontroller import Rover, RoverController
from planetau import Planetau

class TestRover(unittest.TestCase):
  """Tests for Rover"""

  def test_init_with_valid_input(self):
    """Check Rover with valid arguments"""
    direction = "N"
    point = utils.Coordinates2D(5, 100)
    rover = Rover(point, direction)

    self.assertEqual(rover.position, point)
    self.assertEqual(rover.direction, direction)

  def test_init_with_invalid_input(self):
    """Check Rover with invalid arguments"""
    self.assertRaises(ValueError, Rover, "N", "N")
    self.assertRaises(ValueError, Rover, utils.Coordinates2D(5,100), "K")
    self.assertRaises(ValueError, Rover, "N", "K")

  def test_properties(self):
    """Check setters of properties"""
    rover = Rover(utils.Coordinates2D(5, 100), "N")
    self.assertRaises(ValueError, setattr, rover, "position", "position")
    self.assertRaises(ValueError, setattr, rover, "position", 100)
    self.assertRaises(ValueError, setattr, rover, "direction", "K")
    self.assertRaises(ValueError, setattr, rover, "direction", 100)



class TestRoverController(unittest.TestCase):
  """Tests for RoverController"""
  
  def setUp(self):
    """Setup parameters to test with"""
    self._point = utils.Coordinates2D(5, 100)
    self._direction = "N"
    self._planetau = Planetau(self._point)
    self._rover = Rover(self._point, self._direction)


  def test_init_with_valid_input(self):
    """Check RoverController with valid arguments"""
    rc = RoverController(self._planetau, self._rover)
    rc2 = RoverController(self._planetau)

    self.assertEqual(rc.planetau, self._planetau)
    self.assertEqual(rc.marsRover.position, self._point)
    self.assertEqual(rc.marsRover.direction, self._direction)

    self.assertEqual(rc2.planetau, self._planetau)


  def test_init_with_invalid_input(self):
    """Check RoverController with point out of planetau"""
    rover = Rover(utils.Coordinates2D(100, 100), self._direction)
    self.assertRaises(ValueError, RoverController, self._planetau, rover)


  def test_send_invalid_command(self):
    """Chek send invalid command to Rover"""
    point = utils.Coordinates2D(5, 100)
    rc = RoverController(Planetau(point), Rover(point, "N"))

    self.assertRaises(ValueError, rc.sendCommand, "X")
    self.assertRaises(ValueError, rc.sendCommand, 500)


  def test_send_command_rotate_left(self):
    """Check send commands to rover: N->W->S->E"""
    rc = RoverController(self._planetau, self._rover)

    rc.sendCommand("L")
    self.assertEqual(rc.marsRover.direction, "W")
    rc.sendCommand("L")
    self.assertEqual(rc.marsRover.direction, "S")
    rc.sendCommand("L")
    self.assertEqual(rc.marsRover.direction, "E")
    rc.sendCommand("L")
    self.assertEqual(rc.marsRover.direction, "N")


  def test_send_command_rotate_right(self):
    """Check send commands to rover: N->E->S->W"""
    rc = RoverController(self._planetau, self._rover)

    rc.sendCommand("R")
    self.assertEqual(rc.marsRover.direction, "E")
    rc.sendCommand("R")
    self.assertEqual(rc.marsRover.direction, "S")
    rc.sendCommand("R")
    self.assertEqual(rc.marsRover.direction, "W")
    rc.sendCommand("R")
    self.assertEqual(rc.marsRover.direction, "N")


  def test_send_command_move_valid(self):
    """Check movind on 1 step according to direction"""
    rc = RoverController(self._planetau, self._rover)

    rc.sendCommand("L")
    rc.sendCommand("M")
    self.assertEqual(rc.marsRover.position, utils.Coordinates2D(4, 100))
    rc.sendCommand("L")
    rc.sendCommand("M")
    self.assertEqual(rc.marsRover.position, utils.Coordinates2D(4, 99))
    rc.sendCommand("L")
    rc.sendCommand("M")
    self.assertEqual(rc.marsRover.position, utils.Coordinates2D(5, 99))
    rc.sendCommand("L")
    rc.sendCommand("M")
    self.assertEqual(rc.marsRover.position, utils.Coordinates2D(5, 100))

  def test_send_command_move_invalid(self):
    """Check movind out of planetau bounds"""
    rc = RoverController(self._planetau, self._rover)

    rc.sendCommand("R")
    self.assertRaises(IndexError, rc.sendCommand, "M")


if __name__ == '__main__':
    unittest.main()