from datetime import datetime
import random

from app.players.players import set_human_player, set_bot_player, show_remove_players
from app.headers import *
from app.xmlgenerate import generate_xml
from database.datos import *

#creacion de menus cards es para mostrar las cartas siesque esta jugando. si no se pone nada no hace nada
def menus(lista):
    menu=""
    for i in range(len(lista)):
        menu+=" ".center(MARGIN_PLAYER) + str(i + 1) + ") " + lista[i] + "\n"
    menu+=" ".center(MARGIN_PLAYER) + "-> Opcion: "
    again="Invalid Option. Please, Use a number.".center(FULL_SCREEN) + "\n" + "Press enter to continue...".center(FULL_SCREEN)
    while True:
        opt =input(menu)
        if not opt.isdigit():
            input(again)
        elif int(opt) not in range(1, len(lista)+1):
            input(again)
        else:
            opt = int(opt)
            return opt


# creacion de menus cards es para mostrar las cartas siesque esta jugando. si no se pone nada no hace nada
def menus_game(lista,roun,cards=""):
    menu=roun+cards
    for i in range(len(lista)):
        menu+=" ".center(MARGIN_PLAYER) + str(i + 1) + ") " + lista[i] + "\n"
    menu+=" ".center(MARGIN_PLAYER) + "-> Opcion: "
    again="Invalid Option. Please, Use a number.".center(FULL_SCREEN) + "\n" + "Press enter to continue...".center(FULL_SCREEN)
    while True:
        show_header_play_game()
        opt =input(menu)
        if not opt.isdigit():
            input(again)
        elif int(opt) not in range(1, len(lista)+1):
            input(again)
        else:
            opt = int(opt)
            return opt

#Devuelve una lisa con las ids de las cartas "barajeadas"
def barajeo_carta(mazo_keys):
    write_log("barajeo_carta() iniciado")
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
    write_log("setGame Priority iniciado")
    mazo_barajeado=barajeo_carta(mazo_keys)
    for i in context_game["game"]:
        players[i]["initialCard"]=mazo_barajeado[0]

        # print(players[i]["name"],"saco",cartas[mazo_barajeado[0]]["literal"])

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
        players[context_game["game"][i]]["bank"]=False
    players[context_game["game"][-1]]["bank"]=True


#resetear puntos
def resetPoints():
    write_log("resetPoints() iniciado")
    for i in context_game["game"]:
        players[i]["points"]=20

#llena diccionario players_game
def fill_player_game(player_game,gameID,*fields):
    write_log("fill_player_game() iniciado")
    player_game[gameID][fields[0]]={"initial_card":fields[1],"starting_points":fields[2],"ending_points":fields[3],"deck_id":fields[4]}


#llena diccionario player_game_round
def fill_player_game_round(player_game_round,round,*fields):
    player_game_round[round][fields[0]]={"is_bank":fields[1],"bet_points":fields[2],"starting_round_points":fields[3],"cards_value":fields[4],"ending_round_points":fields[5]}


#True si hay 2 o mas jugadores con mas puntos
def checkMinimun2PlayerWithPoints():
    cuenta=len(context_game["game"])
    return cuenta<2


#ordenar gamecontext por orden de prioridad
def orderAllPlayers():
    orden=[]
    for i in context_game["game"]:
        if not players[i]["bank"]:
            orden.append(i)
        else:
            mesa=i
    for i in range(len(orden)):
        for j in range(i+1,len(orden)):
            if players[orden[i]]["priority"]>players[orden[j]]["priority"]:
                orden[i],orden[j]=orden[j],orden[i]
    orden.append(mesa)
    context_game["game"]=orden


#apuestas dependiendo al tipo de jugador
def setBets():
    for i in context_game["game"]:
        if i!=context_game["game"][-1]:
            apuesta=players[i]["type"]//10
            if apuesta>players[i]["points"]:
                apuesta=players[i]["points"]
            puntos_de_banca=players[context_game["game"][-1]]["points"]

            if apuesta<=puntos_de_banca:
                players[i]["bet"]=apuesta
            else:
                players[i]["bet"]=puntos_de_banca


#calcula la chance de perder si cojes mas cartas
def calculaChance(id,mazo):
    puntos_ronda = players[id]["roundPoints"]

    # print(type(puntos_ronda),puntos_ronda)
    # print(players[id]["cards"])
    # print(len(mazo))
    halfcards=len(cartas)-28
    cartas_necesarias=((7-int(puntos_ronda))*4)+ (halfcards if 7.5-puntos_ronda>=0.5 else 0)


    cartas_para_pasarse=len(cartas)-cartas_necesarias
    # print(cartas_para_pasarse,"pasarse")
    chance_para_pasarse=(cartas_para_pasarse/len(cartas))*100

    return chance_para_pasarse


#devuelve true si terminaria eliminado despues dela ronda
def bank_eliminated(id):
    puntos_a_perder=0
    for i in context_game["game"]:
        if id!=i:
            if players[i]["roundPoints"]>players[id]["roundPoints"] and players[i]["roundPoints"]<=7.5:
                if players[i]["roundPoints"]==7.5:
                    puntos_a_perder+=players[i]["bet"]*2
                else:
                    puntos_a_perder+=players[i]["bet"]
            else:
                puntos_a_perder-=players[i]["bet"]

    return players[id]["points"]<=puntos_a_perder

#da true si nadie le gana ala banca
def bank_win(id):

    for i in context_game["game"]:
        if id!=i:
            if players[i]["roundPoints"]>players[id]["roundPoints"] and players[i]["roundPoints"]<=7.5:
                return False
    return True

#jugada automatica del jugador o comp
def standarRound(id,mazo):
    while True:
        chance=calculaChance(id,mazo)
        # print(chance)
        # input("")
        if not players[id]["bank"]:
            if chance<=players[id]["type"]:
                players[id]["cards"].append(mazo[-1])
                players[id]["roundPoints"]+=cartas[mazo[-1]]["realValue"]
                # print(players[id]["name"],"saco la carta",cartas[mazo[-1]]["literal"])
                mazo.pop(-1)
            else:
                # print("decide quedarse o perdio")
                break
        else:
            min=100
            for i in context_game["game"]:
                if i != id:
                    if players[i]["roundPoints"]>7.5:
                        min=0
                        break

                    elif players[i]["roundPoints"]<min:
                        min=players[i]["roundPoints"]

            perdiendo=min>players[id]["roundPoints"]

            # print(bank_eliminated(id))
            if (chance<=players[id]["type"] or perdiendo or bank_eliminated(id)) and not bank_win(id):
                players[id]["cards"].append(mazo[-1])
                players[id]["roundPoints"]+=cartas[mazo[-1]]["realValue"]
                # print(players[id]["name"],"saco la carta",cartas[mazo[-1]]["literal"])
                mazo.pop(-1)
            else:
                # print("pasa o perdio la mesa")
                break

#Realiza los pagos de las apuestas. - recursivo , requiere dnis de players context_game["game"]
def pay_day(lista):
    if len(lista)!=2:
        pay_day(lista[1:])

    if (players[context_game["game"][-1]]["roundPoints"]==7.5 or players[lista[0]]["roundPoints"]>7.5 or players[lista[0]]["roundPoints"]<=players[context_game["game"][-1]]["roundPoints"]) and players[context_game["game"][-1]]["roundPoints"]<=7.5:
        players[context_game["game"][-1]]["points"]+=players[lista[0]]["bet"]
        players[lista[0]]["points"]-=players[lista[0]]["bet"]
    else:
        if players[lista[0]]["roundPoints"]<=7.5:

            if players[lista[0]]["roundPoints"]==7.5:

                if players[lista[0]]["bet"]*2 >= players[context_game["game"][-1]]["points"]:
                    players[lista[0]]["points"]+=players[context_game["game"][-1]]["points"]
                    players[context_game["game"][-1]]["points"]=0
                else:
                    players[lista[0]]["points"]+=players[lista[0]]["bet"]*2
                    players[context_game["game"][-1]]["points"]-=players[lista[0]]["bet"]*2

            else:
                if players[lista[0]]["bet"]>=players[context_game["game"][-1]]["points"]:
                    players[lista[0]]["points"]+=players[context_game["game"][-1]]["points"]
                    players[context_game["game"][-1]]["points"]=0
                else:
                    players[lista[0]]["points"]+=players[lista[0]]["bet"]
                    players[context_game["game"][-1]]["points"]-=players[lista[0]]["bet"]



#Devuelve la lista de candidatos a banca y usa la funcion payday (realiza los pagos)
def distributionPointAndNewBankCandidates():
    bancas=[]
    for i in context_game["game"]:
        if players[i]["roundPoints"]==7.5:
            bancas.append(i)
    pay_day(context_game["game"])
    return bancas


# retorna las cartas usadas por un juegador
def cartas_usadas(id):
    carta = ""
    if len(players[id]["cards"]) != 0:
        for i in players[id]["cards"]:
            carta+=i+";"
        carta=carta[:-1]
    return carta

#stats jugador
def viewStats(id):
    datos="stats of {}".format(players[id]["name"]).center(FULL_SCREEN, "*") + "\n"
    for i in players_values:
        if i!="cards":
            datos+=" ".center(MARGIN_PLAYER) + i.ljust(PLAYER_SPACE) + str(players[id][i]) + "\n"
        else:
            datos+=" ".center(MARGIN_PLAYER) + i.ljust(PLAYER_SPACE) + str(cartas_usadas(id)) + "\n"
    input(datos)

#recoje values de todos los jugadores, (context_game["game"])
def recojerDatos(dato):
    datos=""
    for i in players_values:
        datos+=i.ljust(MARGIN_GAME_SCREEN)
        for j in range(3 if len(dato)>3 else len(dato)):
            if i != "cards":
                datos+=str(players[dato[j]][i]).ljust(GAME_SPACE)
            else:
                datos+=str(cartas_usadas(dato[j]).ljust(GAME_SPACE))
        datos+="\n"
    datos+="\n" +"_" * FULL_SCREEN + "\n"
    if len(dato)>3:
        datos+=recojerDatos(dato[3:])
    return datos


#printa los datos de todos
def gameStats(ronda=0,id=0):
    if id!=0:
        print("Round {}, Turno de {}".format(ronda, players[id]["name"]).center(FULL_SCREEN, "="))
    datos=recojerDatos(context_game["game"])
    datos+="Enter to continue".center(FULL_SCREEN)
    input(datos)

#retorna true si pide carta
def pedir_carta(id,mazo):
    if players[id]["roundPoints"] > 7.5:
        input("You have exceeded the score limit!".center(FULL_SCREEN)+"\n"+"Enter to continue".center(FULL_SCREEN))
    else:
        chance=calculaChance(id,mazo)
        if chance!=0:
            info="\n"+"".center(40)+f"The chance para exceed 7,5 = {chance} %"+"\n"+"".center(40)+"Are you sure do you want to order another card? Y/y = yes , another key = no\n"
            opcion=input(info).upper()
            if opcion == "Y":
                players[id]["cards"].append(mazo[-1])
                players[id]["roundPoints"]+=cartas[mazo[-1]]["realValue"]
                mazo.pop(-1)
        else:
            players[id]["cards"].append(mazo[-1])
            players[id]["roundPoints"] += cartas[mazo[-1]]["realValue"]
            mazo.pop(-1)

def bets(id):
    write_log("Iniciados Bets")
    if players[id]["bank"]:
        print("Cant bet if you are the bank".center(FULL_SCREEN))
        input("Enter to continue".center(FULL_SCREEN))
    elif players[id]["roundPoints"]!=0:
        print("Already pulled a card!".center(FULL_SCREEN))
        input("Enter to continue".center(FULL_SCREEN))
    else:
        while True:
            bet=input("".center(MARGIN_PLAYER) + f"Set the new bet ({1}-{players[id]["points"]}): ")
            if not bet.isdigit():
                print("Introduce only numbers!".center(FULL_SCREEN))
            elif int(bet) not in range(1,players[id]["points"]+1):
                print("The new bet has to be a number between 1 and {}".format(players[id]["points"]).center(FULL_SCREEN))
            else:
                players[id]["bet"]=int(bet)
                break

#quita roundpoints y las cartas
def limpia_datos():
    for i in context_game["game"]:
        players[i]["cards"]=[]
        players[i]["roundPoints"]=0

#elimina los jugadores que no tienen puntos
def kill_player():
    for i in range(len(context_game["game"])-1,-1,-1):
        if players[context_game["game"][i]]["points"]==0:
            if context_game["game"][i]==context_game["game"][-1]:
                players[context_game["game"][i]]["bank"],players[context_game["game"][i-1]]["bank"]=players[context_game["game"][i-1]]["bank"],players[context_game["game"][i]]["bank"]
            context_game["game"].remove(context_game["game"][i])


#ronda de humano
def humanRound(id,mazo_keys,ronda):
    opcion=0
    while opcion<5 and players[id]["roundPoints"]<7.5:
        roun="Round {}, Turno de {}".format(ronda, players[id]["name"]).center(FULL_SCREEN, "=") + "\n"
        hand=showMano(players[id]["cards"],cartas,players[id]["roundPoints"])
        opcion=menus_game(humanRound_menu,roun,hand)
        if opcion == 1:
            show_header_play_game()
            viewStats(id)
        elif opcion == 2:
            show_header_play_game()
            gameStats(ronda,id)
        elif opcion == 3:
            show_header_play_game()
            bets(id)
        elif opcion == 4:
            show_header_play_game()
            pedir_carta(id, mazo_keys)
        elif opcion == 5:

            standarRound(id, mazo_keys)
        else:
            print("")
    show_header_play_game()
    if players[id]["roundPoints"]>=7.5:
        print(roun+showMano(players[id]["cards"], cartas, players[id]["roundPoints"]))
        print("You got 7.5!".center(FULL_SCREEN) if players[id]["roundPoints"] == 7.5 else "You exceeded the score limit!".center(FULL_SCREEN))
        input("Enter to continue".center(FULL_SCREEN))
    else:
        print(roun+showMano(players[id]["cards"], cartas, players[id]["roundPoints"]))
        input("Enter to continue".center(FULL_SCREEN))
#jugar
def play_game():
    # print(cartas)
    # print(context_game["game"])
    if len(cartas)==0:
        input("First choose a deck!...".center(FULL_SCREEN))
        return
    elif checkMinimun2PlayerWithPoints():
        input("at least 2 players are needed!").center(FULL_SCREEN)
        return
    player_game = {}            # datos para exportar a  BBDD
    player_game_round = {}      # datos para exportar a BBDD
    cardGame = {}               # datos a exportar al BBDD


    rondas_jugadas=0
    setGamePriority(cartas.keys())
    resetPoints()
    orderAllPlayers()
    start_time=datetime.time(datetime.now())

    # guarda puntos iniciales del juego
    start_points_game = {}
    # print(context_game["game"])
    for i in context_game["game"]:
        start_points_game[i]=players[i]["points"]

    for ronda in range(1, context_game["round"] + 1):
        setBets()
        cartas_keys = barajeo_carta(cartas.keys())
        rondas_jugadas = ronda                      # rondas jugadas para cardGame

        #turnos de jugadores
        for i in context_game["game"]:
            if players[i]["human"]:
                humanRound(i, cartas_keys,ronda)
            else:
                standarRound(i, cartas_keys)
            show_header_play_game()
            gameStats(ronda,i)

        # fin dela ronda

        #guarda puntos iniciales de ronda
        start_points_round = {}
        for i in context_game["game"]:
            start_points_round[i] = players[i]["points"]

        #Realiza los pagos y devuelve la lista de posibles bancas
        bank_candidates = distributionPointAndNewBankCandidates()

        #crea el diccionario de la ronda
        player_game_round[ronda] = {}

        #rellena los datos de player_game_round
        write_log("fill_player_game_round() used")
        for i in context_game["game"]:
            fill_player_game_round(player_game_round, ronda, i, players[i]["bank"], players[i]["bet"], start_points_round[i],
                                   players[i]["roundPoints"], players[i]["points"])

        #Cambia la banca
        if len(bank_candidates) != 0:
            if bank_candidates[-1] != context_game["game"][-1]:
                players[bank_candidates[-1]]["bank"], players[context_game["game"][-1]]["bank"] = \
                players[context_game["game"][-1]]["bank"], players[bank_candidates[-1]]["bank"]

        show_header_play_game()
        print("Fin de la ronda {}.".format(ronda).center(FULL_SCREEN, "="))
        gameStats()
        limpia_datos()
        orderAllPlayers()
        kill_player()



        if checkMinimun2PlayerWithPoints():
            break

    # fin dela partida
    showWinner(rondas_jugadas)
    write_log("getID() used")
    game_id = getID()  # obtiene id dela BBDD
    cardGame.update({"cardgame_id": game_id, "players": len(start_points_game), "start_hour": start_time,"rounds": rondas_jugadas, "end_hour": datetime.time(datetime.now()),"deck_id":context_game["deck_id"]})


    #datos de player_game
    player_game[game_id]={}
    write_log("fill_player_game() used")
    for i in start_points_game.keys():
        player_game[game_id][i]={}
        fill_player_game(player_game,game_id,i,players[i]["initialCard"],start_points_game[i],players[i]["points"],context_game["deck_id"])

    # subir los datos dela partida ala BBDD
    # print(player_game)

    insertCardGame(cardGame)
    write_log("insertCardGame() used")
    insertarPlayGame(player_game)
    write_log("insertarPlayGame() used")
    insertarPlayGameRound(player_game_round,game_id)
    write_log("insertarPlayGameRound() used")



#ordenar lista ranked
def sorted_ranked(datos,keys,order_key):
    for i in range(len(keys)):
        for j in range(i+1,len(keys)):
            if datos[keys[i]][order_key]<datos[keys[j]][order_key]:
                keys[i],keys[j]=keys[j],keys[i]
    return keys

#opcion 4 ranking
def ranking():
    datos=get_ranking()
    keys = list(datos.keys())
    while True:
        show_header_rank()
        opcion=menus(ranking_menu)
        if opcion==1:
            keys=sorted_ranked(datos,keys,"earnings")
        elif opcion==2:
            keys = sorted_ranked(datos, keys, "games_played")
        elif opcion==3:
            keys = sorted_ranked(datos, keys, "minutes_played")
        else:
            break
        encabezado= ("*" * RANK_SIZE).center(FULL_SCREEN) + "\n" + \
                    ("NIF".ljust(13)+"Name".ljust(25)+"Earnings".rjust(10)+"Games Played".rjust(15)+"Minutes Played".rjust(17)).center(FULL_SCREEN) + "\n" + \
                    ("*" * RANK_SIZE).center(FULL_SCREEN) + "\n"
        exit=False
        pagina=0
        show_max=10
        while not exit:
            rank=encabezado
            #many = cantidad de personas que mostrara
            if show_max*pagina+10>len(keys):
                many=len(keys)-show_max*pagina
            else:
                many=10

            for i in range(show_max*pagina,(show_max*pagina)+many):
                rank+= (keys[i].ljust(13)+datos[keys[i]]["name"].ljust(25)+str(datos[keys[i]]["earnings"]).rjust(10)+str(datos[keys[i]]["games_played"]).rjust(15)+str(datos[keys[i]]["minutes_played"]).rjust(17)).center(FULL_SCREEN) + "\n"

            msg="exit to go Rankings:"
            if pagina-1>=0:
                msg="- to go back, "+msg
            if show_max*pagina+many+1<=len(keys):
                msg="+ to go ahead, "+msg
            while True:
                show_header_rank()
                opc=input(rank+"\n"+" ".ljust(20)+msg).upper()
                if opc == "-" and "-" in msg:
                    pagina -= 1
                    break
                elif opc == "+" and "+" in msg:
                    pagina += 1
                    break
                elif opc == "EXIT":
                    exit = True
                    break
                else:
                    print("Invalid Option".center(FULL_SCREEN, "="))
                    input("Press enter to continue".center(FULL_SCREEN))



def showActualPlayers():
    dato=" ".center(50)+"Actual Players in game".center(61,"*")+"\n"
    for i in context_game["game"]:
        dato+=" ".center(52)+i.ljust(13)+players[i]["name"].ljust(25)+("human" if players[i]["human"]==1 else "Boot").ljust(10)+tipo[players[i]["type"]]+"\n"
    show_header_select_players()
    input(dato+"\n"+"Enter to continue...".rjust(72))

def setGamePlayers():
    exit=False
    showActualPlayers()
    data=datos_jugadores()
    cabezera="Select Players".center(FULL_SCREEN, "=") + "\n" +\
            "Boot Players".center(HALF_SCREEN) + "||" + "Human Players".center(HALF_SCREEN) + "\n" +\
            "".center(FULL_SCREEN, "-") + "\n"\
            "ID".ljust(25) + "Name".ljust(25) + "Type".ljust(26) + "||" + "ID".ljust(25) + "Name".ljust(25) + "Type".ljust(25) + "\n" + \
             "".center(FULL_SCREEN, "=") + "\n"
    while not exit:
        info=cabezera
        human=[]
        bot=[]
        for i in data:
            if i not in context_game["game"]:
                if data[i]["human"]:
                    human.append(i)
                else:
                    bot.append(i)
        largo_min=(len(human) if len(human)<len(bot) else len(bot))
        for i in range(largo_min):
            info+=bot[i].ljust(25)+data[bot[i]]["name"].ljust(25)+tipo[data[bot[i]]["type"]].ljust(25)+"||"+human[i].ljust(25)+data[human[i]]["name"].ljust(25)+tipo[data[human[i]]["type"]].ljust(25)+"\n"
        if largo_min==len(human):
            for i in range(largo_min,len(bot)):
                info+=bot[i].ljust(25)+data[bot[i]]["name"].ljust(25)+tipo[data[bot[i]]["type"]].ljust(25)+"||"+"\n"
        else:
            for i in range(largo_min, len(human)):
                info+=" ".ljust(75)+"||"+human[i].ljust(25)+data[human[i]]["name"].ljust(25)+tipo[data[human[i]]["type"]].ljust(25)+"\n"
        info+="=".center(FULL_SCREEN) + "\n" + "Option (id to add to game, -id to remove player, sh to show actual players in game, -1 to go back:".center(FULL_SCREEN)
        while True:
            show_header_select_players()
            opcion=input(info).upper()
            if len(opcion)<1:
                input("Invalid Option".center(FULL_SCREEN) + "\n" + "Enter to continue".center(FULL_SCREEN))
            elif opcion[0]=="-" and opcion[1:]=="1":
                exit=True
                break
            elif opcion[0]=="-" and opcion[1:] in context_game["game"]:
                context_game["game"].remove(opcion[1:])
                showActualPlayers()
                break
            elif opcion[0]!="-" and opcion in data.keys() and opcion not in context_game["game"]:
                context_game["game"].append(opcion)
                showActualPlayers()
                break
            elif opcion=="SH":
                showActualPlayers()
            else:
                input("Invalid Option".center(FULL_SCREEN) + "\n" + "Enter to continue".center(FULL_SCREEN))
def set_cards_deck():
    write_log("set_cards_deck() used")
    selected_deck=get_cards_deck()
    choosen_cards = {}
    context_game["deck_id"] = selected_deck[0][5]
    for k in selected_deck:
        choosen_cards[k[0]] = {"literal": k[1], "value": k[2], "priority": k[3], "realValue": k[4]}
    # print(choosen_cards)
    # input("")
    cartas.clear()
    cartas.update(choosen_cards)

def setRounds():
    write_log("setRounds() used")
    while True:
        show_header_select_rounds()
        rounds=input(" ".ljust(70)+"Max Round: ")
        if not rounds.isdigit():
            input(" ".ljust(70)+"Please, select a number."+"\n"+" ".ljust(70) + "Enter to continue")

        elif int(rounds) not in range(1,21):
            input(" ".ljust(70)+"The max rounds has to be  between 0 and 20"+"\n"+" ".ljust(70) + "Enter to continue")
        else:
            input(" ".ljust(70)+f"Established maximum of rounds to {rounds}"+"\n"+" ".ljust(70) + "Enter to continue")
            context_game["round"]=int(rounds)
            break
def setting():
    while True:
        show_header_dinamic("settings")
        opcion=menus(settings_menu)
        if opcion==1:
            setGamePlayers()
        elif opcion==2:
            set_cards_deck()
        elif opcion==3:
            setRounds()
        else:
            break

def add_show_remove_players():
    while True:
        show_header_bbdd_players()
        opt = menus(player_menu)
        if opt == 1:
            set_human_player()
        elif opt == 2:
            set_bot_player()
        elif opt == 3:
            show_remove_players()
        else:
            break


def SevenandHalf():
    try:
        write_log("Inicio Sesion")
        while True:
            show_header_main_menu()
            opcion=menus(main_menu)
            if opcion==1:
                write_log("add_show_remove() used")
                add_show_remove_players()
            elif opcion==2:
                write_log("setting() used")
                setting()
            elif opcion==3:
                write_log("play_game() used")
                play_game()
                write_log("play_game() end")
            elif opcion==4:
                write_log("ranking() used")
                ranking()
                write_log("ranking() end")
            elif opcion==5:
                write_log("reports() used")
                reports()
                write_log("reports() end")
            else:
                write_log("Cierre Sesion")
                break
    except Exception as error:
        write_log(f"interrupt End sesion{error}","ERROR")


# Muestra las cosultas datos=select_query() campos=["nombre de los campos"]
def showConsultas(datos,campos, opcion):
    generate_xml(datos, campos, "consulta" + str(opcion) + ".xml")
    cantidad_datos=len(datos)-1
    full_size=0
    tamaños=[]
    for i in campos:
        full_size+=len(i)+5
        tamaños.append(len(i)+5)

    encabezado = ("*" * full_size).center(FULL_SCREEN) + "\n"
    data=""
    for i in range(len(campos)):
        data+=campos[i].ljust(tamaños[i])
    encabezado+= data.center(FULL_SCREEN) + "\n" + ("*" * full_size).center(FULL_SCREEN) + "\n"
    exit=False
    pagina=0
    show_max = 10
    pagina_final=((cantidad_datos//show_max) if cantidad_datos%show_max==0 else (cantidad_datos//show_max)+1)
    while not exit:
        rank=encabezado
        #many = cantidad de personas que mostrara
        if show_max*pagina+show_max>cantidad_datos:
            many=cantidad_datos+1-(show_max*pagina)
        else:
            many=show_max
        for i in range(show_max*pagina,(show_max*pagina)+many):
            info=""
            for j in range(len(datos[i])):
                info+=str(datos[i][j]).ljust(tamaños[j])
            rank+= info.center(FULL_SCREEN) + "\n"
        rank+=(f"Page {pagina+1}/{pagina_final}".center(full_size,"-")).center(FULL_SCREEN)
        msg="exit to go Rankings:"
        if pagina-1>=0:
            msg="- to go back, "+msg
        if show_max*pagina+many+1<=cantidad_datos:
            msg="+ to go ahead, "+msg


        espacio_question=int((HALF_SCREEN) - (full_size / 2))

        while True:
            show_header_reports()
            opc=input(rank+"\n"+" ".ljust(espacio_question)+msg).upper()
            if opc == "-" and "-" in msg:
                pagina -= 1
                break
            elif opc == "+" and "+" in msg:
                pagina += 1
                break
            elif opc == "EXIT":
                exit = True
                break
            else:
                print("Invalid Option".center(FULL_SCREEN, "="))
                input("Press enter to continue".center(FULL_SCREEN))

def reports():
    while True:
        show_header_reports()
        opcion=menus(reports_menu)
        if opcion==11:
            break
        elif opcion not in consultas.keys():
            input("Loading...".center(FULL_SCREEN))
        elif opcion==6:
            show_header_reports()
            opcion=menus(reports_menu_6)
            if opcion!=3:
                # if opcion==1:
                #     data = select_query(consultas[6.1][0])
                #     showConsultas(data, consultas[6.1][1], 6.1)
                # else:
                data = select_query(consultas[6.2][0])
                showConsultas(data, consultas[6.2][1], 6.2)
        else:
            data=select_query(consultas[opcion][0])
            showConsultas(data,consultas[opcion][1], opcion)


#printa las cartas que tengas
def showMano(cards,cartas,points):
    canti=len(cards)
    if canti!=0:
        largo=10*canti
        a="\n" + (("┍"+"".center(8,"━")+"┑")*canti).center(FULL_SCREEN) + "\n"
        b=""
        for i in cards:
            b+="│"+i.ljust(8)+"│"
        a+= b.center(FULL_SCREEN) + "\n" + ("│        │" * canti).center(FULL_SCREEN) + "\n"
        b=""
        for i in cards:
            b += "│" + str(cartas[i]["realValue"]).rjust(8) + "│"
        a+= b.center(FULL_SCREEN) + "\n" + (("┕" + "".center(8, "─") + "┙") * canti).center(FULL_SCREEN) + "\n" + (f"Total value={points}".center(largo)).center(FULL_SCREEN) + "\n"
        return a
    return ""

def showWinner(round):
    points=0
    for i in context_game["game"]:
        if players[i]["points"]-20>points:
            points=players[i]["points"]
            winner=i
    show_header_game_over()
    print(f"The winner is {winner} - {players[winner]["name"]} in {round} rounds , with {points} points".center(FULL_SCREEN))
    input("".center(FULL_SCREEN))