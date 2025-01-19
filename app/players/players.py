from app.players.headers import *
from app.players.utils import print_data_two, print_from_two_lists
from utils import (setDniValidate, generar_dni_bot, dniValidate, get_confirm,
                   setProfilePlayer, getProfileName, setName)
from app.fun import menus
from database.datos import (main_menu, player_menu, insertaPlayer,
                            datos_jugadores, players, deletePlayer, FULL_SCREEN)


"""
Bloque para aplicar los cambios de usuarios
"""
print(players)
players=datos_jugadores()
print(players)
"""
Fin bloque de cambios
"""
def initializeMenu():
    global players
    while True:
        showHeaderStart()
        option = menus(main_menu)
        if option ==1:
            showHeaderBBDDPlayers()
            opt = menus(player_menu)
            arm_players(opt)

def arm_players(option):
    global players

    if option == 1:
        listData = []

        # Add Name
        showHeaderNHP()
        print_data_two(listData)
        name = setName()
        listData.append(('Name', name))

        # Add DNI
        showHeaderNHP()
        print_data_two(listData)

        dni = setDniValidate()
        listData.append(('Dni', dni))

        # Add Profile
        showHeaderNHP()
        print_data_two(listData)

        profile = setProfilePlayer()
        listData.append(('Profile', getProfileName(profile)))

        # Confirm
        showHeaderNHP()
        print_data_two(listData)
        confirm = get_confirm()
        if confirm:
            player = [dni, name, profile, 1]
            insertaPlayer(player)
            players.clear()
            players.update(datos_jugadores())


    elif option == 2:
        listData = []
        showHeaderNBP()
        print_data_two(listData)

        # Add Name
        name = setName()
        dni = generar_dni_bot()
        listData.append(('Name', name))
        listData.append(('Dni', dni))

        # Set Profile
        showHeaderNBP()
        print_data_two(listData)
        profile = setProfilePlayer()

        # Add Name
        listData.append(('Profile', getProfileName(profile)))
        showHeaderNBP()
        print_data_two(listData)

        # Confirm
        confirm = get_confirm()
        if confirm:
            player = [dni, name, profile, 0]
            insertaPlayer(player)
            players.clear()
            players.update(datos_jugadores())

    elif option == 3:

        showHeaderSRPlayer()
        if not (type(players) is dict):
            players.clear()
            players.update(datos_jugadores())

        list_bots = []
        list_humans = []

        for key, value in players.items():
            if value['human']:
                list_humans.append((key, value['name'], getProfileName(value['type'])))
            else:
                list_bots.append((key, value['name'], getProfileName(value['type'])))

        max_length = len(list_humans) if len(list_humans) > len(list_bots) else len(list_bots)
        print_from_two_lists(("ID","Name","Type"),("ID","Name","Type"))

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


        input("Enter to Continue")


def remove_player():
    global players
    print("Option ( -id to remove player, -1 to exit):".center(FULL_SCREEN))
    dni = input( " ".center(HALF_SCREEN-22) )
    while not ((dni == "-1") or (dni[:1] == "-" and dniValidate(dni[1:]) and dni[1:] in players.keys()) ):
        print(" Invalid Option ".center(FULL_SCREEN,"="))

        input("Enter to Continue")

        print("Option ( -id to remove player, -1 to exit):".center(FULL_SCREEN))
        dni = input(" ".center(HALF_SCREEN -22))

    player_name = players[dni[1:]]['name']

    if dni == "-1":
        return False
    else:
        deletePlayer(dni[1:])
        print("{} has been deleted".format(player_name))
        return True


initializeMenu()