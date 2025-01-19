import pymysql


#recolectar datos del SQL y devuelve la arrays (lista de tuplas)
def select_query(query):
    try:
        # Conexión a la base de datos
        connection = pymysql.connect(
            host='thesevenarmy.mysql.database.azure.com',
            user='chayanne',
            password='Qu13r0#S3r#T0r3r0!',
            database='sevenandhalf'
        )
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar la consulta
        with connection.cursor() as cursor:
            # Consulta
            cursor.execute(query)

            # Obtener los resultados de la consulta
            results = cursor.fetchall()

            return results

    except pymysql.MySQLError as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()
            print("Conexión cerrada")

#para insertar a base de datos many=1 si insertaras varias rows
def insert_query(query,data,many=1):
    # Conexión a la base de datos
    try:
        conn = pymysql.connect(
            host='thesevenarmy.mysql.database.azure.com',
            user='chayanne',
            password='Qu13r0#S3r#T0r3r0!',
            database='sevenandhalf',
        )
        cursor = conn.cursor()

        # Insertar datos en la tabla partida
        if many==1:
            cursor.executemany(query,data)
        else:
            cursor.execute(query,data)

        conn.commit()  # Confirmar los cambios
        print("Datos insertados en la tabla partida")

    except pymysql.MySQLError as e:
        print("Error al insertar datos:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()

def datos_jugadores():
    datos=select_query("select * from player")
    players = {}
    for row in datos:
        players[row[0]] = {"name": row[1], "human": row[3], "bank": False, "initialCard": "", "priority": 0,
                           "type": row[2], "bet": 4, "points": 0, "cards": [], "roundPoints": 0}
    return players

def insertarPlayGame(player_game):
    data = []
    for i in player_game:
        for j in player_game[i]:
            data.append((i, j, player_game[i][j]["initial_card"], player_game[i][j]["starting_points"],
                           player_game[i][j]["ending_points"],player_game[i][j]["deck_id"]))
    query="""
    INSERT INTO player_game (game_id, nif, initial_card, starting_points, ending_points,deck_id)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    insert_query(query,data)

def insertCardGame(cardGame):
    data = (cardGame["cardgame_id"],cardGame["players"],cardGame["start_hour"],cardGame["rounds"],cardGame["end_hour"],cardGame["deck_id"])
    query="""
    INSERT INTO game (game_id, number_of_players, start_time, rounds, end_time, deck_id)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    insert_query(query,data,0)


def insertarPlayGameRound(player_game_round, game_id):
    data = []
    for i in player_game_round:
        for j in player_game_round[i]:
            data.append((game_id, i, j, player_game_round[i][j]["is_bank"], player_game_round[i][j]["bet_points"],
                           player_game_round[i][j]["starting_round_points"], player_game_round[i][j]["cards_value"],player_game_round[i][j]["ending_round_points"]))

    query="""
            INSERT INTO player_round_game (game_id, round_id, nif, is_bank, bet, starting_round_points, card_points, ending_round_points)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """
    insert_query(query,data)

def insertaPlayer(player):
    query="""
        INSERT INTO player (nif, name, type, human) VALUES (%s,%s,%s,%s) 
    """
    insert_query(query, player,0)

def deletePlayer(nif):
    query="""
        DELETE FROM player WHERE nif = %s
    """
    insert_query(query, (nif,),0)


def getID():
    dato=select_query("select max(game_id) from game")
    dato = list(dato)[0][0]
    if dato == None:
        dato = 1
    else:
        dato = int(dato) + 1

    return dato

def get_ranking():
    query="""
    SELECT o.nif,o.name,sum(e.ending_points-e.starting_points),count(p.game_id),sum(timestampdiff(second,p.start_time,p.end_time)/60) FROM player o
    join player_game e on o.nif=e.nif
    join game p on p.game_id=e.game_id
    group by o.nif,o.name
    """
    dato=select_query(query)
    # print(dato)
    # input()
    rank={}
    for i in dato:
        rank[i[0]]={"name": i[1], "earnings": i[2], "games_played": i[3], "minutes_played": i[4]}
    return rank

# Función para definir el deck con el que se jugará la partida
def get_cards_deck():
    # las opciones (esto se usará luego con la función de menús)
    print("\n--- Set Card's Deck ---")
    dato=select_query("select * from deck")
    question=""
    for i in dato:
        question=str(i[0])+") " + i[1] + ": " + i[2]
        print(question)
    while True:
        option = input("Choose a deck (1-3): ")
        if option.isdigit() and int(option) >= 1 and int(option) <= 3:
            option = int(option)
            if option == 1:
                print(str(dato[option-1][1]) + " selected.")
                break
            elif option == 2:
                print(str(dato[option-1][1]) + " selected.")
                break
            elif option == 3:
                print(str(dato[option-1][1]) + " selected.")
                break
        else:
            print("Invalid option. Please choose a number between 1 and 3.")
    selected_deck = select_query(f"select * from card WHERE deck_id = {option}")
    return selected_deck

