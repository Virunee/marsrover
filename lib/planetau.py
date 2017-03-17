#!/usr/bin/env python

"""
Planetau description
Planetau - left-lower coordinates (0,0),
           right-upper coordanates - given

"""

import utils
from copy import copy

class Planetau:
  def __init__(self, maxPoint):
    """Init new Planetau with coordinates Coorditates2D - max right point"""
    self.maxCoordinates = None

    if not isinstance(maxPoint, utils.Coordinates2D):
      raise ValueError('Check type')
    
    if (maxPoint.x >= 0 and maxPoint.y >= 0):
      self.maxCoordinates = copy(maxPoint)

  def __repr__(self):
    """Return formatted representation string"""
    return "Planetau >> {0}".format(self.maxCoordinates)

  def __contains__(self, ckeckVal):
    """Check if point is in Planetau"""
    if not isinstance(ckeckVal, utils.Coordinates2D):
      return False

    return (ckeckVal.x >= 0 and ckeckVal.x <= self.maxCoordinates.x and
            ckeckVal.y >= 0 and ckeckVal.y <= self.maxCoordinates.y)

if __name__ == '__main__':
  pass