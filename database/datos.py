from database.fun_datos import *
from datetime import datetime
cartas= {}              #cartas dela base de datos+
players=datos_jugadores()           #jugadores de base de datos
# total_de_cartas=len(cartas)         #Numero de cartas


#agregar jugadores nuevos context_game["game"]=["jugadores nuevos"]

# context_game={"game":[],"round":1}   #diccionario global de uso

#contex_game para pruebas
context_game={"game":list(players.keys())[:4],"round":1,"deck_id":1}   #diccionario global de uso


# Tamaño de menus
tamaño_pantalla=150   #divisores de 50
media_pantalla=75
margen_player=int(tamaño_pantalla*0.4)
espaciado_player=int(tamaño_pantalla*0.1)

margen_game=int(tamaño_pantalla*0.1)
espaciado_game=int(tamaño_pantalla*0.3)

rank_tamaño=90

players_values=("name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints")
tipo= {30:"Cautious",40:"Moderated",50:"Bold"}
#tamaño de menus

max_players=6

# LISTAS PARA GENERAR LOS MENÚS DEL JUEGO
humanRound_menu=["View Stats","View Game Stats","Set Bet","Order Card","Automatic Play","Stand"]

main_menu = ["Add/Remove/Show Players", "Settings", "Play Game", "Ranking", "Reports", "Exit"]
settings_menu = ["Set Game Players", "Set Card's Deck", "Set Max Rounds (Default 5 Rounds)", "Go Back"]
ranking_menu =  ["Player With More Earnings", "Players With More Games Played", "Players With More Minutes Played", "Go Back"]
reports_menu = ["Initial card more repeated by each user, \nonly users who have played a minimum of 3 games.",
                "Player who makes the highest bet per game,\nfind the round with the highest bet",
                "Player who makes the lowest bet per game.",
                "Percentage of rounds won per player in each game\n(%), as well as their average bet for the game.",
                "List of games won by Bots",
                "Rounds won by the bank in each game.",
                "Number of users have been the bank in each game.",
                "Average bet per game",
                "Average bet of the first round of each game.",
                "Average bet of the last round of each game.",
                "Go back"]



