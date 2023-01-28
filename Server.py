import socket

Host = "127.0.0.1"
Port = 2208

# Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind((Host, Port))
socket.listen(1)
print("Serveur: en attente de connexions des clients TCP ...")
client, ip = socket.accept()
print("Le Rover : ", ip, "s'est connecté")

while True:
    requete_rover = client.recv(500)
    requete_rover = requete_rover.decode('utf-8')
    print(requete_rover)
    if not requete_rover:
        print("Connexion perdue :( \n CLOSE")
        break
    msg = input("->")
    msg = msg.encode("utf-8")
    client.send(msg)


client.close()
socket.close()