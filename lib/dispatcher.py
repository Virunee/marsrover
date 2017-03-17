#!/usr/bin/env python

"""
Dispatcher to send commands to RoverController
Gives input data and parses it according instructions (see description)

"""

import utils
from rovercontroller import Rover, RoverController
from planetau import Planetau

class Dispatcher:

  def __init__(self, data):
    """Init dispatcher"""
    self.planetau = None
    self.__roverControllers = []
    self.__commands = []

    self.parseInputs(data)


  def parseInputs(self, data):
    """Parse test inputs"""
    coord = data.pop(0).split()

    try:
      self.planetau = Planetau(utils.Coordinates2D(int(coord[0]), int(coord[1])))
      while data:
          tmp = data.pop(0).split()
          rover = Rover(utils.Coordinates2D(int(tmp[0]), int(tmp[1])), tmp[2])
          self.__roverControllers.append(RoverController(self.planetau, rover))
          self.__commands.append(list(data.pop(0).strip()))

    except Exception as e:
      self.planetau = None
      self.__roverControllers[:]
      self.__commands[:]
      raise e

  def dispatch(self):
    """Send commands one by one to Rover Controller"""
    for (roverController, commands) in zip(self.__roverControllers, self.__commands):
      for command in commands:
        roverController.sendCommand(command)

  def getPositions(self):
    res = []
    for rc in self.__roverControllers:
      r = rc.marsRover
      res.append("{0} {1} {2}".format(r.position.x, 
                                      r.position.y,
                                      r.direction))
    return res


if __name__ == '__main__':
  inputs = []

  inputs.append( input("Input upper-right planetau coordinates: ") )
  counter = 0
  while True:
    counter+=1
    inputs.append( input("Input Rover[{0}] coordinates: ".format(counter)) )
    inputs.append( input("Input command to Rover[{0}]: ".format(counter)) )
    if inputs[-1] == "":
      inputs.pop()
      break

  d = Dispatcher(inputs)
  d.dispatch()
