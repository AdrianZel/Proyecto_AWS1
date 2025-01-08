def menus(lista):
    while True:
        for i in range(len(lista)):
            print(str(i+1) + ") " + lista[i])
        opt = input("\n-> Opcion: ")
        if not opt.isdigit():
            print("Invalid Option. Please, use a number.")
            input("Press enter to continue.\n")
        elif int(opt) not in range(1, len(lista)+1):
            print("Out of range. Please, choose a number between 1 and" + " " + str(len(lista))+ ".")
            input("Press enter to continue.\n")
        else:
            opt = int(opt)
            return opt
