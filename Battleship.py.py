#BattleShip

def battleship() :
    
    import colorama
    from colorama import Fore
    #all these varibles must be defined 
    round = 1
    computer_round = 1
    import random
    user_sub_location = None
    user_destoryer_location = None
    user_sub_location2 = None
    user_destoryer_location2 = None
    computer_sub_location = None
    computer_sub_location2 = None
    computer_destoryer_location = None
    computer_destoryer_location2 = None
    board_size = None
    try_again = None
    
    while True:
        try:
            board_size = int(input("What size board would you like? (at least 10 but under 25) "))
        except ValueError:
            print("Please type only whole numbers that are at least 10 but below 25")
            continue

        if board_size > 25:
            print("Please type only a whole number that is at least 10 but below 25")
            board_size = int(input("What size board would you like? (at least 10 but under 25) "))
            
            
        if board_size < 10:
            print("Please type a whole number that is at least 10 but below 25")
            board_size = int(input("What size board would you like? (at least 10 but under 25) "))
            
                
        break
        
    def ask():
        decision = input("Are you ready to play Battle ship? :(y/n) ")
        if decision == "y":
            print("Now we shall begin with this glorious exercise testing ones strengh and wit")
        elif decision == "n":
            print("OK, goodbye")
            exit()
        else: 
            print("Please either type y or n")
            decision = input("Are you ready to play Battle ship? :(y/n) ")
        
        decision2 = input("Do you want your Submarine's location to be random? :(y/n) ")
        if decision2 == "y":
            row2 = random.randrange(0,board_size)
            colm2 = random.randrange(0,board_size)
            user_sub_location = (row2, colm2)
            user_sub_location2 = (row2, colm2 + 1)
        elif decision2 == "n":
            row2 = int(input("What row would you like the Submarine to be placed?: "))
            colm2 = int(input("What column would you like the Submarine to be placed?: "))
            user_sub_location = (row2, colm2)
            user_sub_location2 = (row2, colm2 + 1)
        else:
            print("Please just pick a row and column :")
            decision2 = input("Do you want the Submarine's location to be random? :(y/n) ")
         
        decision3 = input("Do you want your Destoryer's location to be random? :(y/n) ")
        if decision2 == "y":
            row3 = random.randrange(0,board_size)
            colm3 = random.randrange(0,board_size)
            user_destoryer_location = (row3, colm3)
            user_destoryer_location2 = (row3 + 1, colm3)
        elif decision3 == "n":
            row3 = int(input("What row would you like the Destoryer to be placed?: "))
            colm3 = int(input("What column would you like the Destoryer to be placed?: "))
            user_destoryer_location = (row3, colm3)
            user_destoryer_location2 = (row3 + 1, colm3)
        else:
            print("Please just pick a row and column :")
            decision3 = input("Do you want the Destoryer's location to be random? :(y/n) ")
        
        return row2, colm2, user_sub_location, user_sub_location2, row3, colm3, user_destoryer_location, user_destoryer_location2
        
    row2, colm2, user_sub_location, user_sub_location2, row3, colm3, user_destoryer_location, user_destoryer_location2 = ask()
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print("You have choosen," ,user_sub_location, user_sub_location2, "as your Submarine's location and" ,user_destoryer_location, user_destoryer_location2, "as your Destoryer's location")
    def computer_ask():
        row4 = random.randrange(0,board_size)
        colm4 = random.randrange(0,board_size)
        computer_sub_location = (row4, colm4)
        computer_sub_location2 = (row4, colm4 +1)
        return computer_sub_location, computer_sub_location2
    
    computer_sub_location, computer_sub_location2 = computer_ask()
    
    def computer_ask2():
        row4 = random.randrange(0,board_size)
        colm4 = random.randrange(0,board_size)
        computer_destoryer_location = (row4, colm4)
        computer_destoryer_location2 = (row4 +1, colm4)
        return computer_destoryer_location, computer_destoryer_location2
    
    
    computer_destoryer_location, computer_destoryer_location2 = computer_ask2()
    
    print(computer_sub_location)
    print(computer_sub_location2)
    print(computer_destoryer_location)
    print(computer_destoryer_location2)

    ArrayUser = []
    
    for x in range(0,board_size):
        ArrayUser.append([Fore.BLUE + "O"] * board_size)
        
    ArrayComputer = []
    
    for x in range(0,board_size):
        ArrayComputer.append([Fore.BLUE + "O"] * board_size)

    def printboard(ArrayUser):
        for row in ArrayUser:
            print(" ".join(row))
            
    def printboard(ArrayComputer):
        for row in ArrayComputer:
            print(" ".join(row))
            
    ArrayComputer[row2][colm2] = (Fore.WHITE + "S")
    ArrayComputer[row2][colm2 +1] = (Fore.WHITE + "S")
    ArrayComputer[row3][colm3] = (Fore.WHITE + "D")
    ArrayComputer[row3 +1][colm3] = (Fore.WHITE + "D")

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
                print(Fore.WHITE + "Round", round)
                print(Fore.WHITE + "This is the enemy's board. Now try to guess where their ship is.")
                printboard(ArrayUser)
                print(Fore.WHITE + "**************")
                
                while True:
                    try:
                        row = int(input(Fore.WHITE + "Please guess a row : "))
                    except ValueError:
                        print(Fore.WHITE + "Please type only whole numbers that coorelate to the board size")
                        continue
                    if row in (range(0,board_size)):
                        print(Fore.WHITE + "**************")
                    else:
                        if row != (range(0,board_size)):
                            print(Fore.WHITE + "Good try sucker now enter whooe numbers that coorelate to the board size")
                            row = int(input(Fore.WHITE + "Please guess a row : "))
                    break
    
                while True:
                    try:
                        colm = int(input(Fore.WHITE + "Please guess a column : "))
                    except ValueError:
                        print(Fore.WHITE + "Please type only whole numbers that coorelate to the board size")
                        continue
                    if colm in (range(0,board_size)):
                        print(Fore.WHITE + "***************")
                    else:
                        if colm != (range(0,board_size)):
                            print(Fore.WHITE + "Good try sucker now enter only whole numbers that coorelate to the board size")
                            colm = int(input(Fore.WHITE + "Please guess a column : "))
                    break
                list= (row, colm)
                user_guesslist.append(list)
                print(Fore.WHITE + "These are the guesses that have been made so far:", user_guesslist)
        
                if ArrayUser[row][colm] == "O":
                    print(Fore.WHITE + "**********")
                else:
                    print(Fore.WHITE + "You already chose that coordinate!")
        
                if list == computer_sub_location or list == computer_sub_location2 or list == computer_destoryer_location or list == computer_destoryer_location2:
                    print(Fore.WHITE + "Dang you hit one of the computers ships")
                    ArrayUser[row][colm] = (Fore.GREEN + "X")
                    if user_guesslist == computer_sub_location and user_guesslist == computer_sub_location2:
                        print(Fore.WHITE + "You have sunk the computers Submarine")
                        ArrayUser[row][colm] = (Fore.BLACK + "X")
                    if user_guesslist == computer_destoryer_location and user_guesslist == computer_destoryer_location2:
                        print(Fore.WHITE + "You have sunk the computers Destoryer")
                        ArrayUser[row][colm] = (Fore.BLACK + "X")
                    elif user_guesslist == computer_destoryer_location and user_guesslist == computer_destoryer_location2 and user_guesslist == computer_sub_location and user_guesslist == computer_sub_location2:
                        print(Fore.WHITE + "Congraulations, you have beaten the very challenging game of Battle Ship")
                        try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")
                        if try_again == "y":
                            battleship()
                        elif try_again == "n":
                            print(Fore.WHITE + "Ok thank you, goodbye")
                            exit()
                        else:
                            print(Fore.WHITE + "Please type only y or n")
                            try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")
                            
                else:
                    print(Fore.WHITE + "You missed! Try again!")
                    ArrayUser[row][colm] = (Fore.RED + "M")
                    
                round +=1
                
                if round > 6 and list == computer_sub_location or round > 6 and list == computer_sub_location2 or round > 6 and list == computer_destoryer_location or round > 6 and list == computer_destoryer_location2:
                    print(Fore.WHITE + "Wow your pretty lucky, Congratulations you win!")
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
                print(Fore.WHITE + "Computer Round", computer_round)
                print(Fore.WHITE + "This is your board, the computer will now try to guess where your Submarine, shown by the S, and Destoryer, shown by the D.")
                printboard(ArrayComputer)
                computer_row = random.randrange(0,board_size-1)
                computer_colm = random.randrange(0,board_size-1)
        
                computer_list= (computer_row, computer_colm)
                computer_guesslist.append(computer_list)
                print(Fore.WHITE + "These are the guesses the computer made:", computer_guesslist)
                computer_round += 1
        
                if ArrayComputer[computer_row][computer_colm] == "O":
                    print(Fore.WHITE + "**********")
                else:
                    computer_row = random.randrange(0,board_size-1)
                    computer_colm = random.randrange(0,board_size-1)
                if computer_list == user_sub_location or computer_list == user_sub_location2 or computer_list == user_destoryer_location or computer_list == user_destoryer_location2:
                    print(Fore.WHITE + "Dang the computer hit one of your ships")
                    ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_guesslist == user_sub_location and computer_guesslist == user_sub_location2:
                        print(Fore.WHITE + "The computer has sunk your Submarine")
                        ArrayComputer[computer_row][computer_colm] = (Fore.BLACK + "X")
                    if computer_guesslist == user_destoryer_location and computer_guesslist == user_destoryer_location2:
                        print(Fore.WHITE + "The computer has sunk your Destoryer")
                        ArrayComputer[computer_row][computer_colm] = (Fore.BLACK + "X")
                    elif computer_guesslist == user_destoryer_location and computer_guesslist == user_destoryer_location2 and computer_guesslist == user_sub_location and computer_guesslist == user_sub_location2:
                        print(Fore.WHITE + "Congraulations, you have beaten the very challenging game of Battle Ship")
                        try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")
                        if try_again == "y":
                            battleship()
                        elif try_again == "n":
                            print(Fore.WHITE + "Ok thank you, goodbye")
                            exit()
                        else:
                            print(Fore.WHITE + "Please type only y or n")
                            try_again = input(Fore.WHITE + "Would you like to play again? :(y/n): ")
                else:
                    print(Fore.WHITE + "The computer missed, so you survived another round")
                    ArrayComputer[computer_row][computer_colm] = (Fore.RED + "M")
                    
                if round > 6 and computer_list == user_sub_location or round > 6 and computer_list == user_sub_location2 or round > 6 and computer_list == user_destoryer_location or round > 6 and computer_list == user_destoryer_location2:
                    print(Fore.WHITE + "Wow you lost to the computer the last round. Good Game")
                    continue
                break


battleship()
