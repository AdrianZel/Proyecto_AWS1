""" Cabeceras utilizadas la administaración de jugadores"""

import os
from database.datos import HALF_SCREEN, ASTERISKS_LINE, HORIZONTAL_LINE, FULL_SCREEN

os.environ["TERM"] = "xterm"

def show_header_bbdd_players() -> None:
    show_header_dinamic(title="players")
    """
    Cabecera menú inicial de jugadores
    :return: cabecera
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(ASTERISKS_LINE + "\n")
    # print(r"""
    #                                 ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗
    #                                 ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝
    #                                 ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████╗
    #                                 ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║
    #                                 ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║███████║
    #                                 ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
    #
    # """)
    # print(ASTERISKS_LINE + "\n")


def show_header_nhp() -> None:
    show_header_dinamic(title="new human player")
    """
    Cabecera crear nuevo player humano
    :return: cabecera
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(ASTERISKS_LINE)
    # print(r"""
    #
    #                                     ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗
    #                                     ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝
    #                                     ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████╗
    #                                     ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║
    #                                     ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║███████║
    #                                     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
    #
    #                             ███╗   ██╗███████╗██╗    ██╗    ██╗  ██╗██╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
    #                             ████╗  ██║██╔════╝██║    ██║    ██║  ██║██║   ██║████╗ ████║██╔══██╗████╗  ██║
    #                             ██╔██╗ ██║█████╗  ██║ █╗ ██║    ███████║██║   ██║██╔████╔██║███████║██╔██╗ ██║
    #                             ██║╚██╗██║██╔══╝  ██║███╗██║    ██╔══██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    #                             ██║ ╚████║███████╗╚███╔███╔╝    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    #                             ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    #
    # """)
    # print(ASTERISKS_LINE)


def show_header_add_bot_player() -> None:
    show_header_dinamic(title="New bot player")
    """
    Cabecera opcion crear player bot
    :return: Cabecera
    """
    # os.system('cls' if os.name == 'nt' else 'clear')
    # print(ASTERISKS_LINE)
    # print(r"""
    #
    #                                     ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗
    #                                     ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝
    #                                     ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████╗
    #                                     ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║
    #                                     ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║███████║
    #                                     ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
    #
    #                                     ███╗   ██╗███████╗██╗    ██╗    ██████╗  ██████╗ ████████╗
    #                                     ████╗  ██║██╔════╝██║    ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
    #                                     ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██████╔╝██║   ██║   ██║
    #                                     ██║╚██╗██║██╔══╝  ██║███╗██║    ██╔══██╗██║   ██║   ██║
    #                                     ██║ ╚████║███████╗╚███╔███╔╝    ██████╔╝╚██████╔╝   ██║
    #                                     ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝     ╚═════╝  ╚═════╝    ╚═╝
    #
    # """)
    # print(ASTERISKS_LINE)


def show_header_sr_player() -> None:
    """
    Cabecera para la opción de mostrar y borrar jugadores
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASTERISKS_LINE)
    print(
        r"""
                             
                                        ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ ███████╗                                
                                        ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝                                
                                        ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝███████╗                                
                                        ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗╚════██║                                
                                        ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║███████║                                
                    ███████╗██╗  ██╗ ██████╗ ██╗╚═══██╗╝╚═╝  ╚═╝   ╚═██████╗═███████╗███╗╚══███╗╝██████╗ ██╗   ██╗███████╗       
                    ██╔════╝██║  ██║██╔═══██╗██║    ██║              ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝       
                    ███████╗███████║██║   ██║██║ █╗ ██║    █████╗    ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗         
                    ╚════██║██╔══██║██║   ██║██║███╗██║    ╚════╝    ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝         
                    ███████║██║  ██║╚██████╔╝╚███╔███╔╝              ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗       
                    ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝               ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝       
        """
    )
    print(ASTERISKS_LINE)
    print("Select Players".center(FULL_SCREEN , "*"))
    print("Boot Players".center(HALF_SCREEN-3), "|| ","Human Players".center(HALF_SCREEN)  )
    print(HORIZONTAL_LINE)

def show_header_main_menu() -> None:
    show_header_dinamic(title="Seven And Half")

def show_header_game_over() -> None:
    show_header_dinamic(title="Game Over")

def show_header_settings() -> None:
    show_header_dinamic(title="Settings")


def show_header_play_game() -> None:
    show_header_dinamic(title="Play Game")

def show_header_rankings() -> None:
    show_header_dinamic(title="Rankings")


def show_header_reports() -> None:
    show_header_dinamic(title="Reports")

def show_header_dinamic(title="Reports") -> None:
    """
    Cabecera dinamica
    """
    import pyfiglet
    font = pyfiglet.Figlet(font="ansi_shadow")
    header = font.renderText(title)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(HORIZONTAL_LINE)

    for line in header.splitlines():
        print(line.center(FULL_SCREEN))

    print(HORIZONTAL_LINE)
    print()
