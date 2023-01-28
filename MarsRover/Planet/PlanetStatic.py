from MarsRover.Planet.Obstacle.Box import Box
from MarsRover.Planet.Obstacle.Coline import Coline
from MarsRover.Planet.Obstacle.Rock import Rock
from MarsRover.Rover.Rover import Rover


class PlanetStatic:

    mapPlanet = [
        [Rover, None, None],
        [None, Box, None],
        [Coline, None, Rock]
    ]

