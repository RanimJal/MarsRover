import socket

from MarsRover.Planet.Planet import Planet
from MarsRover.Planet.PlanetBuild import PlanetBuild
from MarsRover.Planet.PlanetStatic import PlanetStatic
from MarsRover.Rover.Position import Position
from MarsRover.Rover.Rover import Rover
from MarsRover.Rover.State import State


Host = "127.0.0.1"
Port = 2208

# Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((Host, Port))

# Config Rover #
world: list = PlanetStatic.mapPlanet
dimension = Planet.dimension
grid = PlanetBuild.build(dimension, world)
position_rover: Position = Planet.findRover(dimension, world)
rover = Rover()
rover.state = State()
rover.state.position = position_rover
rover.state.orientation = "S"


def avance(delta):
    rover.advance_N(delta, dimension)
    return str("### After Advancing : (" + str(rover.state.position.x) + "," + str(rover.state.position.y) + ") ****> " + rover.state.orientation)


def reculer(delta):
    rover.backOff_S(delta, dimension)
    return str("### After Retreating : (" + str(rover.state.position.x) + "," + str(rover.state.position.y) + ") ****> " + rover.state.orientation)


def turnR():
    rover.turn_right()
    return str("### After Turning Right : ("+str(rover.state.position.x)+","+str(rover.state.position.y)+") ****> "+rover.state.orientation)


def turnL():
    rover.turn_left()
    return str("### After Turning Left : ("+str(rover.state.position.x)+","+str(rover.state.position.y)+") ****> "+rover.state.orientation)


msg = "\n ### Bonjour c'est le Rover, j'attends vos instructions :)  ...\n"
msg = msg.encode("utf-8")
socket.send(msg)


while True:

    requete_server = socket.recv(500)
    data_list = requete_server.decode('utf-8').split(" ", 1)
    cmd = data_list[0]

    if cmd == "TL":
        s: str = turnL()
        socket.send(s.encode("utf-8"))
    if cmd == "TR":
        s: str = turnR()
        socket.send(s.encode("utf-8"))
    # Il faut deux arguments pour cette commande
    if cmd == "AV":
        s: str = avance(int(data_list[1]))
        socket.send(s.encode("utf-8"))
    # Il faut deux arguments pour cette commande
    if cmd == "RC":
        s: str = reculer(int(data_list[1]))
        socket.send(s.encode("utf-8"))

    print(requete_server)

