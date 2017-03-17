#!/usr/bin/env python

"""
Base data for moving
MovingDirections - all available commands to Rover
CardinalDirections - all available directions to turn
Coordinates2D - describes coordinates (x,y)

"""

MovingDirections = ('L', 'R', 'M')
CardinalDirections = ('N', 'E', 'S', 'W')

class Coordinates2D:
  def __init__(self, x, y):
    """Init x,y coordinates"""
    if (not isinstance(x, int) or not isinstance(y, int)):
      raise ValueError('Check types')
    self.x = x
    self.y = y

  def __repr__(self):
    """Return formatted representation string"""
    return '{0} {1}'.format(self.x, self.y)

  def __eq__(self, val):
    """Check if coordinates are equal"""
    if isinstance(val, Coordinates2D):
      return (self.x == val.x and self.y == val.y)
    return False

  def __ne__(self, val):
    """Check if coordinates are not equal"""
    return not self.__eq__(val)

if __name__ == '__main__':
  pass