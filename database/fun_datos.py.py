import pyodbc

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

#recolectar datos del SQL y agregarlos al diccionario players
def datos_jugadores():
    players={}
    try:
        conn = pyodbc.connect("Driver={MySQL ODBC 9.1 ANSI Driver};"
                              "Server=localhost;"
                              "Database=cartas;"
                              "User=root;"
                              "Password=adrian;"
                              "Trusted_Connection=yes")
        if conn:
            print("coneccion")
        cursor=conn.cursor()

        #query
        cursor.execute("select * from jugador")
        #guardamos los datos en los jugadores
        for jugador in cursor:
            players[jugador[0]]={"name":jugador[1], "human": jugador[3], "bank": False, "initialCard": "", "priority": 0, "type": jugador[2], "bet": 0, "points": 0,"cards": [], "roundPoints": 0}

    finally:
        if conn:
            conn.close()
            print("Coneccion cerrada")
        return players

#insertar play_game ala BBDD
def insertarPlayGame(player_game):
    values=[]
    for i in player_game:
        for j in player_game[i]:
            values.append((i,j,player_game[i][j]["initial_card"],player_game[i][j]["starting_points"],player_game[i][j]["ending_points"]))
    try:
        conn = pyodbc.connect("Driver={MySQL ODBC 9.1 ANSI Driver};"
                              "Server=localhost;"
                              "Database=cartas;"
                              "User=root;"
                              "Password=adrian;"
                              "Trusted_Connection=yes")
        if conn:
            print("coneccion")
        cursor = conn.cursor()

        # Insertar datos en la tabla ronda
        query_ronda = """
            INSERT INTO jugador_partida (id_partida, nif, carta_inicial, puntos_inicial, puntos_final)
            VALUES (?, ?, ?, ?, ?)
            """
        cursor.executemany(query_ronda, values)
        conn.commit()  # Confirmar los cambios
        print("Datos insertados en la tabla ronda")

    except pyodbc.Error as e:
        print("Error al insertar datos:", e)

    finally:
        if conn:
            conn.close()

# insertar play_game_round ala BBDD
def insertarPlayGameRound(player_game_round,game_id):
    values=[]
    for i in player_game_round:
        for j in player_game_round[i]:
            values.append((game_id,i,j,player_game_round[i][j]["is_bank"],player_game_round[i][j]["bet_points"],player_game_round[i][j]["starting_round_points"],player_game_round[i][j]["cards_value"],player_game_round[i][j]["ending_round_points"]))
    try:
        conn = pyodbc.connect("Driver={MySQL ODBC 9.1 ANSI Driver};"
                              "Server=localhost;"
                              "Database=cartas;"
                              "User=root;"
                              "Password=adrian;"
                              "Trusted_Connection=yes")
        if conn:
            print("coneccion")
        cursor = conn.cursor()

        # Insertar datos en la tabla ronda
        query_ronda = """
            INSERT INTO jugador_partida_ronda (id_partida, id_ronda, nif, es_banca, apuesta, puntos_ronda_inicial, puntos_ronda_final, puntos_cartas)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

        cursor.executemany(query_ronda, values)
        conn.commit()  # Confirmar los cambios
        print("Datos insertados en la tabla ronda")

    except pyodbc.Error as e:
        print("Error al insertar datos:", e)

    finally:
        if conn:
            conn.close()

#insertar cardgame a la BBDD
def insertCardGame(cardGame):

    values = (cardGame["cardgame_id"],cardGame["players"],cardGame["start_hour"],cardGame["rounds"],cardGame["end_hour"])

    try:
        conn = pyodbc.connect("Driver={MySQL ODBC 9.1 ANSI Driver};"
                              "Server=localhost;"
                              "Database=cartas;"
                              "User=root;"
                              "Password=adrian;"
                              "Trusted_Connection=yes")
        if conn:
            print("coneccion")
        cursor = conn.cursor()

        # Insertar datos en la tabla ronda
        query_ronda = """
            INSERT INTO partida (id_partida, jugadores, hora_inicio, rondas, hora_fin)
            VALUES (?, ?, ?, ?, ?)
            """

        cursor.execute(query_ronda, values)
        conn.commit()  # Confirmar los cambios
        print("Datos insertados en la tabla ronda")

    except pyodbc.Error as e:
        print("Error al insertar datos:", e)

    finally:
        if conn:
            conn.close()

#obtener la bbdd
def getIdGame():
    try:
        conn = pyodbc.connect("Driver={MySQL ODBC 9.1 ANSI Driver};"
                              "Server=localhost;"
                              "Database=cartas;"
                              "User=root;"
                              "Password=adrian;"
                              "Trusted_Connection=yes")
        if conn:
            print("coneccion")
        cursor=conn.cursor()
        #query
        cursor.execute("select max(id_partida) from partida")

        id=list(cursor)[0][0]
        if id==None:
            id=1
        else:
            id=int(id)+1

        return id

    finally:
        if conn:
            conn.close()
            print("Coneccion cerrada")
