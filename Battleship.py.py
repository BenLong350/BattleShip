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
            
            
        if board_size < 9:
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
            row2 = random.randrange(1,board_size -1)
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
         
        decision3 = input("Do you want your Destroyer's location to be random? :(y/n) ")
        if decision2 == "y":
            row3 = random.randrange(0,board_size)
            colm3 = random.randrange(1,board_size - 1)
            user_destoryer_location = (row3, colm3)
            user_destoryer_location2 = (row3 + 1, colm3)
        elif decision3 == "n":
            row3 = int(input("What row would you like the Destroyer to be placed?: "))
            colm3 = int(input("What column would you like the Destroyer to be placed?: "))
            user_destoryer_location = (row3, colm3)
            user_destoryer_location2 = (row3 + 1, colm3)
        else:
            print("Please just pick a row and column :")
            decision3 = input("Do you want the Destroyer's location to be random? :(y/n) ")
        
        return row2, colm2, user_sub_location, user_sub_location2, row3, colm3, user_destoryer_location, user_destoryer_location2
        
    row2, colm2, user_sub_location, user_sub_location2, row3, colm3, user_destoryer_location, user_destoryer_location2 = ask()
    
    def ship_check1():
        if user_sub_location == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
            
    ship_check1()
    
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print("You have choosen," ,user_sub_location, user_sub_location2, "as your Submarine's location and" ,user_destoryer_location, user_destoryer_location2, "as your Destroyer's location")
    
    def computer_ask():
        row4 = random.randrange(1,board_size - 1)
        colm4 = random.randrange(0,board_size)
        computer_sub_location = (row4, colm4)
        computer_sub_location2 = (row4, colm4 +1)
        return computer_sub_location, computer_sub_location2, row4, colm4
    
    computer_sub_location, computer_sub_location2, row4, colm4 = computer_ask()
    
    def computer_ask2():
        row5 = random.randrange(0,board_size)
        colm5 = random.randrange(1,board_size - 1)
        computer_destoryer_location = (row5, colm5)
        computer_destoryer_location2 = (row5 +1, colm5)
        return computer_destoryer_location, computer_destoryer_location2, row5, colm5
    
    
    computer_destoryer_location, computer_destoryer_location2, row5, colm5 = computer_ask2()
    
    def ship_check2():
        if computer_sub_location == computer_destoryer_location:
            print("The computers ship locations were invalid, please re-start the function")
        
    ship_check2()

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
            while round < 9 and computer_round >= round :
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
                            print(Fore.WHITE + "Good try sucker now enter whole numbers that coorelate to the board size")
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
                    print()
        
                if list == computer_sub_location or list == computer_sub_location2 or list == computer_destoryer_location or list == computer_destoryer_location2:
                    print(Fore.WHITE + "**********")
                    if list == computer_sub_location or list == computer_sub_location2:
                        print(Fore.WHITE + "You have hit the computers Submarine")
                        ArrayUser[row][colm] = (Fore.GREEN + "X")
                    if list == computer_destoryer_location or list == computer_destoryer_location2:
                        print(Fore.WHITE + "You have hit the computers Destroyer")
                        ArrayUser[row][colm] = (Fore.GREEN + "X")
                    if ArrayUser[row4][colm4] == (Fore.GREEN + "X") and ArrayUser[row4][colm4 + 1] == (Fore.GREEN + "X"):
                        print("You have sunk the computers submarine!")
                        ArrayUser[row4][colm4] = (Fore.BLACK + "X")
                        ArrayUser[row4][colm4 + 1] = (Fore.BLACK + "X")
                    if ArrayUser[row5][colm5] == (Fore.GREEN + "X") and ArrayUser[row5+ 1][colm5] == (Fore.GREEN + "X"):
                        print("You have sunk the computers destroyer!")
                        ArrayUser[row5][colm5] = (Fore.BLACK + "X")
                        ArrayUser[row5 + 1][colm5] = (Fore.BLACK + "X")
                    
                    if ArrayUser[row5][colm5] == (Fore.BLACK + "X") and ArrayUser[row5+ 1][colm5] == (Fore.BLACK + "X") and ArrayUser[row4][colm4] == (Fore.BLACK + "X") and ArrayUser[row4][colm4 +1] == (Fore.BLACK + "X"):
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
                    print(Fore.WHITE + "You missed!")
                    ArrayUser[row][colm] = (Fore.RED + "M")
                    
                if round == 8:
                    print("You lost the game of battleship!")
                    
                round +=1
                
            while round < 9 and computer_round <= round :
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "Computer Round", computer_round)
                print(Fore.WHITE + "This is your board, the computer will now try to guess where your Submarine, shown by the S, and Destroyer, shown by the D.")
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
                    print(Fore.WHITE + "**********")
                    if computer_list == user_sub_location or computer_list == user_sub_location2:
                        print(Fore.WHITE + "Your submarine has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_destoryer_location or computer_list == user_destoryer_location2:
                        print(Fore.WHITE + "Your Destroyer has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if ArrayComputer[row2][colm2] == (Fore.GREEN + "X") and ArrayComputer[row3][colm3 + 1] == (Fore.GREEN + "X"):
                        print("Your submarine has been hit!")
                        ArrayUser[row2][colm2] = (Fore.BLACK + "X")
                        ArrayUser[row2][colm2 + 1] = (Fore.BLACK + "X")
                    if ArrayUser[row3][colm3] == (Fore.GREEN + "X") and ArrayUser[row3+ 1][colm3] == (Fore.GREEN + "X"):
                        print("Your Destroyer has been hit!")
                        ArrayUser[row3][colm3] = (Fore.BLACK + "X")
                        ArrayUser[row3 + 1][colm3] = (Fore.BLACK + "X")
                    if ArrayUser[row3][colm3] == (Fore.BLACK + "X") and ArrayUser[row3+ 1][colm3] == (Fore.BLACK + "X") and ArrayUser[row2][colm2] == (Fore.BLACK + "X") and ArrayUser[row2][colm2 +1] == (Fore.BLACK + "X"):
                        print(Fore.WHITE + "You have been beaten by the computer!")
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
                    
                if round > 9 and computer_list == user_sub_location or round > 9 and computer_list == user_sub_location2 or round > 9 and computer_list == user_destoryer_location or round > 6 and computer_list == user_destoryer_location2:
                    print(Fore.WHITE + "Wow you lost to the computer the last round. Good Game")
                    continue
                    
                break


battleship()
