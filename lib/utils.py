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
    return '(x={0}, y={1})'.format(self.x, self.y)

  def __eq__(self, val):
    """Check if coordinates are equal"""
    if isinstance(val, Coordinates2D):
      return (self.x == val.x and self.y == val.y)
    return False

  def __ne__(self, val):
    """Check if coordinates are not equal"""
    return not self.__eq__(val) 