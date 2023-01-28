from MarsRover.Planet.Dimension import Dimension
from MarsRover.Planet.Obstacle.Obstacle import Obstacle
from MarsRover.Rover.Position import Position


class PlanetBuild:

    def build(dimension: Dimension, world: list) -> list:
        builder = {}
        listL = []
        listG = []
        for x in range(dimension.width+1):
            for y in range(dimension.height+1):
                #print(x,y)
                position = Position()
                position.x = x
                position.y = y
                #print(world[x][y])
                obstacle: Obstacle = world[x][y]
                key, value = position, obstacle
                builder[key] = value
            listG.append(listL)
        return listG
