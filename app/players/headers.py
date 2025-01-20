""" Cabeceras utilizadas la administaración de jugadores"""

import os
from database.datos import HALF_SCREEN, ASTERISKS_LINE, HORIZONTAL_LINE, FULL_SCREEN

os.environ["TERM"] = "xterm"

def show_header_bbdd_players() -> None:
    """
    Cabecera menú inicial de jugadores
    :return: cabecera
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASTERISKS_LINE + "\n")
    print(r"""
                                  ____   ____   ____   ____     ____   __                                                                   
                                 / __ ) / __ ) / __ \ / __ \   / __ \ / /____ _ __  __ ___   _____ _____                                    
                                / __  |/ __  |/ / / // / / /  / /_/ // // __ `// / / // _ \ / ___// ___/                                    
                               / /_/ // /_/ // /_/ // /_/ /  / ____// // /_/ // /_/ //  __// /   (__  )                                     
                              /_____//_____//_____//_____/  /_/    /_/ \__,_/ \__, / \___//_/   /____/                                      
                                                                             /____/                                                                                                                                          

    """)
    print(ASTERISKS_LINE + "\n")


def show_header_nhp() -> None:
    """
    Cabecera crear nuevo player humano
    :return: cabecera
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASTERISKS_LINE)
    print(r"""
                          _   __                  __  __                                   ____   __                                            
                         / | / /___  _      __   / / / /__  __ ____ ___   ____ _ ____     / __ \ / /____ _ __  __ ___   _____                   
                        /  |/ // _ \| | /| / /  / /_/ // / / // __ `__ \ / __ `// __ \   / /_/ // // __ `// / / // _ \ / ___/                   
                       / /|  //  __/| |/ |/ /  / __  // /_/ // / / / / // /_/ // / / /  / ____// // /_/ // /_/ //  __// /                       
                      /_/ |_/ \___/ |__/|__/  /_/ /_/ \__,_//_/ /_/ /_/ \__,_//_/ /_/  /_/    /_/ \__,_/ \__, / \___//_/                        
                                                                                                        /____/                                  
    """)
    print(ASTERISKS_LINE)


def show_header_add_bot_player() -> None:
    """
    Cabecera opcion crear player bot
    :return: Cabecera
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASTERISKS_LINE)
    print(r"""
                                _   __                  ____          __     ____   __                                                      
                               / | / /___  _      __   / __ ) ____   / /_   / __ \ / /____ _ __  __ ___   _____                             
                              /  |/ // _ \| | /| / /  / __  |/ __ \ / __/  / /_/ // // __ `// / / // _ \ / ___/                             
                             / /|  //  __/| |/ |/ /  / /_/ // /_/ // /_   / ____// // /_/ // /_/ //  __// /                                 
                            /_/ |_/ \___/ |__/|__/  /_____/ \____/ \__/  /_/    /_/ \__,_/ \__, / \___//_/                                  
                                                                                          /____/                                            
    """)
    print(ASTERISKS_LINE)


def show_header_sr_player() -> None:
    """
    Cabecera para la opción de mostrar y borrar jugadores
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ASTERISKS_LINE)
    print(
        r"""
          _____  __                            ____                                         ____   __                                       
         / ___/ / /_   ____  _      __        / __ \ ___   ____ ___   ____  _   __ ___     / __ \ / /____ _ __  __ ___   _____ _____        
         \__ \ / __ \ / __ \| | /| / /______ / /_/ // _ \ / __ `__ \ / __ \| | / // _ \   / /_/ // // __ `// / / // _ \ / ___// ___/        
        ___/ // / / // /_/ /| |/ |/ //_____// _, _//  __// / / / / // /_/ /| |/ //  __/  / ____// // /_/ // /_/ //  __// /   (__  )         
       /____//_/ /_/ \____/ |__/|__/       /_/ |_| \___//_/ /_/ /_/ \____/ |___/ \___/  /_/    /_/ \__,_/ \__, / \___//_/   /____/          
                                                                                                         /____/                             
        """
    )
    print(ASTERISKS_LINE)
    print("Select Players".center(FULL_SCREEN , "*"))
    print("Boot Players".center(HALF_SCREEN-3), "|| ","Human Players".center(HALF_SCREEN)  )
    print(HORIZONTAL_LINE)

def show_header_main_menu() -> None:
    """
    Cabecera para menú inicial
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(HORIZONTAL_LINE)
    print(r"""
                  ███████╗███████╗██╗   ██╗███████╗███╗   ██╗     █████╗ ███╗   ██╗██████╗     ██╗  ██╗ █████╗ ██╗     ███████╗
                  ██╔════╝██╔════╝██║   ██║██╔════╝████╗  ██║    ██╔══██╗████╗  ██║██╔══██╗    ██║  ██║██╔══██╗██║     ██╔════╝
                  ███████╗█████╗  ██║   ██║█████╗  ██╔██╗ ██║    ███████║██╔██╗ ██║██║  ██║    ███████║███████║██║     █████╗  
                  ╚════██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║    ██╔══██║██║╚██╗██║██║  ██║    ██╔══██║██╔══██║██║     ██╔══╝  
                  ███████║███████╗ ╚████╔╝ ███████╗██║ ╚████║    ██║  ██║██║ ╚████║██████╔╝    ██║  ██║██║  ██║███████╗██║     
                  ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     
    """)
    print(HORIZONTAL_LINE)
    print()