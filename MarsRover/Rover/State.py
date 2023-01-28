
from MarsRover.Rover.Position import Position


class State:

    def __int__(self):
        from MarsRover.Rover.Orientation import Orientation
        self.position = Position()
        self.orientation = Orientation()
