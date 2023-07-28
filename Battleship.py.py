#BattleShip

def battleship() :
    
    import string
    import colorama
    from colorama import Fore
    #all these varibles must be defined 
    round = 1
    computer_round = 1
    import random
    user_sub_location = None
    user_sub_location2 = None
    user_sub_location3 = None
    user_destoryer_location = None
    user_destoryer_location2 = None
    user_destoryer_location3 = None
    user_patrol_location = None
    user_patrol_location2 = None
    user_battle_location = None
    user_battle_location2 = None
    user_battle_location3 = None
    user_battle_location4 = None
    user_carrier_location = None
    user_carrier_location2 = None
    user_carrier_location3 = None
    user_carrier_location4 = None
    user_carrier_location5 = None
    computer_sub_location = None
    computer_sub_location2 = None
    computer_sub_location3 = None
    computer_destoryer_location = None
    computer_destoryer_location2 = None
    computer_destoryer_location3 = None
    computer_patrol_location = None
    computer_patrol_location2 = None
    computer_battle_location = None
    computer_battle_location2 = None
    computer_battle_location3 = None
    computer_battle_location4 = None
    computer_carrier_location = None
    computer_carrier_location2 = None
    computer_carrier_location3 = None
    computer_carrier_location4 = None
    computer_carrier_location5 = None
    board_size = 10
    try_again = None

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
            row2 = random.choice(string.ascii_uppercase[0:10])
            colm2 = random.randrange(0,board_size - 2)
            user_sub_location = (ord(row2) - 65, colm2)
            user_sub_location2 = (ord(row2) - 65, colm2 + 1)
            user_sub_location3 = (ord(row2) - 65, colm2 + 2)
        elif decision2 == "n":
            row2 = input("What row would you like the Submarine to be placed? (A-J): ")
            colm2 = int(input("What column would you like the Submarine to be placed?: "))
            user_sub_location = (row2, colm2)
            user_sub_location2 = (row2, colm2 + 1)
            user_sub_location3 = (row2, colm2 + 2)
        decision4 = input("Do you want your Patrol Boat's location to be random? :(y/n) ")
        if decision4 == "y":
            row6 = random.choice(string.ascii_uppercase[0:10])
            colm6 = random.randrange(0,board_size - 1)
            user_patrol_location = (ord(row6) - 65, colm6)
            user_patrol_location2 = (ord(row6) - 64, colm6)
        elif decision4 == "n":
            row6 = input("What row would you like the Submarine to be placed? (A-J): ")
            colm6 = int(input("What column would you like the Submarine to be placed?: "))
            user_patrol_location = (row6, colm6)
            user_patrol_location2 = (row6 + 1, colm6)
        else:
            print("Please just pick a row and column :")
            decision4 = input("Do you want the Patrol Boats location to be random? :(y/n) ")
         
        decision3 = input("Do you want your Destroyer's location to be random? :(y/n) ")
        if decision3 == "y":
            row3 = random.choice(string.ascii_uppercase[0:10])
            colm3 = random.randrange(1,board_size - 2)
            user_destoryer_location = (ord(row3) - 65, colm3)
            user_destoryer_location2 = (ord(row3) - 65, colm3 + 1)
            user_destoryer_location3 = (ord(row3) - 65, colm3 + 2)
        elif decision3 == "n":
            row3 = input("What row would you like the Destroyer to be placed? (A-J): ")
            colm3 = int(input("What column would you like the Destroyer to be placed?: "))
            user_destoryer_location = (row3, colm3)
            user_destoryer_location2 = (row3 , colm3 + 1)
            user_destoryer_location3 = (row3, colm3 + 2)
        else:
            print("Please just pick a row and column :")
            decision3 = input("Do you want the Destroyer's location to be random? :(y/n) ")
        
        decision5 = input("Do you want your Battleship's location to be random? :(y/n) ")
        if decision5 == "y":
            row7 = random.choice(string.ascii_uppercase[0:10])
            colm7 = random.randrange(1,board_size - 3)
            user_battle_location = (ord(row7) - 65, colm7)
            user_battle_location2 = (ord(row7) - 64, colm7)
            user_battle_location3 = (ord(row7) - 63, colm7)
            user_battle_location4 = (ord(row7) - 62, colm7)
        elif decision5 == "n":
            row7 = input("What row would you like the Battleship to be placed? (A-J): ")
            colm7 = int(input("What column would you like the Battleship to be placed?: "))
            user_battle_location = (row7, colm7)
            user_battle_location2 = (row7 + 1, colm7)
            user_battle_location3 = (row7 + 2, colm7)
            user_battle_location4 = (row7 + 3, colm7)
        else:
            print("Please just pick a row and column :")
            decision5 = input("Do you want the Battleship's location to be random? :(y/n) ")
            
        decision6 = input("Do you want your Carriers's location to be random? :(y/n) ")
        if decision6 == "y":
            row8 = random.choice(string.ascii_uppercase[0:10])
            colm8 = random.randrange(1,board_size - 4)
            user_carrier_location = (ord(row8) - 65, colm8)
            user_carrier_location2 = (ord(row8) - 65, colm8 + 1)
            user_carrier_location3 = (ord(row8) - 65, colm8 + 2)
            user_carrier_location4 = (ord(row8) - 65, colm8 + 3)
            user_carrier_location5 = (ord(row8) -65, colm8 + 4)
        elif decision5 == "n":
            row8 = input("What row would you like the Carrier to be placed? (A-J): ")
            colm8 = int(input("What column would you like the Carrier to be placed?: "))
            user_carrier_location = (row8, colm8)
            user_carrier_location2 = (row8, colm8 + 1)
            user_carrier_location3 = (row8, colm8 + 2)
            user_carrier_location4 = (row8, colm8 + 3)
            user_carrier_location5 = (row8, colm8 + 4)
        else:
            print("Please just pick a row and column :")
            decision5 = input("Do you want the Carrier's location to be random? :(y/n) ")
        
        return row2, colm2, user_sub_location, user_sub_location2, user_sub_location3, row3, colm3, user_destoryer_location, user_destoryer_location2, user_destoryer_location3, row6, colm6, user_patrol_location, user_patrol_location2, user_battle_location, user_battle_location2, user_battle_location3, user_battle_location4, row7, colm7, user_carrier_location, user_carrier_location2, user_carrier_location3, user_carrier_location4, user_carrier_location5, row8, colm8
        
    row2, colm2, user_sub_location, user_sub_location2, user_sub_location3, row3, colm3, user_destoryer_location, user_destoryer_location2, user_destoryer_location3, row6, colm6, user_patrol_location, user_patrol_location2, user_battle_location, user_battle_location2, user_battle_location3, user_battle_location4, row7, colm7, user_carrier_location, user_carrier_location2, user_carrier_location3, user_carrier_location4, user_carrier_location5, row8, colm8 = ask()
    
    def ship_check_user():
        if user_sub_location == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location2 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            exit()
        if user_sub_location3 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            exit()
    ship_check_user()
    
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print("You have chosen," ,user_sub_location, user_sub_location2, user_sub_location3, "as your Submarine's location and" ,user_destoryer_location, user_destoryer_location2, user_destoryer_location3, "as your Destroyer's location")
    print("You have chosen," ,user_patrol_location, user_patrol_location2, "as your Patrol Boat's location and" ,user_battle_location, user_battle_location2, user_battle_location3, user_battle_location4, "as your Battleship's location")
    print("You have chosen," ,user_carrier_location, user_carrier_location2, user_carrier_location3, user_carrier_location4, user_carrier_location5, "as your Carrier's location")
    
    def computer_ask():
        row4 = random.randrange(1,board_size - 1)
        colm4 = random.randrange(0,board_size)
        computer_sub_location = (row4, colm4)
        computer_sub_location2 = (row4, colm4 +1)
        computer_sub_location3 = (row4, colm4 +2)
        return computer_sub_location, computer_sub_location2, computer_sub_location3, row4, colm4
    
    computer_sub_location, computer_sub_location2, computer_sub_location3, row4, colm4 = computer_ask()
    
    def computer_ask2():
        row5 = random.randrange(0,board_size)
        colm5 = random.randrange(1,board_size - 1)
        computer_destoryer_location = (row5, colm5)
        computer_destoryer_location2 = (row5 +1, colm5)
        computer_destoryer_location3 = (row5 +2, colm5)
        return computer_destoryer_location, computer_destoryer_location2, computer_destoryer_location3, row5, colm5
    
    
    computer_destoryer_location, computer_destoryer_location2, computer_destoryer_location3, row5, colm5 = computer_ask2()
    
    def computer_ask3():
        row9 = random.randrange(0,board_size)
        colm9 = random.randrange(1,board_size - 1)
        computer_patrol_location = (row9, colm9)
        computer_patrol_location2 = (row9 +1, colm9)
        return computer_patrol_location, computer_patrol_location2, row9, colm9
    
    
    computer_patrol_location, computer_patrol_location2, row9, colm9 = computer_ask3()
    
    def computer_ask4():
        row10 = random.randrange(0,board_size)
        colm10 = random.randrange(1,board_size - 1)
        computer_battle_location = (row10, colm10)
        computer_battle_location2 = (row10 +1, colm10)
        computer_battle_location3 = (row10 +2, colm10)
        computer_battle_location4 = (row10 +3, colm10)
        return computer_battle_location, computer_battle_location2, computer_battle_location3, computer_battle_location4, row10, colm10
    
    
    computer_battle_location, computer_battle_location2, computer_battle_location3, computer_battle_location4, row10, colm10 = computer_ask4()
    
    def computer_ask5():
        row11 = random.randrange(0,board_size)
        colm11 = random.randrange(1,board_size - 1)
        computer_carrier_location = (row11, colm11)
        computer_carrier_location2 = (row11 +1, colm11)
        computer_carrier_location3 = (row11 +2, colm11)
        computer_carrier_location4 = (row11 +3, colm11)
        computer_carrier_location5 = (row11 + 4, colm11)
        return computer_carrier_location, computer_carrier_location2, computer_carrier_location3, computer_carrier_location4, computer_carrier_location5, row11, colm11
    
    
    computer_carrier_location, computer_carrier_location2, computer_carrier_location3, computer_carrier_location4, computer_carrier_location5, row11, colm11 = computer_ask5()
    
    def ship_check_computer():
        if computer_sub_location == computer_destoryer_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_patrol_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_battle_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_carrier_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_destoryer_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_patrol_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_battle_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_carrier_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_destoryer_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_battle_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_carrier_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_battle_location4:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_carrier_location4:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location == computer_carrier_location5:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_destoryer_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_patrol_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_battle_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_carrier_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_destoryer_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_patrol_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_battle_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_carrier_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_destoryer_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_battle_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_carrier_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_battle_location4:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_carrier_location4:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location2 == computer_carrier_location5:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_destoryer_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_patrol_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_battle_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_carrier_location:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_destoryer_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_patrol_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_battle_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_carrier_location2:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_destoryer_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_battle_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_carrier_location3:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_battle_location4:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_carrier_location4:
            print("The computers placement is invalid, please run the program again")
            exit()
        if computer_sub_location3 == computer_carrier_location5:
            print("The computers placement is invalid, please run the program again")
            exit()
    ship_check_computer()

    ArrayUser = []
    
    for x in range(0,board_size):
        ArrayUser.append([Fore.BLUE + "O"] * board_size)
        
    ArrayComputer = []
    
    for x in range(0,board_size):
        ArrayComputer.append([Fore.BLUE + "O"] * board_size)
    row_letters = [ Fore.WHITE + "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    def printboard(ArrayUser):
        letter_index = 0
        for i in range(0, board_size + 1):
            print(i, end = " ")
        print("")
        
        for row in ArrayUser:
            print(Fore.WHITE + row_letters[letter_index], " ".join(row))
            letter_index += 1
            
    def printboard(ArrayComputer):
        letter_index = 0
        for i in range(0, board_size + 1):
            print(i, end = " ")
        print("")
        
        for row in ArrayComputer:
            print(Fore.WHITE + row_letters[letter_index], " ".join(row))
            letter_index += 1
            
    ArrayComputer[ord(row2) - 65][colm2] = (Fore.WHITE + "S")
    ArrayComputer[ord(row2) - 65][colm2 + 1] = (Fore.WHITE + "S")
    ArrayComputer[ord(row2) - 65][colm2 + 2] = (Fore.WHITE + "S")
    ArrayComputer[ord(row3) - 65][colm3] = (Fore.WHITE + "D")
    ArrayComputer[ord(row3) - 65][colm3 + 1] = (Fore.WHITE + "D")
    ArrayComputer[ord(row3) - 65][colm3 + 2] = (Fore.WHITE + "D")
    ArrayComputer[ord(row6) - 65][colm6] = (Fore.WHITE + "P")
    ArrayComputer[ord(row6) - 64][colm6] = (Fore.WHITE + "P")
    ArrayComputer[ord(row7) - 65][colm7] = (Fore.WHITE + "B")
    ArrayComputer[ord(row7) - 64][colm7] = (Fore.WHITE + "B")
    ArrayComputer[ord(row7) - 63][colm7] = (Fore.WHITE + "B")
    ArrayComputer[ord(row7) - 62][colm7] = (Fore.WHITE + "B")
    ArrayComputer[ord(row8) - 65][colm8] = (Fore.WHITE + "C")
    ArrayComputer[ord(row8) - 65][colm8 + 1] = (Fore.WHITE + "C")
    ArrayComputer[ord(row8) - 65][colm8 + 2] = (Fore.WHITE + "C")
    ArrayComputer[ord(row8) - 65][colm8 + 3] = (Fore.WHITE + "C")
    ArrayComputer[ord(row8) - 65][colm8 + 4] = (Fore.WHITE + "C")
    
    row = 0
    colm = 0
    user_guesslist = []
    computer_row = 0
    computer_colm = 0
    computer_guesslist = []
    
        
    while True:
        while True:
            while round < 25 and computer_round >= round :
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
                        row = input(Fore.WHITE + "Please guess a row (A-J): ") 
                    except ValueError:
                        print(Fore.WHITE + "Please type only letters that coorelate to the board size")
                        continue
                    if row in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"):
                        print(Fore.WHITE + "**************")
                    else:
                        if row != ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J"):
                            print(Fore.WHITE + "Good try sucker now enter letters that coorelate to the board size")
                            row = input(Fore.WHITE + "Please guess a row (A-J): ")
                    break
    
                while True:
                    try:
                        colm = int(input(Fore.WHITE + "Please guess a column : ")) -1
                    except ValueError:
                        print(Fore.WHITE + "Please type only whole numbers that coorelate to the board size")
                        continue
                    if colm in (range(0,board_size)):
                        print(Fore.WHITE + "***************")
                    else:
                        if colm != (range(0,board_size)):
                            print(Fore.WHITE + "Good try sucker now enter only whole numbers that coorelate to the board size")
                            colm = int(input(Fore.WHITE + "Please guess a column : ")) -1
                    break
                list= (ord(row) -65, colm +1)
                guess = (chr(ord(row)), colm + 1 )
                user_guesslist.append(guess)
                print(Fore.WHITE + "These are the guesses that have been made so far:", user_guesslist)
        
                if ArrayUser[ord(row) -65][colm] == (Fore.BLUE + "O"):
                    print(Fore.WHITE + "**********")
                else:
                    print()
        
                if list == computer_sub_location or list == computer_sub_location2 or list == computer_sub_location3 or list == computer_destoryer_location or list == computer_destoryer_location2 or list == computer_destoryer_location3 or list == computer_patrol_location or list == computer_patrol_location2 or list == computer_battle_location or list == computer_battle_location2 or list == computer_battle_location3 or list == computer_battle_location4 or list == computer_carrier_location or list == computer_carrier_location2 or list == computer_carrier_location3 or list == computer_carrier_location4 or list == computer_carrier_location5:
                    print(Fore.WHITE + "**********")
                    
                    if list == computer_sub_location or list == computer_sub_location2 or list == computer_sub_location3:
                        print(Fore.WHITE + "You have hit the computers Submarine")
                        ArrayUser[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_destoryer_location or list == computer_destoryer_location2 or list == computer_destoryer_location3:
                        print(Fore.WHITE + "You have hit the computers Destroyer")
                        ArrayUser[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_patrol_location or list == computer_patrol_location2:
                        print(Fore.WHITE + "You have hit the computers Patrol Boat")
                        ArrayUser[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_battle_location or list == computer_battle_location2 or list == computer_battle_location3 or list == computer_battle_location4:
                        print(Fore.WHITE + "You have hit the computers Battleship")
                        ArrayUser[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_carrier_location or list == computer_carrier_location2 or list == computer_carrier_location3 or list == computer_carrier_location4 or list == computer_carrier_location5:
                        print(Fore.WHITE + "You have hit the computers Carrier")
                        ArrayUser[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    
                    if ArrayUser[row4][colm4] == (Fore.GREEN + "X") and ArrayUser[row4][colm4 + 1] == (Fore.GREEN + "X") and ArrayUser[row4][colm4 + 2] == (Fore.GREEN + "X"):
                        print("You have sunk the computers submarine!")
                        ArrayUser[row4][colm4] = (Fore.BLACK + "X")
                        ArrayUser[row4][colm4 + 1] = (Fore.BLACK + "X")
                    if ArrayUser[row5][colm5] == (Fore.GREEN + "X") and ArrayUser[row5+ 1][colm5] == (Fore.GREEN + "X"):
                        print("You have sunk the computers destroyer!")
                        ArrayUser[row5][colm5] = (Fore.BLACK + "X")
                        ArrayUser[row5 + 1][colm5] = (Fore.BLACK + "X")
                    if ArrayUser[row9][colm9] == (Fore.GREEN + "X") and ArrayUser[row9+ 1][colm9] == (Fore.GREEN + "X"):
                        print("You have sunk the computers Patrol Boat!")
                        ArrayUser[row9][colm9] = (Fore.BLACK + "X")
                        ArrayUser[row9 + 1][colm9] = (Fore.BLACK + "X")
                    if ArrayUser[row10][colm10] == (Fore.GREEN + "X") and ArrayUser[row10 + 1][colm10] == (Fore.GREEN + "X") and ArrayUser[row10 + 2][colm10] == (Fore.GREEN + "X") and ArrayUser[row10 + 3][colm10] == (Fore.GREEN + "X"):
                        print("You have sunk the computers Battleship!")
                        ArrayUser[row10][colm10] = (Fore.BLACK + "X")
                        ArrayUser[row10 + 1][colm10] = (Fore.BLACK + "X")
                        ArrayUser[row10 + 2][colm10] = (Fore.BLACK + "X")
                        ArrayUser[row10 + 3][colm10] = (Fore.BLACK + "X")
                    if ArrayUser[row11][colm11] == (Fore.GREEN + "X") and ArrayUser[row11 + 1][colm11] == (Fore.GREEN + "X") and ArrayUser[row11 + 2][colm11] == (Fore.GREEN + "X") and ArrayUser[row11 + 3][colm11] == (Fore.GREEN + "X") and ArrayUser[row11 + 4][colm11] == (Fore.GREEN + "X"):
                        print("You have sunk the computers Carrier!")
                        ArrayUser[row11][colm11] = (Fore.BLACK + "X")
                        ArrayUser[row11 + 1][colm11] = (Fore.BLACK + "X")
                        ArrayUser[row11 + 2][colm11] = (Fore.BLACK + "X")
                        ArrayUser[row11 + 3][colm11] = (Fore.BLACK + "X")
                        ArrayUser[row11 + 4][colm11] = (Fore.BLACK + "X")
                    
                    if ArrayUser[row5][colm5] == (Fore.BLACK + "X") and ArrayUser[row5+ 1][colm5] == (Fore.BLACK + "X") and ArrayUser[row5+ 2][colm5] == (Fore.BLACK + "X") and ArrayUser[row4][colm4] == (Fore.BLACK + "X") and ArrayUser[row4][colm4 +1] == (Fore.BLACK + "X") and ArrayUser[row4][colm4 + 2] == (Fore.GREEN + "X") and ArrayUser[row9][colm9] == (Fore.BLACK + "X") and ArrayUser[row9 + 1][colm9] == (Fore.BLACK + "X") and ArrayUser[row10][colm10] == (Fore.BLACK + "X") and ArrayUser[row10 + 1][colm10] == (Fore.BLACK + "X") and ArrayUser[row10 + 2][colm10] == (Fore.BLACK + "X") and ArrayUser[row10 + 3][colm10] == (Fore.BLACK + "X") and ArrayUser[row11][colm11] == (Fore.BLACK + "X") and ArrayUser[row11 + 1][colm11] == (Fore.BLACK + "X") and ArrayUser[row11 + 2][colm11] == (Fore.BLACK + "X") and ArrayUser[row11 + 3][colm11] == (Fore.BLACK + "X") and ArrayUser[row11 + 4][colm11] == (Fore.BLACK + "X"):
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
                    ArrayUser[ord(row) -65][colm] = (Fore.RED + "M")
                    
                if round == 25:
                    print("You lost the game of battleship!")
                    
                round +=1
                
            while round < 25 and computer_round <= round :
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "**************")
                print(Fore.WHITE + "Computer Round", computer_round)
                print(Fore.WHITE + "This is your board, the computer will now try to guess where your Submarine, shown by the S, Destroyer, shown by the D, Patrol Boat, shown by the P, Battleship, shown by the B, and Carrier, shown by the C.")
                printboard(ArrayComputer)
                computer_row = random.randrange(0,9)
                computer_colm = random.randrange(0,9)
        
                computer_list= (chr(computer_row +65), computer_colm +1)
                computer_guesslist.append(computer_list)
                print(Fore.WHITE + "These are the guesses the computer made:", computer_guesslist)
                computer_round += 1
        
                if ArrayComputer[computer_row][computer_colm] == (Fore.BLUE + "O"):
                    print(Fore.WHITE + "**********")
                else: 
                    computer_row = random.randrange(0,9)
                    computer_colm = random.randrange(0,9)
                if computer_list == user_sub_location or computer_list == user_sub_location2 or computer_list == user_sub_location3 or computer_list == user_destoryer_location or computer_list == user_destoryer_location2 or computer_list == user_destoryer_location3 or computer_list == user_patrol_location or computer_list == user_patrol_location2 or computer_list == user_battle_location or computer_list == user_battle_location2 or computer_list == user_battle_location3 or computer_list == user_battle_location4 or computer_list == user_carrier_location or computer_list == user_carrier_location2 or computer_list == user_carrier_location3 or computer_list == user_carrier_location4 or computer_list == user_carrier_location5:
                    print(Fore.WHITE + "**********")
                    if computer_list == user_sub_location or computer_list == user_sub_location2 or computer_list == user_sub_location3:
                        print(Fore.WHITE + "Your submarine has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_destoryer_location or computer_list == user_destoryer_location2 or computer_list == user_destoryer_location3:
                        print(Fore.WHITE + "Your Destroyer has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_patrol_location or computer_list == user_patrol_location2:
                        print(Fore.WHITE + "Your Patrol Boat has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_battle_location or computer_list == user_battle_location2 or computer_list == user_battle_location3 or computer_list == user_battle_location4:
                        print(Fore.WHITE + "Your Battleship has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_carrier_location or computer_list == user_carrier_location2 or computer_list == user_carrier_location3 or computer_list == user_carrier_location4 or computer_list == user_carrier_location5:
                        print(Fore.WHITE + "Your Carrier has been hit!")
                        ArrayComputer[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if ArrayComputer[row2][colm2] == (Fore.GREEN + "X") and ArrayComputer[row2][colm2 + 1] == (Fore.GREEN + "X") and ArrayComputer[row2][colm2 + 2] == (Fore.GREEN + "X"):
                        print("Your submarine has been sunk!")
                        ArrayUser[row2][colm2] = (Fore.BLACK + "X")
                        ArrayUser[row2][colm2 + 1] = (Fore.BLACK + "X")
                        ArrayUser[row2][colm2 + 2] = (Fore.BLACK + "X")
                    if ArrayUser[row3][colm3] == (Fore.GREEN + "X") and ArrayUser[row3][colm3 + 1] == (Fore.GREEN + "X") and ArrayUser[row3][colm3 + 2] == (Fore.GREEN + "X"):
                        print("Your Destroyer has been sunk!")
                        ArrayUser[row3][colm3] = (Fore.BLACK + "X")
                        ArrayUser[row3][colm3 + 1] = (Fore.BLACK + "X")
                        ArrayUser[row3][colm3 + 2] = (Fore.BLACK + "X")
                    if ArrayUser[row6][colm6] == (Fore.GREEN + "X") and ArrayUser[row6 + 1][colm6] == (Fore.GREEN + "X"):
                        print("Your Patrol Boat has been sunk!")
                        ArrayUser[row6][colm6] = (Fore.BLACK + "X")
                        ArrayUser[row6 + 1][colm6] = (Fore.BLACK + "X")
                    if ArrayUser[row7][colm7] == (Fore.GREEN + "X") and ArrayUser[row7 + 1][colm7] == (Fore.GREEN + "X") and ArrayUser[row7 + 2][colm7] == (Fore.GREEN + "X") and ArrayUser[row7 + 3][colm7] == (Fore.GREEN + "X"):
                        print("Your Battleship has been sunk!")
                        ArrayUser[row7][colm7] = (Fore.BLACK + "X")
                        ArrayUser[row7 + 1][colm7] = (Fore.BLACK + "X")
                        ArrayUser[row7 + 2][colm7] = (Fore.BLACK + "X")
                        ArrayUser[row7 + 3][colm7] = (Fore.BLACK + "X")
                    if ArrayUser[row8][colm8] == (Fore.GREEN + "X") and ArrayUser[row8][colm8 + 1] == (Fore.GREEN + "X") and ArrayUser[row8][colm8 + 2] == (Fore.GREEN + "X") and ArrayUser[row8][colm8 + 3] == (Fore.GREEN + "X") and ArrayUser[row8][colm8 + 4] == (Fore.GREEN + "X"):
                        print("Your Carrier has been sunk!")
                        ArrayUser[row8][colm8] = (Fore.BLACK + "X")
                        ArrayUser[row8][colm8 + 1] = (Fore.BLACK + "X")
                        ArrayUser[row8][colm8 + 2] = (Fore.BLACK + "X")
                        ArrayUser[row8][colm8 + 3] = (Fore.BLACK + "X")
                        ArrayUser[row8][colm8 + 4] == (Fore.BLACK + "X")
                    if ArrayUser[row3][colm3] == (Fore.BLACK + "X") and ArrayUser[row3][colm3 + 1] == (Fore.BLACK + "X") and ArrayUser[row3][colm3 + 2] == (Fore.BLACK + "X") and ArrayUser[row2][colm2] == (Fore.BLACK + "X") and ArrayUser[row2][colm2 + 1] == (Fore.BLACK + "X") and ArrayUser[row2][colm2 + 2] == (Fore.BLACK + "X") and ArrayUser[row6][colm6] == (Fore.BLACK + "X") and ArrayUser[row6 + 1][colm6] == (Fore.BLACK + "X") and ArrayUser[row7][colm7] == (Fore.BLACK + "X") and ArrayUser[row7 + 1][colm7] == (Fore.BLACK + "X") and ArrayUser[row7 + 2][colm7] == (Fore.BLACK + "X") and ArrayUser[row7 + 3][colm7] == (Fore.BLACK + "X") and ArrayUser[row8][colm8] == (Fore.BLACK + "X") and ArrayUser[row8][colm8 + 1] == (Fore.BLACK + "X") and ArrayUser[row8][colm8 + 2] == (Fore.BLACK + "X") and ArrayUser[row8][colm8 + 3] == (Fore.BLACK + "X") and ArrayUser[row8][colm8 + 4] == (Fore.BLACK + "X"):
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
                    ArrayComputer[computer_row] [computer_colm] = (Fore.RED + "M")
                    
                if round > 25 and computer_list == user_sub_location or round > 25 and computer_list == user_sub_location2 or round > 25 and computer_list == user_sub_location3 or round > 25 and computer_list == user_destoryer_location or round > 25 and computer_list == user_destoryer_location2 or round > 25 and computer_list == user_destoryer_location3 or round > 25 and computer_list == user_patrol_location or round > 25 and computer_list == user_patrol_location2 or round > 25 and computer_list == user_battle_location or round > 25 and computer_list == user_battle_location2 or round > 25 and computer_list == user_battle_location3 or round > 25 and computer_list == user_battle_location4 or round > 25 and computer_list == user_carrier_location or round > 25 and computer_list == user_carrier_location2 or round > 25 and computer_list == user_carrier_location3 or round > 25 and computer_list == user_carrier_location4 or round > 25 and computer_list == user_carrier_location5:
                    print(Fore.WHITE + "Wow you lost to the computer the last round. Good Game")
                    continue
                    
                break


battleship()
