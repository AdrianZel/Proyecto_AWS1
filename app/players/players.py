from app.players.headers import *
from app.players.utils import (print_data_two, print_from_two_lists, set_dni_validate, generar_dni_bot,
                               dni_validate, get_confirm, get_profile_name, set_name, set_profile_player)
from database.datos import (insertaPlayer, datos_jugadores, players, deletePlayer, FULL_SCREEN,MARGIN_SCREEN)

def set_human_player():
    """
    Crear jugador en base de datos y actualizar el diccionario de jugadores.
    """
    global players
    list_data = []

    # Add Name
    show_header_nhp()
    name = set_name()
    list_data.append(('Name', name))

    # Add DNI
    show_header_nhp()
    print_data_two(list_data)

    dni = set_dni_validate()
    list_data.append(('Dni', dni))

    # Add Profile
    show_header_nhp()
    print_data_two(list_data)

    profile = set_profile_player()
    list_data.append(('Profile', get_profile_name(profile)))

    # Confirm
    show_header_nhp()
    print_data_two(list_data)
    confirm = get_confirm()
    if confirm:
        player = [dni, name, profile, 1]
        insertaPlayer(player)
        players.clear()
        players.update(datos_jugadores())

        print(MARGIN_SCREEN + "{} has been created as a human player".format(name))

def set_bot_player():
    """
    Crear jugador Bot en base de datos y actualizar el diccionario de jugadores.
    Se utiliza la función generar_dni_bot, que genera uno aleatorio.
    """
    global players
    list_data = []
    show_header_add_bot_player()
    print_data_two(list_data)

    # Add Name
    name = set_name()
    dni = generar_dni_bot()
    list_data.append(('Name', name))
    list_data.append(('Dni', dni))

    # Set Profile
    show_header_add_bot_player()
    print_data_two(list_data)
    profile = set_profile_player()

    # Add Name
    list_data.append(('Profile', get_profile_name(profile)))
    show_header_add_bot_player()
    print_data_two(list_data)

    # Confirm
    confirm = get_confirm()
    if confirm:
        player = [dni, name, profile, 0]
        insertaPlayer(player)
        players.clear()
        players.update(datos_jugadores())
        print(MARGIN_SCREEN + "{} has been created as a bot player".format(name))

def show_remove_players():
    global players

    show_header_sr_player()
    if not (type(players) is dict):
        players.clear()
        players.update(datos_jugadores())

    list_bots = []
    list_humans = []

    for key, value in players.items():
        if value['human']:
            list_humans.append((key, value['name'], get_profile_name(value['type'])))
        else:
            list_bots.append((key, value['name'], get_profile_name(value['type'])))

    max_length = len(list_humans) if len(list_humans) > len(list_bots) else len(list_bots)
    print_from_two_lists(("ID", "Name", "Type"), ("ID", "Name", "Type"))

    print(ASTERISKS_LINE)

    for i in range(max_length):
        if not i < len(list_bots):
            print_from_two_lists((' ', ' ', ' '), list_humans[i])
        elif not i < len(list_humans):
            print_from_two_lists(list_bots[i], (' ', ' ', ' '))
        else:
            print_from_two_lists(list_bots[i], list_humans[i])

    print(ASTERISKS_LINE)

    remove_player_listen = remove_player()
    if remove_player_listen:
        players.clear()
        players.update(datos_jugadores())

    input(MARGIN_SCREEN + "Enter to Continue")


def remove_player():
    global players
    msg_opt="Option ( -id to remove player, -1 to exit):"
    print(MARGIN_SCREEN + msg_opt)
    dni = input( MARGIN_SCREEN + " " )
    while not ((dni == "-1") or (dni[:1] == "-" and dni_validate(dni[1:]) and dni[1:] in players.keys())):
        print(" Invalid Option ".center(FULL_SCREEN,"="))

        input("Enter to Continue")

        print(MARGIN_SCREEN + msg_opt)
        dni = input(MARGIN_SCREEN + " ")

    player_name = players[dni[1:]]['name']

    if dni == "-1":
        return False
    else:
        deletePlayer(dni[1:])
        print(MARGIN_SCREEN + "{} has been deleted".format(player_name))
        return True
