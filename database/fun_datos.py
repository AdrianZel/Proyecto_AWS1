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
        #print("Conexión exitosa a la base de datos")

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
            #print("Conexión cerrada")

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
        #print("Datos insertados en la tabla partida")

    except pymysql.MySQLError as e:
        print("Error al insertar datos:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()


#obtener datos dela carta
def datos_cartas():
    cartas = {"O01": {"literal": "1 de Oros", "value": 1, "priority": 4, "realValue": 1},
              "O02": {"literal": "2 de Oros", "value": 2, "priority": 4, "realValue": 2},
              "O03": {"literal": "3 de Oros", "value": 3, "priority": 4, "realValue": 3},
              "O04": {"literal": "4 de Oros", "value": 4, "priority": 4, "realValue": 4},
              "O05": {"literal": "5 de Oros", "value": 5, "priority": 4, "realValue": 5},
              "O06": {"literal": "6 de Oros", "value": 6, "priority": 4, "realValue": 6},
              "O07": {"literal": "7 de Oros", "value": 7, "priority": 4, "realValue": 7},
              "O08": {"literal": "8 de Oros", "value": 8, "priority": 4, "realValue": 0.5},
              "O09": {"literal": "9 de Oros", "value": 9, "priority": 4, "realValue": 0.5},
              "O10": {"literal": "10 de Oros", "value": 10, "priority": 4, "realValue": 0.5},
              "O11": {"literal": "11 de Oros", "value": 11, "priority": 4, "realValue": 0.5},
              "O12": {"literal": "12 de Oros", "value": 12, "priority": 4, "realValue": 0.5},
              "O13": {"literal": "13 de Oros", "value": 13, "priority": 4, "realValue": 0.5},

              "C01": {"literal": "1 de Copas", "value": 1, "priority": 3, "realValue": 1},
              "C02": {"literal": "2 de Copas", "value": 2, "priority": 3, "realValue": 2},
              "C03": {"literal": "3 de Copas", "value": 3, "priority": 3, "realValue": 3},
              "C04": {"literal": "4 de Copas", "value": 4, "priority": 3, "realValue": 4},
              "C05": {"literal": "5 de Copas", "value": 5, "priority": 3, "realValue": 5},
              "C06": {"literal": "6 de Copas", "value": 6, "priority": 3, "realValue": 6},
              "C07": {"literal": "7 de Copas", "value": 7, "priority": 3, "realValue": 7},
              "C08": {"literal": "8 de Copas", "value": 8, "priority": 3, "realValue": 0.5},
              "C09": {"literal": "9 de Copas", "value": 9, "priority": 3, "realValue": 0.5},
              "C10": {"literal": "10 de Copas", "value": 10, "priority": 3, "realValue": 0.5},
              "C11": {"literal": "11 de Copas", "value": 11, "priority": 3, "realValue": 0.5},
              "C12": {"literal": "12 de Copas", "value": 12, "priority": 3, "realValue": 0.5},
              "C13": {"literal": "13 de Copas", "value": 13, "priority": 3, "realValue": 0.5},

              "E01": {"literal": "1 de Espadas", "value": 1, "priority": 2, "realValue": 1},
              "E02": {"literal": "2 de Espadas", "value": 2, "priority": 2, "realValue": 2},
              "E03": {"literal": "3 de Espadas", "value": 3, "priority": 2, "realValue": 3},
              "E04": {"literal": "4 de Espadas", "value": 4, "priority": 2, "realValue": 4},
              "E05": {"literal": "5 de Espadas", "value": 5, "priority": 2, "realValue": 5},
              "E06": {"literal": "6 de Espadas", "value": 6, "priority": 2, "realValue": 6},
              "E07": {"literal": "7 de Espadas", "value": 7, "priority": 2, "realValue": 7},
              "E08": {"literal": "8 de Espadas", "value": 8, "priority": 2, "realValue": 0.5},
              "E09": {"literal": "9 de Espadas", "value": 9, "priority": 2, "realValue": 0.5},
              "E10": {"literal": "10 de Espadas", "value": 10, "priority": 2, "realValue": 0.5},
              "E11": {"literal": "11 de Espadas", "value": 11, "priority": 2, "realValue": 0.5},
              "E12": {"literal": "12 de Espadas", "value": 12, "priority": 2, "realValue": 0.5},
              "E13": {"literal": "13 de Espadas", "value": 13, "priority": 2, "realValue": 0.5},


              "B01": {"literal": "1 de Bastos", "value": 1, "priority": 1, "realValue": 1},
              "B02": {"literal": "2 de Bastos", "value": 2, "priority": 1, "realValue": 2},
              "B03": {"literal": "3 de Bastos", "value": 3, "priority": 1, "realValue": 3},
              "B04": {"literal": "4 de Bastos", "value": 4, "priority": 1, "realValue": 4},
              "B05": {"literal": "5 de Bastos", "value": 5, "priority": 1, "realValue": 5},
              "B06": {"literal": "6 de Bastos", "value": 6, "priority": 1, "realValue": 6},
              "B07": {"literal": "7 de Bastos", "value": 7, "priority": 1, "realValue": 7},
              "B08": {"literal": "8 de Bastos", "value": 8, "priority": 1, "realValue": 0.5},
              "B09": {"literal": "9 de Bastos", "value": 9, "priority": 1, "realValue": 0.5},
              "B10": {"literal": "10 de Bastos", "value": 10, "priority": 1, "realValue": 0.5},
              "B11": {"literal": "11 de Bastos", "value": 11, "priority": 1, "realValue": 0.5},
              "B12": {"literal": "12 de Bastos", "value": 12, "priority": 1, "realValue": 0.5},
              "B13": {"literal": "13 de Bastos", "value": 13, "priority": 1, "realValue": 0.5}
              }
    return cartas
import pymysql


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
                           player_game[i][j]["ending_points"]))
    query="""
    INSERT INTO player_game (game_id, nif, initial_card, starting_points, ending_points)
    VALUES (%s,%s,%s,%s,%s)
    """
    insert_query(query,data)

def insertCardGame(cardGame):
    data = (cardGame["cardgame_id"],cardGame["players"],cardGame["start_hour"],cardGame["rounds"],cardGame["end_hour"],1)
    query="""
    INSERT INTO game (game_id, number_of_players, start_time, rounds, end_time, deck)
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

def getID():
    dato=select_query("select max(game_id) from game")
    dato = list(dato)[0][0]
    if dato == None:
        dato = 1
    else:
        dato = int(dato) + 1

    return dato


def set_max_rounds():
    print("\n--- Set Max Rounds ---")
    while True:
        max_rounds = input("Enter the number of maximum rounds (1-30): ")
        if max_rounds.isdigit():
            max_rounds = int(max_rounds)
            if max_rounds >= 1 and max_rounds <= 30:
                print(f"Maximum rounds set to {max_rounds}.")
                context_game["round"]=max_rounds
                break
            else:
                print("Please enter a number between 1 and 30.")
        else:
            print("Invalid input. Please enter a number.")