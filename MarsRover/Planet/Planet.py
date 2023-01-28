from MarsRover.Planet.Dimension import Dimension
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover


class Planet:

    HEIGHT: int = 2
    WIDTH: int = 2
    dimension: Dimension = Dimension()
    dimension.height = HEIGHT
    dimension.width = WIDTH

    def findRover(dimension: Dimension, world: list) ->Position:
        for x in range(dimension.width+1):
            for y in range(dimension.height+1):
                if world[x][y] == Rover:
                    pos = Position()
                    pos.x = x
                    pos.y = y
                    return pos

