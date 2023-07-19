#BattleShip

def battleship() :
    
    import colorama
    from colorama import Fore
    
    round = 1
    computer_round = 1
    import random
    user_ship_location = None
    computer_ship_location = None
    board_size = None
    try_again = None
    
    while True:
        try:
            board_size = int(input("What size board would you like? (under 20) "))
        except ValueError:
            print("Please type only whole numbers below 20")
            continue

        if board_size > 20:
            print("please type only a whole number below 20")
            board_size = int(input("What size board would you like? (under 20) "))
            
            
        if board_size < 1:
            print("Please type a whole number greater than 0")
            board_size = int(input("What size board would you like? (under 20) "))
            
                
        break
        
    def ask():
        decision = input("Are you ready to play Battle ship? :(y/n) ")
        if decision == "y":
            print("Now we shall begin with this glorious exercise testing ones strengh and wit")
        elif decision == "n":
            print("OK, goodbye you bum piece of poopoo crap now GTFO")
            exit()
        else: 
            print("Hell to daw naw, to daw naw naw naw- no please enter either y or n")
            decision = input("Are you ready to play Battle ship? :(y/n) ")
        
        decision2 = input("Do you want your ships location to be random? :(y/n) ")
        if decision2 == "y":
            row2 = random.randrange(0,board_size)
            colm2 = random.randrange(0,board_size)
            user_ship_location = (row2, colm2)
        elif decision2 == "n":
            row2 = int(input("What row would you like the ship to be placed?: "))
            colm2 = int(input("What column would you like the ship to be placed?: "))
            user_ship_location = (row2, colm2)
        else:
            print("bro wth are you doing just pick a damn row and column :")
            decision2 = input("Do you want the ships location to be random? :(y/n) ")
        
        return row2, colm2, user_ship_location
        
    row2, colm2, user_ship_location = ask()
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print("You have choosen," ,user_ship_location, "as your ship location")
    def computer_ask():
        row4 = random.randrange(0,board_size)
        colm4 = random.randrange(0,board_size)
        computer_ship_location = (row4, colm4)
        return computer_ship_location
    
    computer_ship_location = computer_ask()
    print(computer_ship_location)

    ArrayUser = []
    
    for x in range(board_size):
        ArrayUser.append([Fore.BLUE + "O"] * board_size)
        
    ArrayComputer = []
    
    for x in range(board_size):
        ArrayComputer.append([Fore.BLUE + "O"] * board_size)

    def printboard(ArrayUser):
        for row in ArrayUser:
            print(" ".join(row))
            
    def printboard(ArrayComputer):
        for row in ArrayComputer:
            print(" ".join(row))
            
    ArrayUser[row2][colm2] = (Fore.WHITE + "S")

    row = 0
    colm = 0
    user_guesslist = []
    computer_row = 0
    computer_colm = 0
    computer_guesslist = []
        
    while True:
        while True:
            while round < 6 and computer_round >= round :
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print (Fore.WHITE + "Round", round)
                printboard(ArrayComputer)
                print(Fore.WHITE + "**************")
                
                while True:
                    try:
                        row = int(input(Fore.WHITE + "Please guess a row : "))
                    except ValueError:
                        print(Fore.WHITE + "Please type only whole numbers that coorelate to the board size")
                        continue
                    if row in (range(board_size)):
                        print(Fore.WHITE + "**************")
                    else:
                        if row != (range(board_size)):
                            print(Fore.WHITE + "Good try sucker now enter whooe numbers that coorelate to the board size")
                            row = int(input(Fore.WHITE + "Please guess a row : "))
                    break
    
                while True:
                    try:
                        colm = int(input(Fore.WHITE + "Please guess a column : "))
                    except ValueError:
                        print(Fore.WHITE + "Please type only whole numbers that coorelate to the board size")
                        continue
                    if colm in (range(board_size)):
                        print(Fore.WHITE + "***************")
                    else:
                        if colm != (range(board_size)):
                            print(Fore.WHITE + "Good try sucker now enter only whole numbers that coorelate to the board size")
                            colm = int(input(Fore.WHITE + "Please guess a column : "))
                    break
                list= (row, colm)
                user_guesslist.append(list)
                print(Fore.WHITE + "These are the guesses that have been made so far:", user_guesslist)
        
                if ArrayComputer[row][colm] == "O":
                    print(Fore.WHITE + "**********")
                else:
                    print(Fore.WHITE + "You already chose that coordinate!")
        
                if list == computer_ship_location:
                    print(Fore.WHITE + "Dang you hit the computers Battle Ship")
                    ArrayComputer[row][colm] = (Fore.GREEN + "X")
                    printboard(ArrayComputer)
                    print(Fore.WHITE + "Congraulations, you have beaten my very hard game of Battle Ship")
                    try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")
                    if try_again == "y":
                        battleship()
                    elif try_again == "n":
                        print(Fore.WHITE + "Ok loser, now GTFO of my code")
                        exit()
                    else:
                        print(Fore.WHITE + "Please type y or n you dumdum poopoo head")
                        try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")

                else:
                    print(Fore.WHITE + "You missed! Try again!")
                    ArrayUser[row][colm] = (Fore.RED + "M")
                    
                round +=1
                
                if round > 6 and list == computer_ship_location:
                    print(Fore.WHITE + "Dang you lucky son of a gun you got it. Congrats you win")
                    continue
                    
            while round < 6 and computer_round <= round :
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print (Fore.WHITE + "Computer Round", computer_round)
                printboard(ArrayUser)
                computer_row = random.randrange(0,board_size)
                computer_colm = random.randrange(0,board_size)
        
                computer_list= (computer_row, computer_colm)
                computer_guesslist.append(computer_list)
                print(Fore.WHITE + "These are the guesses the computer made:", computer_guesslist)
                computer_round += 1
        
                if ArrayUser[computer_row][computer_colm] == "O":
                    print(Fore.WHITE + "**********")
                else:
                    computer_row = random.randrange(0,board_size)
                    computer_colm = random.randrange(0,board_size)
        
                if computer_list == user_ship_location:
                    print(Fore.WHITE + "The computer has hit your battleship!")
                    ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                    printboard(ArrayUser)
                    print(Fore.WHITE + "You suck, your bum self lost to the stupid coomputer")
                    try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")
                    if try_again == "y":
                        battleship()
                    elif try_again == "n":
                        print(Fore.WHITE + "Ok loser, now GTFO of my code")
                        exit()
                    else:
                        print(Fore.WHITE + "Please type y or n you dumdum poopoo head")
                        try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")

                else:
                    print(Fore.WHITE + "The computer missed, youve survived another round")
                    ArrayComputer[computer_row][computer_colm] = (Fore.RED + "M")
                    
                if round > 6 and computer_list == user_ship_location:
                    print(Fore.WHITE + "Dang you suck so much you lost on the last round. MUAH HA HA HA HA HA HA")
                    continue
                break


battleship()
