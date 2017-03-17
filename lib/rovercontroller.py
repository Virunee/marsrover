import utils
from planetau import Planetau
from copy import copy

class Rover:
  def __init__(self, position, direction):
    """Init Mars Rover with position in Coordinates2D and Direction"""
    self.__position = None
    self.__direction = None

    if ( not isinstance(position, utils.Coordinates2D) or
         direction not in utils.CardinalDirections ):
      raise ValueError('Check types')

    self.__position = copy(position)
    self.__direction = copy(direction)

  def __repr__(self):
    """Return formatted representation string"""
    return "Mars Rover >> Current position: {0}; Direction: {1}".format(self.__position, self.__direction)

  @property
  def direction(self):
    return self.__direction

  @direction.setter
  def direction(self, newDirection):
    if newDirection not in utils.CardinalDirections:
      raise ValueError('Check type of new direction (utils.CardinalDirections)')
    self.__direction = newDirection

  @property
  def position(self):
    return self.__position

  @position.setter
  def position(self, newPosition):
    if not isinstance(newPosition, utils.Coordinates2D):
      raise ValueError('Check type of new position (Coordinates2D)')
    self.__position = newPosition


class RoverController:
  step = 1
  def __init__(self, planetau, marsRover = None):
    """Init Roller Cobtroller with Planetau and MarsRover"""
    self.__planetau = None
    self.__marsRover = None

    if not isinstance(planetau, Planetau):
      raise ValueError('Check planetau')
    self.planetau = planetau

    if (marsRover and (not isinstance(marsRover, Rover) or
         marsRover.position not in planetau)):
      raise ValueError('Chek rover. It could be out of planetau')
    self.marsRover = marsRover

  def getMarsRover(self):
    """Return private property marsRover"""
    return self.__marsRover

  def sendCommand(self, command):
    """Handle commands to move Rover"""
    if command not in utils.MovingDirections:
      raise ValueError('Check command (utils.MovingDirections)')

    if command == 'M':
      self.__move(RoverController.step)
    else:
      self.__rotate(command)

  def __rotate(self, direction):
    """Rotate Rover 90 degrees left or right"""
    newDirectionIndex = utils.CardinalDirections.index(self.marsRover.direction)

    if (direction == 'R'):
      newDirectionIndex = (newDirectionIndex-1)%len(utils.CardinalDirections)
    elif (direction == 'L'):
      newDirectionIndex = (newDirectionIndex+1)%len(utils.CardinalDirections)
    
    self.marsRover.direction = utils.CardinalDirections[newDirectionIndex]

  def __move(self, step):
    """Move Rover in 1 step according direction"""
    rawCoordinates = self.marsRover.position

    if (self.marsRover.direction == 'N'):
      rawCoordinates.y += step
    elif (self.marsRover.direction == 'E'):
      rawCoordinates.x += step
    elif (self.marsRover.direction == 'S'):
      rawCoordinates.y -= step
    elif (self.marsRover.direction == 'W'):
      rawCoordinates.x -= step

    if rawCoordinates not in self.planetau:
      raise IndexError('Rover can''t go out of bounds of Planetau' )

    self.marsRover.position = rawCoordinates
