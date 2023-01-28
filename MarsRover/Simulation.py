from MarsRover.Planet.Planet import Planet
from MarsRover.Planet.PlanetBuild import PlanetBuild
from MarsRover.Planet.PlanetStatic import PlanetStatic
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover
from MarsRover.Rover.State import State


class Simulation:
    world: list = PlanetStatic.mapPlanet
    dimension = Planet.dimension
    grid = PlanetBuild.build(dimension, world)

    position_rover: Position = Planet.findRover(dimension, world)
    rover: Rover = Rover()
    rover.state = State()
    rover.state.position = position_rover
    rover.state.orientation = "S"

    rover.turn_left()
    rover.advance_N(2,dimension)
    rover.backOff_S(2,dimension)
    print("** Orientation Rover: ", rover.state.orientation)
    print("*** Position Rover: (", rover.state.position.x,",", rover.state.position.y, ")")
