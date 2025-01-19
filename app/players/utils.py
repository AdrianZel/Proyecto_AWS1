import random
from database.datos import select_profile_menu, players, FULL_SCREEN
from app.fun import menus

def setName():
    name = input("Name: ")
    while not (name.isalpha()):
        print("Incorrect name, please, enter a name not empty with only letters")
        input("Enter to Continue")
        name = input("Name: ")
    return name

def generar_dni_bot():
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numDni = random.randint(10000000, 99999999)
    letra = letras[numDni % 23]
    dni = f"{numDni}{letra}"

    while dni in players.keys():
        numDni = random.randint(10000000, 99999999)
        letra = letras[numDni % 23]
        dni = f"{numDni}{letra}"

    return dni

def calcular_letra_dni(numero_dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[int(numero_dni) % 23]


def dniValidate(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    if len(dni) == 9 and dni[:-1].isdigit() and dni[-1].isalpha():
        return letras[int(dni[:-1]) % 23] == dni[-1].upper()
    return False

def setDniValidate():
    global players

    dni = input("Enter new DNI: ")

    dni_exists = True if dni in players.keys() else False

    while not (dniValidate(dni) and not dni_exists):
        if not dni.isalnum():
            print("Incorrect format")
        elif not len(dni) == 9:
            print("Incorrect length")
        elif not dni[:8].isdigit():
            print("The first 8 characters of DNI are numbers")
        elif not dni[8:].isalpha():
            print("DNI has to end with a letter")
        elif dni in players.keys():
            print("DNI already exists")
        elif not dni[8:] == calcular_letra_dni(dni[:8]):
            print("Incorrect DNI letter")

        dni = input("Enter new DNI: ")

        dni_exists = True if dni in players.keys() else False

    return dni

def get_confirm():
    confirm = input("Is ok? Y/n")

    while not (confirm.isalpha() and len(confirm)==1 and
               (confirm== 'Y' or confirm== 'n')):
        print(" Invalid Option ".center(FULL_SCREEN,"="))
        input("Enter to Continue")
        confirm = input("Is ok? Y/n")

    return confirm == 'Y'

def setProfilePlayer():
    print("\nSelect your Profile:")
    option = menus(select_profile_menu)
    if option == 1:
        return 30
    elif option == 2:
        return 40
    else:
        return 50


def getProfileName(value_profile):
    if value_profile == 50:
        return select_profile_menu[2]
    elif value_profile == 40:
        return select_profile_menu[1]
    elif value_profile == 30:
        return select_profile_menu[0]

def print_data_two(showdata):
    for i in range(len(showdata)):
        print("{}".format(showdata[i][0].ljust(10)), showdata[i][1])

def print_from_two_lists(list1, list2):
    print("{}{}{}|| {}{}{}".format(list1[0].ljust(21),
                                   list1[1].ljust(26),
                                   list1[2].ljust(26),
                                   list2[0].ljust(21),
                                   list2[1].ljust(26),
                                   list2[2].ljust(26)))