import pyodbc
from datetime import datetime
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
        conn= pyodbc.connect("Driver={MySQL ODBC 9.1 ANSI Driver};"
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
            players[jugador[0]]={"name":jugador[1], "human": jugador[3], "bank": False, "initialCard": "", "priority": 0, "type": jugador[2], "bet": 4, "points": 0,"cards": [], "roundPoints": 0}

    finally:
        if conn:
            conn.close()
            print("Coneccion cerrada")
        return players

cartas=datos_cartas()               #cartas dela base de datos+
players=datos_jugadores()           #jugadores de base de datos
player_game={}                      #datos para exportar a  sql
player_game_round={}                #datos para exportar a sql
game=[]                             #Jugadores que jugaran
total_de_cartas=len(cartas)         #Numero de cartas
context_game={"game":list(players.keys()),"round":[]}   #diccionario global de uso





