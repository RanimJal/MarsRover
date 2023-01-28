from MarsRover.Planet.Dimension import Dimension
from MarsRover.Rover.Orientation import Orientation
from MarsRover.Rover.Position import Position
from MarsRover.Rover.State import State


class Rover:

    def __int__(self, s: State):
        self.state = s

    def canMove(self):
        pass

    def advance_N(self, delta: int, dimension_planet: Dimension) -> State:

        # move forward while being on the edge of the toroidal planet
        if self.state.position.y == dimension_planet.height and self.state.orientation == "N" and delta <= dimension_planet.height:
            self.state.position.y = 0
        if self.state.position.y == 0 and self.state.orientation == "S" and delta <= dimension_planet.height:
            self.state.position.y = dimension_planet.height
        if self.state.position.x == 0 and self.state.orientation == "E":
            self.state.position.x = dimension_planet.width
        if self.state.position.y == dimension_planet.width and self.state.orientation == "W":
            self.state.position.x = 0

        if self.state.orientation == "N":
            self.state.position.y = self.state.position.y + delta
        if self.state.orientation == "S":
            self.state.position.y = self.state.position.y - delta
        if self.state.orientation == "E":
            self.state.position.x = self.state.position.x - delta
        if self.state.orientation == "W":
            self.state.position.x = self.state.position.x + delta
        return self.state

    def backOff_S(self, delta: int, dimension_planet: Dimension) -> State:
        # move backwards while on the edge of the toroidal planet
        if self.state.orientation == "N":
            self.state.position.y = self.state.position.y - delta
        if self.state.orientation == "S":
            self.state.position.y = self.state.position.y + delta
        if self.state.orientation == "E":
            self.state.position.x = self.state.position.x + delta
        if self.state.orientation == "W":
            self.state.position.x = self.state.position.x - delta
        return self.state

    def turn_left(self) -> State:
        if self.state.orientation == "N":
            self.state.orientation = "E"
            return self.state
        if self.state.orientation == "S":
            self.state.orientation = "E"
            return self.state
        if self.state.orientation == "E":
            self.state.orientation = "S"
            return self.state
        if self.state.orientation == "W":
            self.state.orientation = "N"
            return self.state

    def turn_right(self) -> State:
        if self.state.orientation == "N":
            self.state.orientation = "W"
            return self.state
        if self.state.orientation == "S":
            self.state.orientation = "W"
            return self.state
        if self.state.orientation == "E":
            self.state.orientation = "N"
            return self.state
        if self.state.orientation == "W":
            self.state.orientation = "S"
            return self.state



