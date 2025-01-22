from database.fun_datos import *
cartas= {}              #cartas dela base de datos+
players=datos_jugadores()           #jugadores de base de datos
# total_de_cartas=len(cartas)         #Numero de cartas


#agregar jugadores nuevos context_game["game"]=["jugadores nuevos"]

# context_game={"game":[],"round":1}   #diccionario global de uso

#contex_game para pruebas
context_game={"game":list(players.keys())[:4],"round":5,"deck_id":1}   #diccionario global de uso


# Tamaño de menus

FULL_SCREEN = 150   #divisores de 50
ASTERISKS_LINE = "*" * FULL_SCREEN
HORIZONTAL_LINE = "-" * FULL_SCREEN
HALF_SCREEN = int(FULL_SCREEN*0.5)
MARGIN_SCREEN = " ".center(int(FULL_SCREEN*0.4))

MARGIN_PLAYER=int(FULL_SCREEN * 0.4)
PLAYER_SPACE=int(FULL_SCREEN * 0.1)

MARGIN_GAME_SCREEN=int(FULL_SCREEN * 0.1)
GAME_SPACE=int(FULL_SCREEN * 0.3)

RANK_SIZE=90

players_values=("name","type","human","bank","initialCard","priority","bet","points","cards","roundPoints")
tipo= {30:"Cautious",40:"Moderated",50:"Bold"}
#tamaño de menus


# LISTAS PARA GENERAR LOS MENÚS DEL JUEGO
humanRound_menu=["View Stats","View Game Stats","Set Bet","Order Card","Automatic Play","Stand"]

main_menu = ["Add/Remove/Show Players", "Settings", "Play Game", "Ranking", "Reports", "Exit"]
player_menu = ["New Human Player","New Boot","Show/Remove Players","Go back"]
select_profile_menu = ["Cautious", "Moderated", "Bold"]
settings_menu = ["Set Game Players", "Set Card's Deck", "Set Max Rounds (Default 5 Rounds)", "Go Back"]
ranking_menu =  ["Player With More Earnings", "Players With More Games Played", "Players With More Minutes Played", "Go Back"]
reports_menu = ["Initial card more repeated by each user, \n" +" ".center(MARGIN_PLAYER + 3) + "only users who have played a minimum of 3 games." + "\n",
                "Player who makes the highest bet per game,\n" +" ".center(MARGIN_PLAYER + 3) + "find the round with the highest bet" + "\n",
                "Player who makes the lowest bet per game." +"\n",
                "Percentage of rounds won per player in each game\n" +" ".center(MARGIN_PLAYER + 3) + "(%), as well as their average bet for the game." + "\n",
                "List of games won by Bots" +"\n",
                "Rounds won by the bank in each game." +"\n",
                "Number of users have been the bank in each game." +"\n",
                "Average bet per game" +"\n",
                "Average bet of the first round of each game." +"\n",
                "Average bet of the last round of each game." +"\n",
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
             6:"",
             1:["""
            WITH Carta_Repetida AS (
    SELECT 
        nif AS identificador_jugador,
        initial_card AS carta_inicial_mas_repetida,
        COUNT(initial_card) AS veces_repetida,
        COUNT(DISTINCT game_id) AS total_partidas_jugadas
    FROM player_game WHERE nif IN (SELECT nif FROM player_game GROUP BY nif HAVING COUNT(DISTINCT game_id) >= 3) GROUP BY nif, initial_card),
    Max_Repetida AS (SELECT identificador_jugador,MAX(veces_repetida) AS max_repetida FROM Carta_Repetida GROUP BY identificador_jugador)
SELECT 
    cr.identificador_jugador,
    cr.carta_inicial_mas_repetida,
    cr.veces_repetida,
    cr.total_partidas_jugadas
FROM Carta_Repetida cr
JOIN Max_Repetida mr
ON cr.identificador_jugador = mr.identificador_jugador AND cr.veces_repetida = mr.max_repetida
ORDER BY cr.identificador_jugador, cr.carta_inicial_mas_repetida;
             """,["nif        ","Most apear Card","Numbers appers","Total games"]],
             5:["""
             WITH Bot_Scores AS (SELECT pg.game_id, pg.nif AS bot_nif, (pg.ending_points - pg.starting_points) AS score_difference
FROM player_game pg
JOIN player p
ON pg.nif = p.nif
WHERE p.human = false),
Winning_Bots AS (SELECT bs.game_id, bs.bot_nif, bs.score_difference
FROM Bot_Scores bs
JOIN (SELECT game_id, MAX(score_difference) AS max_score
FROM Bot_Scores
GROUP BY game_id) max_scores ON bs.game_id = max_scores.game_id AND bs.score_difference = max_scores.max_score)
SELECT wb.game_id AS partida_id, wb.bot_nif AS ganador_bot, wb.score_difference AS diferencia_puntos
FROM Winning_Bots wb
ORDER BY wb.game_id;
             """,["ID game","BOT code","Points won"]],
             6.2:["""
             SELECT prg.game_id AS partida_id,
COUNT(CASE WHEN prg.is_bank = true AND prg.ending_round_points > prg.starting_round_points THEN 1 ELSE NULL END) AS rondas_ganadas_banca
FROM player_round_game prg
GROUP BY prg.game_id
ORDER BY prg.game_id;
             """,["ID game","Rounds won"]]
             }

