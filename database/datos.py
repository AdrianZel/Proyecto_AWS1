from database.fun_datos import *
cartas= {}              #cartas dela base de datos+
players=datos_jugadores()           #jugadores de base de datos
# total_de_cartas=len(cartas)         #Numero de cartas


#agregar jugadores nuevos context_game["game"]=["jugadores nuevos"]

# context_game={"game":[],"round":1}   #diccionario global de uso

#contex_game para pruebas
context_game={"game":list(players.keys())[:4],"round":1,"deck_id":1}   #diccionario global de uso


# Tamaño de menus
tamaño_pantalla=150   #divisores de 50
FULL_SCREEN = 150   #divisores de 50
ASTERISKS_LINE = "*" * FULL_SCREEN
HORIZONTAL_LINE = "-" * FULL_SCREEN
HALF_SCREEN = int(FULL_SCREEN*0.5)
MARGIN_SCREEN = " ".center(int(FULL_SCREEN*0.4))
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
player_menu = ["New Human Player","New Boot","Show/Remove Players","Go back"]
select_profile_menu = ["Cautious", "Moderated", "Bold"]
settings_menu = ["Set Game Players", "Set Card's Deck", "Set Max Rounds (Default 5 Rounds)", "Go Back"]
ranking_menu =  ["Player With More Earnings", "Players With More Games Played", "Players With More Minutes Played", "Go Back"]
reports_menu = ["Initial card more repeated by each user, \n"+" ".center(margen_player+3)+"only users who have played a minimum of 3 games."+"\n",
                "Player who makes the highest bet per game,\n"+" ".center(margen_player+3)+"find the round with the highest bet"+"\n",
                "Player who makes the lowest bet per game."+"\n",
                "Percentage of rounds won per player in each game\n"+" ".center(margen_player+3)+"(%), as well as their average bet for the game."+"\n",
                "List of games won by Bots"+"\n",
                "Rounds won by the bank in each game."+"\n",
                "Number of users have been the bank in each game."+"\n",
                "Average bet per game"+"\n",
                "Average bet of the first round of each game."+"\n",
                "Average bet of the last round of each game."+"\n",
                "Go back"]

reports_menu_6=["Rounds won by the bank in each game. Distinguishing user.","Rounds won by the bank in each game. Without distinguishing user.","Go back."]
consultas = {3: ["""
    SELECT 
        prg.game_id AS partida_id, 
        prg.nif AS jugador_id, 
        prg.bet AS apuesta_mas_baja
    FROM 
        player_round_game prg
    WHERE 
        prg.bet = (
            SELECT MIN(sub_prg.bet)
            FROM player_round_game sub_prg
            WHERE sub_prg.game_id = prg.game_id
        )
    ORDER BY 
        prg.game_id;

        """, ["ID Game", "ID Player", "Lower bet"]],

             2: ["""
           SELECT 
    prg.game_id AS partida_id, 
    prg.nif AS jugador_id, 
    prg.bet AS apuesta_mas_alta
FROM 
    player_round_game prg
WHERE 
    prg.bet = (
        SELECT MAX(sub_prg.bet)
        FROM player_round_game sub_prg
        WHERE sub_prg.game_id = prg.game_id
    )
ORDER BY 
    prg.game_id;
           """, ["ID Game", "ID Player", "Higher bet"]],

             4: ["""
           WITH round_winners AS (
    SELECT
        prg.game_id AS partida_id,
        prg.round_id AS ronda_id,
        prg.nif AS jugador_id,
        MAX(prg.ending_round_points - prg.starting_round_points) AS max_diferencia
    FROM
        player_round_game prg
    GROUP BY
        prg.game_id, prg.round_id, prg.nif
),
player_wins AS (
    SELECT
        prg.game_id AS partida_id,
        prg.nif AS jugador_id,
        COUNT(rw.ronda_id) AS rondas_ganadas
    FROM
        player_round_game prg
    LEFT JOIN (
        SELECT
            partida_id,
            ronda_id,
            jugador_id
        FROM
            round_winners
    ) rw
    ON
        prg.game_id = rw.partida_id
        AND prg.round_id = rw.ronda_id
        AND prg.nif = rw.jugador_id
    GROUP BY
        prg.game_id, prg.nif
),
player_stats AS (
    SELECT
        prg.game_id AS partida_id,
        prg.nif AS jugador_id,
        COUNT(DISTINCT prg.round_id) AS total_rondas,
        AVG(prg.bet) AS apuesta_media
    FROM
        player_round_game prg
    GROUP BY
        prg.game_id, prg.nif
)
SELECT
    ps.partida_id AS identificador_partida,
    ps.jugador_id AS identificador_jugador,
    ps.total_rondas AS rondas_partida,
    ps.apuesta_media AS apuesta_media,
    COALESCE(pw.rondas_ganadas, 0) AS rondas_ganadas_jugador,
    ROUND(COALESCE(pw.rondas_ganadas, 0) * 100.0 / ps.total_rondas, 2) AS porcentaje_ganadas
FROM
    player_stats ps
LEFT JOIN
    player_wins pw
ON
    ps.partida_id = pw.partida_id
    AND ps.jugador_id = pw.jugador_id
ORDER BY
    ps.partida_id, ps.jugador_id;
           """, ["ID Game", "ID Player", "Rounds", "Avg bet", "Wins", "Winrate"]],
             7: ["""
           SELECT prg.game_id, count(prg.nif) 
from player_round_game prg where prg.is_bank = 1 group by prg.game_id order by count(prg.nif);
           """, ["ID game", "Count bank Users"]],
             8: ["""
           SELECT 
    prg.game_id AS identificador_partida,
    AVG(prg.bet) AS apuesta_media
FROM 
    player_round_game prg
GROUP BY 
    prg.game_id
ORDER BY 
    prg.game_id;
           """, ["ID game", "Avg bet"]],
             9: ["""
           SELECT 
    prg.game_id AS partida_id, 
    AVG(prg.bet) AS apuesta_media
FROM 
    player_round_game prg
WHERE 
    prg.round_id = 1
GROUP BY 
    prg.game_id;

           """, ["ID game", "First round's avg bet"]],
             10: ["""
           SELECT 
prg.game_id AS partida_id, 
AVG(prg.bet) AS apuesta_media
FROM 
    player_round_game prg
WHERE 
    prg.round_id = (
        SELECT MAX(sub_prg.round_id)
        FROM player_round_game sub_prg
        WHERE sub_prg.game_id = prg.game_id
    )
GROUP BY 
    prg.game_id;
           """, ["ID game", "Last round's avg bet"]],
             6:""
             }

