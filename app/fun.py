from datetime import datetime
import random
from database.datos import *

#creacion de menus
def menus(lista):
    while True:
        for i in range(len(lista)):
            print(str(i+1) + ") " + lista[i])
        opt = input("\n-> Opcion: ")
        if not opt.isdigit():
            print("Invalid Option. Please, use a number.")
            input("Press enter to continue.\n")
        elif int(opt) not in range(1, len(lista)+1):
            print("Out of range. Please, choose a number between 1 and" + " " + str(len(lista))+ ".")
            input("Press enter to continue.\n")
        else:
            opt = int(opt)
            return opt

#Devuelve una lisa con las ids de las cartas "barajeadas"
def barajeo_carta(mazo_keys):
    mazo_keys=list(mazo_keys)
    largo=len(mazo_keys)
    mazo_barajeado=[]

    while largo!=len(mazo_barajeado):
        carta=mazo_keys[random.randrange(len(mazo_keys))]
        if carta not in mazo_barajeado:
            mazo_barajeado.append(carta)
            mazo_keys.pop(mazo_keys.index(carta))
    return mazo_barajeado


#prioridad de turnos
#cambia las cartas iniciales y la prioridad de juego al diccionario players.
def setGamePriority(mazo_keys):
    mazo_barajeado=barajeo_carta(mazo_keys)
    for i in context_game["game"]:
        players[i]["initialCard"]=mazo_barajeado[0]

        print(players[i]["name"],"saco",cartas[mazo_barajeado[0]]["literal"])

        mazo_barajeado=mazo_barajeado[1:]
    for i in range(len(context_game["game"])):
        for j in range(i+1,len(context_game["game"])):
            if cartas[players[context_game["game"][i]]["initialCard"]]["value"]==cartas[players[context_game["game"][j]]["initialCard"]]["value"]:
                if cartas[players[context_game["game"][i]]["initialCard"]]["priority"]>cartas[players[context_game["game"][j]]["initialCard"]]["priority"]:
                    aux = context_game["game"][i]
                    context_game["game"][i] = context_game["game"][j]
                    context_game["game"][j] = aux

            elif cartas[players[context_game["game"][i]]["initialCard"]]["value"]>cartas[players[context_game["game"][j]]["initialCard"]]["value"]:
                aux=context_game["game"][i]
                context_game["game"][i]=context_game["game"][j]
                context_game["game"][j]=aux
    for i in range(len(context_game["game"])):
        players[context_game["game"][i]]["priority"]=i+1
    players[context_game["game"][-1]]["bank"]=True


#resetear puntos
def resetPoints():
    for i in context_game["game"]:
        players[i]["points"]=20