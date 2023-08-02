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
        
        decision2_2 = input("Do you want your Submarine's location to be vertical or horizontal? :(h/v) ")
        if decision2_2 == "h":
            decision2 = input("Do you want your Submarine's location to be random? :(y/n) ")
            if decision2 == "y":
                row2 = random.choice(string.ascii_uppercase[0:10])
                colm2 = random.randrange(0,board_size - 3)
                user_sub_location = (ord(row2) - 65, colm2)
                user_sub_location2 = (ord(row2) - 65, colm2 + 1)
                user_sub_location3 = (ord(row2) - 65, colm2 + 2)
            elif decision2 == "n":
                row2 = input("What row would you like the Submarine to be placed? (A-J): ")
                colm2 = int(input("What column would you like the Submarine to be placed?: "))
                user_sub_location = (row2, colm2)
                user_sub_location2 = (row2, colm2 + 1)
                user_sub_location3 = (row2, colm2 + 2)
        elif decision2_2 == "v":
            decision2 = input("Do you want your Submarine's location to be random? :(y/n) ")
            if decision2 == "y":
                row2 = random.choice(string.ascii_uppercase[0:7])
                colm2 = random.randrange(0,board_size)
                user_sub_location = (ord(row2) - 65, colm2)
                user_sub_location2 = (ord(row2) - 64, colm2)
                user_sub_location3 = (ord(row2) - 63, colm2)
            elif decision2 == "n":
                row2 = input("What row would you like the Submarine to be placed? (A-J): ")
                colm2 = int(input("What column would you like the Submarine to be placed?: "))
                user_sub_location = (row2, colm2)
                user_sub_location2 = (row2 + 1, colm2)
                user_sub_location3 = (row2 + 2, colm2)
        
        decision4_4 = input("Do you want your Patrol Boat to be Horizontal or Vertical? (h/v) ")        
        if decision4_4 == "h":
            decision4 = input("Do you want your Patrol Boat's location to be random? :(y/n) ")
            if decision4 == "y":
                row6 = random.choice(string.ascii_uppercase[0:10])
                colm6 = random.randrange(0,board_size - 2)
                user_patrol_location = (ord(row6) - 65, colm6)
                user_patrol_location2 = (ord(row6) - 65, colm6 + 1)
            elif decision4 == "n":
                row6 = input("What row would you like the Submarine to be placed? (A-J): ")
                colm6 = int(input("What column would you like the Submarine to be placed?: "))
                user_patrol_location = (row6, colm6)
                user_patrol_location2 = (row6, colm6 + 1)
            else:
                print("Please just pick a row and column :")
                decision4 = input("Do you want the Patrol Boats location to be random? :(y/n) ")
        elif decision4_4 == "v":
            decision4 = input("Do you want your Patrol Boat's location to be random? :(y/n) ")
            if decision4 == "y":
                row6 = random.choice(string.ascii_uppercase[0:8])
                colm6 = random.randrange(0,board_size)
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
        
        decision3_3 = input("Do you want your Destroyer to be Horizontal or Vertical? (h/v) ") 
        if decision3_3 == "h":
            decision3 = input("Do you want your Destroyer's location to be random? :(y/n) ")
            if decision3 == "y":
                row3 = random.choice(string.ascii_uppercase[0:10])
                colm3 = random.randrange(1,board_size - 3)
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
        elif decision3_3 == "v":
            decision3 = input("Do you want your Destroyer's location to be random? :(y/n) ")
            if decision3 == "y":
                row3 = random.choice(string.ascii_uppercase[0:7])
                colm3 = random.randrange(1,board_size)
                user_destoryer_location = (ord(row3) - 65, colm3)
                user_destoryer_location2 = (ord(row3) - 64, colm3)
                user_destoryer_location3 = (ord(row3) - 63, colm3)
            elif decision3 == "n":
                row3 = input("What row would you like the Destroyer to be placed? (A-J): ")
                colm3 = int(input("What column would you like the Destroyer to be placed?: "))
                user_destoryer_location = (row3, colm3)
                user_destoryer_location2 = (row3 + 1, colm3)
                user_destoryer_location3 = (row3 + 2, colm3)
            else:
                print("Please just pick a row and column :")
                decision3 = input("Do you want the Destroyer's location to be random? :(y/n) ")
        
        decision5_5 = input("Do you want your Battleship to be Horizontal or Vertical (h/v) ")
        if decision5_5 == "h":
            decision5 = input("Do you want your Battleship's location to be random? :(y/n) ")
            if decision5 == "y":
                row7 = random.choice(string.ascii_uppercase[0:10])
                colm7 = random.randrange(1,board_size - 4)
                user_battle_location = (ord(row7) - 65, colm7)
                user_battle_location2 = (ord(row7) - 65, colm7 + 1)
                user_battle_location3 = (ord(row7) - 65, colm7 + 2)
                user_battle_location4 = (ord(row7) - 65, colm7 + 3)
            elif decision5 == "n":
                row7 = input("What row would you like the Battleship to be placed? (A-J): ")
                colm7 = int(input("What column would you like the Battleship to be placed?: "))
                user_battle_location = (row7, colm7)
                user_battle_location2 = (row7, colm7 + 1)
                user_battle_location3 = (row7, colm7 + 2)
                user_battle_location4 = (row7, colm7 + 3)
            else:
                print("Please just pick a row and column :")
                decision5 = input("Do you want the Battleship's location to be random? :(y/n) ")
        elif decision5_5 == "v":
            decision5 = input("Do you want your Battleship's location to be random? :(y/n) ")
            if decision5 == "y":
                row7 = random.choice(string.ascii_uppercase[0:6])
                colm7 = random.randrange(1,board_size)
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
        
        decision6_6 = input("Do you want your Carrier to be Horizontal or Vertical? (h/v) ")    
        if decision6_6 == "h":
            decision6 = input("Do you want your Carriers's location to be random? :(y/n) ")
            if decision6 == "y":
                row8 = random.choice(string.ascii_uppercase[0:10])
                colm8 = random.randrange(1,board_size - 5)
                user_carrier_location = (ord(row8) - 65, colm8)
                user_carrier_location2 = (ord(row8) - 65, colm8 + 1)
                user_carrier_location3 = (ord(row8) - 65, colm8 + 2)
                user_carrier_location4 = (ord(row8) - 65, colm8 + 3)
                user_carrier_location5 = (ord(row8) -65, colm8 + 4)
            elif decision6 == "n":
                row8 = input("What row would you like the Carrier to be placed? (A-J): ")
                colm8 = int(input("What column would you like the Carrier to be placed?: "))
                user_carrier_location = (row8, colm8)
                user_carrier_location2 = (row8, colm8 + 1)
                user_carrier_location3 = (row8, colm8 + 2)
                user_carrier_location4 = (row8, colm8 + 3)
                user_carrier_location5 = (row8, colm8 + 4)
            else:
                print("Please just pick a row and column :")
                decision6 = input("Do you want the Carrier's location to be random? :(y/n) ")
        elif decision6_6 == "v":
            decision6 = input("Do you want your Carriers's location to be random? :(y/n) ")
            if decision6 == "y":
                row8 = random.choice(string.ascii_uppercase[0:5])
                colm8 = random.randrange(1,board_size)
                user_carrier_location = (ord(row8) - 65, colm8)
                user_carrier_location2 = (ord(row8) - 64, colm8)
                user_carrier_location3 = (ord(row8) - 63, colm8)
                user_carrier_location4 = (ord(row8) - 62, colm8)
                user_carrier_location5 = (ord(row8) -61, colm8)
            elif decision6 == "n":
                row8 = input("What row would you like the Carrier to be placed? (A-J): ")
                colm8 = int(input("What column would you like the Carrier to be placed?: "))
                user_carrier_location = (row8, colm8)
                user_carrier_location2 = (row8 + 1, colm8)
                user_carrier_location3 = (row8 + 2, colm8)
                user_carrier_location4 = (row8 + 3, colm8)
                user_carrier_location5 = (row8 + 4, colm8)
            else:
                print("Please just pick a row and column :")
                decision6 = input("Do you want the Carrier's location to be random? :(y/n) ")
        return row2, colm2, user_sub_location, user_sub_location2, user_sub_location3, row3, colm3, user_destoryer_location, user_destoryer_location2, user_destoryer_location3, row6, colm6, user_patrol_location, user_patrol_location2, user_battle_location, user_battle_location2, user_battle_location3, user_battle_location4, row7, colm7, user_carrier_location, user_carrier_location2, user_carrier_location3, user_carrier_location4, user_carrier_location5, row8, colm8, decision2_2, decision3_3, decision4_4, decision5_5, decision6_6
        
    row2, colm2, user_sub_location, user_sub_location2, user_sub_location3, row3, colm3, user_destoryer_location, user_destoryer_location2, user_destoryer_location3, row6, colm6, user_patrol_location, user_patrol_location2, user_battle_location, user_battle_location2, user_battle_location3, user_battle_location4, row7, colm7, user_carrier_location, user_carrier_location2, user_carrier_location3, user_carrier_location4, user_carrier_location5, row8, colm8, decision2_2, decision3_3, decision4_4, decision5_5, decision6_6 = ask()
    
    def ship_check_user():
        if user_sub_location == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location2 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_sub_location3 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
    ship_check_user()
    
    def ship_check_user2():
        if user_destoryer_location == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location2 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_destoryer_location3 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
    ship_check_user2()
    
    def ship_check_user3():
        if user_battle_location == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location2 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location3 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_patrol_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_patrol_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_battle_location4 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
    ship_check_user3()
    
    def ship_check_user4():
        if user_patrol_location == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_destoryer_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_sub_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_battle_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_carrier_location:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_destoryer_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_sub_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_battle_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_carrier_location2:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_destoryer_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_sub_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_battle_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_carrier_location3:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_battle_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_carrier_location4:
            print("Your ship placement is invalid, please run the program again")
            ask()
        if user_patrol_location2 == user_carrier_location5:
            print("Your ship placement is invalid, please run the program again")
            ask()
    ship_check_user4()
    
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print(Fore.WHITE + "**************")
    print("You have chosen," ,user_sub_location, user_sub_location2, user_sub_location3, "as your Submarine's location and" ,user_destoryer_location, user_destoryer_location2, user_destoryer_location3, "as your Destroyer's location")
    print("You have chosen," ,user_patrol_location, user_patrol_location2, "as your Patrol Boat's location and" ,user_battle_location, user_battle_location2, user_battle_location3, user_battle_location4, "as your Battleship's location")
    print("You have chosen," ,user_carrier_location, user_carrier_location2, user_carrier_location3, user_carrier_location4, user_carrier_location5, "as your Carrier's location")
    
    def computer_ask():
        row4 = random.randrange(1,board_size - 3)
        colm4 = random.randrange(0,board_size -1)
        computer_sub_location = (row4, colm4)
        computer_sub_location2 = (row4, colm4 +1)
        computer_sub_location3 = (row4, colm4 +2)
        return computer_sub_location, computer_sub_location2, computer_sub_location3, row4, colm4
    
    computer_sub_location, computer_sub_location2, computer_sub_location3, row4, colm4 = computer_ask()
    
    def computer_ask2():
        row5 = random.randrange(0,board_size - 3)
        colm5 = random.randrange(1,board_size - 1)
        computer_destoryer_location = (row5, colm5)
        computer_destoryer_location2 = (row5 +1, colm5)
        computer_destoryer_location3 = (row5 +2, colm5)
        return computer_destoryer_location, computer_destoryer_location2, computer_destoryer_location3, row5, colm5
    
    
    computer_destoryer_location, computer_destoryer_location2, computer_destoryer_location3, row5, colm5 = computer_ask2()
    
    def computer_ask3():
        row9 = random.randrange(0,board_size - 2)
        colm9 = random.randrange(1,board_size - 1)
        computer_patrol_location = (row9, colm9)
        computer_patrol_location2 = (row9 +1, colm9)
        return computer_patrol_location, computer_patrol_location2, row9, colm9
    
    
    computer_patrol_location, computer_patrol_location2, row9, colm9 = computer_ask3()
    
    def computer_ask4():
        row10 = random.randrange(0,board_size - 4)
        colm10 = random.randrange(1,board_size - 1)
        computer_battle_location = (row10, colm10)
        computer_battle_location2 = (row10 +1, colm10)
        computer_battle_location3 = (row10 +2, colm10)
        computer_battle_location4 = (row10 +3, colm10)
        return computer_battle_location, computer_battle_location2, computer_battle_location3, computer_battle_location4, row10, colm10
    
    
    computer_battle_location, computer_battle_location2, computer_battle_location3, computer_battle_location4, row10, colm10 = computer_ask4()
    
    def computer_ask5():
        row11 = random.randrange(0,board_size - 5)
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
            ask()
        if computer_sub_location == computer_patrol_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_battle_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_carrier_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_destoryer_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_patrol_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_battle_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_carrier_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_destoryer_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_battle_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_carrier_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_battle_location4:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_carrier_location4:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location == computer_carrier_location5:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_destoryer_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_patrol_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_battle_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_carrier_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_destoryer_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_patrol_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_battle_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_carrier_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_destoryer_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_battle_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_carrier_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_battle_location4:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_carrier_location4:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location2 == computer_carrier_location5:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_destoryer_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_patrol_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_battle_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_carrier_location:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_destoryer_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_patrol_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_battle_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_carrier_location2:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_destoryer_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_battle_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_carrier_location3:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_battle_location4:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_carrier_location4:
            print("The computers placement is invalid, please run the program again")
            ask()
        if computer_sub_location3 == computer_carrier_location5:
            print("The computers placement is invalid, please run the program again")
            ask()
    ship_check_computer()

    ArrayComputer = []
    
    for x in range(0,board_size):
        ArrayComputer.append([Fore.BLUE + "O"] * board_size)
        
    ArrayUser = []
    
    for x in range(0,board_size):
        ArrayUser.append([Fore.BLUE + "O"] * board_size)
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
        
        if decision2_2 == "h":
            ArrayUser[ord(row2) - 65][colm2] = (Fore.WHITE + "S")
            ArrayUser[ord(row2) - 65][colm2 + 1] = (Fore.WHITE + "S")
            ArrayUser[ord(row2) - 65][colm2 + 2] = (Fore.WHITE + "S")
        elif decision2_2 == "v":
            ArrayUser[ord(row2) - 65][colm2] = (Fore.WHITE + "S")
            ArrayUser[ord(row2) - 64][colm2] = (Fore.WHITE + "S")
            ArrayUser[ord(row2) - 63][colm2] = (Fore.WHITE + "S")
            
        if decision3_3 == "h":
            ArrayUser[ord(row3) - 65][colm3] = (Fore.WHITE + "D")
            ArrayUser[ord(row3) - 65][colm3 + 1] = (Fore.WHITE + "D")
            ArrayUser[ord(row3) - 65][colm3 + 2] = (Fore.WHITE + "D")
        elif decision3_3 == "v":
            ArrayUser[ord(row3) - 65][colm3] = (Fore.WHITE + "D")
            ArrayUser[ord(row3) - 64][colm3] = (Fore.WHITE + "D")
            ArrayUser[ord(row3) - 63][colm3] = (Fore.WHITE + "D")
            
        if decision4_4 == "v":
            ArrayUser[ord(row6) - 65][colm6] = (Fore.WHITE + "P")
            ArrayUser[ord(row6) - 64][colm6] = (Fore.WHITE + "P")
        elif decision4_4 == "h":
            ArrayUser[ord(row6) - 65][colm6] = (Fore.WHITE + "P")
            ArrayUser[ord(row6) - 65][colm6 + 1] = (Fore.WHITE + "P")
            
        if decision5_5 == "v":
            ArrayUser[ord(row7) - 65][colm7] = (Fore.WHITE + "B")
            ArrayUser[ord(row7) - 64][colm7] = (Fore.WHITE + "B")
            ArrayUser[ord(row7) - 63][colm7] = (Fore.WHITE + "B")
            ArrayUser[ord(row7) - 62][colm7] = (Fore.WHITE + "B")
        elif decision5_5 == "h":
            ArrayUser[ord(row7) - 65][colm7] = (Fore.WHITE + "B")
            ArrayUser[ord(row7) - 65][colm7 + 1] = (Fore.WHITE + "B")
            ArrayUser[ord(row7) - 65][colm7 + 2] = (Fore.WHITE + "B")
            ArrayUser[ord(row7) - 65][colm7 + 3] = (Fore.WHITE + "B")
            
        if decision6_6 == "h":    
            ArrayUser[ord(row8) - 65][colm8] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 65][colm8 + 1] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 65][colm8 + 2] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 65][colm8 + 3] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 65][colm8 + 4] = (Fore.WHITE + "C")
        elif decision6_6 == "v":
            ArrayUser[ord(row8) - 65][colm8] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 64][colm8] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 63][colm8] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 62][colm8] = (Fore.WHITE + "C")
            ArrayUser[ord(row8) - 61][colm8] = (Fore.WHITE + "C")
    
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
                printboard(ArrayComputer)
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
        
                if ArrayComputer[ord(row) -65][colm] == (Fore.BLUE + "O"):
                    print(Fore.WHITE + "**********")
                else:
                    print()
        
                if list == computer_sub_location or list == computer_sub_location2 or list == computer_sub_location3 or list == computer_destoryer_location or list == computer_destoryer_location2 or list == computer_destoryer_location3 or list == computer_patrol_location or list == computer_patrol_location2 or list == computer_battle_location or list == computer_battle_location2 or list == computer_battle_location3 or list == computer_battle_location4 or list == computer_carrier_location or list == computer_carrier_location2 or list == computer_carrier_location3 or list == computer_carrier_location4 or list == computer_carrier_location5:
                    print(Fore.WHITE + "**********")
                    
                    if list == computer_sub_location or list == computer_sub_location2 or list == computer_sub_location3:
                        print(Fore.WHITE + "You have hit the computers Submarine")
                        ArrayComputer[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_destoryer_location or list == computer_destoryer_location2 or list == computer_destoryer_location3:
                        print(Fore.WHITE + "You have hit the computers Destroyer")
                        ArrayComputer[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_patrol_location or list == computer_patrol_location2:
                        print(Fore.WHITE + "You have hit the computers Patrol Boat")
                        ArrayComputer[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_battle_location or list == computer_battle_location2 or list == computer_battle_location3 or list == computer_battle_location4:
                        print(Fore.WHITE + "You have hit the computers Battleship")
                        ArrayComputer[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    if list == computer_carrier_location or list == computer_carrier_location2 or list == computer_carrier_location3 or list == computer_carrier_location4 or list == computer_carrier_location5:
                        print(Fore.WHITE + "You have hit the computers Carrier")
                        ArrayComputer[ord(row) - 65][colm] = (Fore.GREEN + "X")
                    
                    if ArrayComputer[row4][colm4] == (Fore.GREEN + "X") and ArrayComputer[row4][colm4 + 1] == (Fore.GREEN + "X") and ArrayComputer[row4][colm4 + 2] == (Fore.GREEN + "X"):
                        print("You have sunk the computers submarine!")
                        ArrayComputer[row4][colm4] = (Fore.BLACK + "X")
                        ArrayComputer[row4][colm4 + 1] = (Fore.BLACK + "X")
                        ArrayComputer[row4][colm4 + 2] = (Fore.BLACK + "X")
                    if ArrayComputer[row5][colm5] == (Fore.GREEN + "X") and ArrayComputer[row5 + 1][colm5] == (Fore.GREEN + "X") and ArrayComputer[row5 + 2][colm5] == (Fore.GREEN + "X"):
                        print("You have sunk the computers destroyer!")
                        ArrayComputer[row5][colm5] = (Fore.BLACK + "X")
                        ArrayComputer[row5 + 1][colm5] = (Fore.BLACK + "X")
                        ArrayComputer[row5 + 2][colm5] = (Fore.BLACK + "X")
                    if ArrayComputer[row9][colm9] == (Fore.GREEN + "X") and ArrayComputer[row9 + 1][colm9] == (Fore.GREEN + "X"):
                        print("You have sunk the computers Patrol Boat!")
                        ArrayComputer[row9][colm9] = (Fore.BLACK + "X")
                        ArrayComputer[row9 + 1][colm9] = (Fore.BLACK + "X")
                    if ArrayComputer[row10][colm10] == (Fore.GREEN + "X") and ArrayComputer[row10 + 1][colm10] == (Fore.GREEN + "X") and ArrayComputer[row10 + 2][colm10] == (Fore.GREEN + "X") and ArrayComputer[row10 + 3][colm10] == (Fore.GREEN + "X"):
                        print("You have sunk the computers Battleship!")
                        ArrayComputer[row10][colm10] = (Fore.BLACK + "X")
                        ArrayComputer[row10 + 1][colm10] = (Fore.BLACK + "X")
                        ArrayComputer[row10 + 2][colm10] = (Fore.BLACK + "X")
                        ArrayComputer[row10 + 3][colm10] = (Fore.BLACK + "X")
                    if ArrayComputer[row11][colm11] == (Fore.GREEN + "X") and ArrayComputer[row11 + 1][colm11] == (Fore.GREEN + "X") and ArrayComputer[row11 + 2][colm11] == (Fore.GREEN + "X") and ArrayComputer[row11 + 3][colm11] == (Fore.GREEN + "X") and ArrayComputer[row11 + 4][colm11] == (Fore.GREEN + "X"):
                        print("You have sunk the computers Carrier!")
                        ArrayComputer[row11][colm11] = (Fore.BLACK + "X")
                        ArrayComputer[row11 + 1][colm11] = (Fore.BLACK + "X")
                        ArrayComputer[row11 + 2][colm11] = (Fore.BLACK + "X")
                        ArrayComputer[row11 + 3][colm11] = (Fore.BLACK + "X")
                        ArrayComputer[row11 + 4][colm11] = (Fore.BLACK + "X")
                    
                    if ArrayComputer[row5][colm5] == (Fore.BLACK + "X") and ArrayComputer[row5 + 1][colm5] == (Fore.BLACK + "X") and ArrayComputer[row5 + 2][colm5] == (Fore.BLACK + "X") and ArrayComputer[row4][colm4] == (Fore.BLACK + "X") and ArrayComputer[row4][colm4 + 1] == (Fore.BLACK + "X") and ArrayComputer[row4][colm4 + 2] == (Fore.GREEN + "X") and ArrayComputer[row9][colm9] == (Fore.BLACK + "X") and ArrayComputer[row9 + 1][colm9] == (Fore.BLACK + "X") and ArrayComputer[row10][colm10] == (Fore.BLACK + "X") and ArrayComputer[row10 + 1][colm10] == (Fore.BLACK + "X") and ArrayComputer[row10 + 2][colm10] == (Fore.BLACK + "X") and ArrayComputer[row10 + 3][colm10] == (Fore.BLACK + "X") and ArrayComputer[row11][colm11] == (Fore.BLACK + "X") and ArrayComputer[row11 + 1][colm11] == (Fore.BLACK + "X") and ArrayComputer[row11 + 2][colm11] == (Fore.BLACK + "X") and ArrayComputer[row11 + 3][colm11] == (Fore.BLACK + "X") and ArrayComputer[row11 + 4][colm11] == (Fore.BLACK + "X"):
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
                    ArrayComputer[ord(row) -65][colm] = (Fore.RED + "M")
                    
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
                printboard(ArrayUser)
        
                computer_list= (computer_row, computer_colm)
                computer_guesses = (chr(computer_row + 65), computer_colm + 1)
                computer_guesslist.append(computer_guesses)
                print(Fore.WHITE + "These are the guesses the computer made:", computer_guesslist)
                
                if ArrayUser[computer_row][computer_colm] == (Fore.BLUE + "O"):
                    print(Fore.WHITE + "**********")
                    print(Fore.WHITE + "Me pepe est grande")
                else:
                    computer_row = random.randrange(0,9)
                    computer_colm = random.randrange(0,9)
                    

                if computer_list == user_sub_location or computer_list == user_sub_location2 or computer_list == user_sub_location3 or computer_list == user_destoryer_location or computer_list == user_destoryer_location2 or computer_list == user_destoryer_location3 or computer_list == user_patrol_location or computer_list == user_patrol_location2 or computer_list == user_battle_location or computer_list == user_battle_location2 or computer_list == user_battle_location3 or computer_list == user_battle_location4 or computer_list == user_carrier_location or computer_list == user_carrier_location2 or computer_list == user_carrier_location3 or computer_list == user_carrier_location4 or computer_list == user_carrier_location5:
                    print(Fore.WHITE + "**********")
                    if computer_list == user_sub_location or computer_list == user_sub_location2 or computer_list == user_sub_location3:
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                        print(Fore.WHITE + "Your submarine has been hit!")
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_destoryer_location or computer_list == user_destoryer_location2 or computer_list == user_destoryer_location3:
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                        print(Fore.WHITE + "Your Destroyer has been hit!")
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_patrol_location or computer_list == user_patrol_location2:
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                        print(Fore.WHITE + "Your Patrol Boat has been hit!")
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_battle_location or computer_list == user_battle_location2 or computer_list == user_battle_location3 or computer_list == user_battle_location4:
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                        print(Fore.WHITE + "Your Battleship has been hit!")
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                    if computer_list == user_carrier_location or computer_list == user_carrier_location2 or computer_list == user_carrier_location3 or computer_list == user_carrier_location4 or computer_list == user_carrier_location5:
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                        print(Fore.WHITE + "Your Carrier has been hit!")
                        ArrayUser[computer_row][computer_colm] = (Fore.GREEN + "X")
                    
                    if ArrayUser[ord(row2) - 65][colm2] == (Fore.GREEN + "X") and ArrayUser[ord(row2) - 65][colm2 + 1] == (Fore.GREEN + "X") and ArrayUser[ord(row2) - 65][colm2 + 2] == (Fore.GREEN + "X") or ArrayUser[ord(row2) - 65][colm2] == (Fore.GREEN + "X") and ArrayUser[ord(row2) - 64][colm2] == (Fore.GREEN + "X") and ArrayUser[ord(row2) - 63][colm2] == (Fore.GREEN + "X"):
                        print("Your submarine has been sunk!")
                        if decision2_2 == "h":
                            ArrayUser[ord(row2) - 65][colm2] = (Fore.BLACK + "X")
                            ArrayUser[ord(row2) - 65][colm2 + 1] = (Fore.BLACK + "X")
                            ArrayUser[ord(row2) - 65][colm2 + 2] = (Fore.BLACK + "X")
                        elif decision2_2 == "v":
                            ArrayUser[ord(row2) - 65][colm2] = (Fore.BLACK + "X")
                            ArrayUser[ord(row2) - 64][colm2] = (Fore.BLACK + "X")
                            ArrayUser[ord(row2) - 63][colm2] = (Fore.BLACK + "X")
                    if ArrayUser[ord(row3) -  65][colm3] == (Fore.GREEN + "X") and ArrayUser[ord(row3) - 65][colm3 + 1] == (Fore.GREEN + "X") and ArrayUser[ord(row3) - 65][colm3 + 2] == (Fore.GREEN + "X") or ArrayUser[ord(row3) -  65][colm3] == (Fore.GREEN + "X") and ArrayUser[ord(row3) - 64][colm3] == (Fore.GREEN + "X") and ArrayUser[ord(row3) - 63][colm3] == (Fore.GREEN + "X"):
                        print("Your Destroyer has been sunk!")
                        if decision3_3 == "h":
                            ArrayUser[ord(row3) - 65][colm3] = (Fore.BLACK + "X")
                            ArrayUser[ord(row3) - 65][colm3 + 1] = (Fore.BLACK + "X")
                            ArrayUser[ord(row3) - 65][colm3 + 2] = (Fore.BLACK + "X")
                        elif decision3_3 == "v":
                            ArrayUser[ord(row3) - 65][colm3] = (Fore.BLACK + "X")
                            ArrayUser[ord(row3) - 64][colm3] = (Fore.BLACK + "X")
                            ArrayUser[ord(row3) - 63][colm3] = (Fore.BLACK + "X")
                    if ArrayUser[ord(row6) - 65][colm6] == (Fore.GREEN + "X") and ArrayUser[ord(row6) - 65][colm6 + 1] == (Fore.GREEN + "X") or ArrayUser[ord(row6) - 65][colm6] == (Fore.GREEN + "X") and ArrayUser[ord(row6) - 64][colm6] == (Fore.GREEN + "X"):
                        print("Your Patrol Boat has been sunk!")
                        if decision4_4 == "v":
                            ArrayUser[ord(row6) - 65][colm6] = (Fore.BLACK + "X")
                            ArrayUser[ord(row6) - 64][colm6] = (Fore.BLACK + "X")
                        elif decision4_4 == "h":
                            ArrayUser[ord(row6) - 65][colm6]
                            ArrayUser[ord(row6) - 65][colm6 + 1] = (Fore.BLACK + "X")
                    if ArrayUser[ord(row7) - 65][colm7] == (Fore.GREEN + "X") and ArrayUser[ord(row7) - 64][colm7] == (Fore.GREEN + "X") and ArrayUser[ord(row7) - 63][colm7] == (Fore.GREEN + "X") and ArrayUser[ord(row7) - 62][colm7] == (Fore.GREEN + "X") or ArrayUser[ord(row7) - 65][colm7] == (Fore.GREEN + "X") and ArrayUser[ord(row7) - 65][colm7 + 1] == (Fore.GREEN + "X") and ArrayUser[ord(row7) - 65][colm7 + 2] == (Fore.GREEN + "X") and ArrayUser[ord(row7) - 65][colm7 + 3] == (Fore.GREEN + "X"):
                        print("Your Battleship has been sunk!")
                        if decision5_5 == "v":
                            ArrayUser[ord(row7) - 65][colm7] = (Fore.BLACK + "X")
                            ArrayUser[ord(row7) - 64][colm7] = (Fore.BLACK + "X")
                            ArrayUser[ord(row7) - 63][colm7] = (Fore.BLACK + "X")
                            ArrayUser[ord(row7) - 62][colm7] = (Fore.BLACK + "X")
                        elif decision5_5 == "h":
                            ArrayUser[ord(row7) - 65][colm7] = (Fore.BLACK + "X")    
                            ArrayUser[ord(row7) - 65][colm7 + 1] = (Fore.BLACK + "X")
                            ArrayUser[ord(row7) - 65][colm7 + 2] = (Fore.BLACK + "X")
                            ArrayUser[ord(row7) - 65][colm7 + 3] = (Fore.BLACK + "X")
                    if ArrayUser[ord(row8) - 65][colm8] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 65][colm8 + 1] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 65][colm8 + 2] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 65][colm8 + 3] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 65][colm8 + 4] == (Fore.GREEN + "X") or ArrayUser[ord(row8) - 65][colm8] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 64][colm8] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 63][colm8] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 62][colm8] == (Fore.GREEN + "X") and ArrayUser[ord(row8) - 61][colm8] == (Fore.GREEN + "X"):
                        print("Your Carrier has been sunk!")
                        if decision6_6 == "h":
                            ArrayUser[ord(row8) - 65][colm8] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 65][colm8 + 1] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 65][colm8 + 2] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 65][colm8 + 3] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 65][colm8 + 4] = (Fore.BLACK + "X")
                        elif decision6_6 == "v":
                            ArrayUser[ord(row8) - 65][colm8] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 64][colm8] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 63][colm8] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 62][colm8] = (Fore.BLACK + "X")
                            ArrayUser[ord(row8) - 61][colm8] = (Fore.BLACK + "X")
                    if ArrayUser[ord(row3) - 65][colm3] == (Fore.BLACK + "X") and ArrayUser[ord(row3) - 65][colm3 + 1] == (Fore.BLACK + "X") and ArrayUser[ord(row3) - 65][colm3 + 2] == (Fore.BLACK + "X") and ArrayUser[ord(row2) - 65][colm2] == (Fore.BLACK + "X") and ArrayUser[ord(row2) - 65][colm2 + 1] == (Fore.BLACK + "X") and ArrayUser[ord(row2) - 65][colm2 + 2] == (Fore.BLACK + "X") and ArrayUser[ord(row6) - 65][colm6] == (Fore.BLACK + "X") and ArrayUser[ord(row6) - 64][colm6] == (Fore.BLACK + "X") and ArrayUser[ord(row7) - 65][colm7] == (Fore.BLACK + "X") and ArrayUser[ord(row7) - 64][colm7] == (Fore.BLACK + "X") and ArrayUser[ord(row7) - 63][colm7] == (Fore.BLACK + "X") and ArrayUser[ord(row7) - 62][colm7] == (Fore.BLACK + "X") and ArrayUser[ord(row8) - 65][colm8] == (Fore.BLACK + "X") and ArrayUser[ord(row8) - 65][colm8 + 1] == (Fore.BLACK + "X") and ArrayUser[ord(row8) - 65][colm8 + 2] == (Fore.BLACK + "X") and ArrayUser[ord(row8) - 65][colm8 + 3] == (Fore.BLACK + "X") and ArrayUser[ord(row8) - 65][colm8 + 4] == (Fore.BLACK + "X"):
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
                    ArrayUser[computer_row][computer_colm] = (Fore.RED + "M")
                
                computer_row = random.randrange(0,9)
                computer_colm = random.randrange(0,9)    
                computer_round += 1
                    
                if round > 25 and computer_list == user_sub_location or round > 25 and computer_list == user_sub_location2 or round > 25 and computer_list == user_sub_location3 or round > 25 and computer_list == user_destoryer_location or round > 25 and computer_list == user_destoryer_location2 or round > 25 and computer_list == user_destoryer_location3 or round > 25 and computer_list == user_patrol_location or round > 25 and computer_list == user_patrol_location2 or round > 25 and computer_list == user_battle_location or round > 25 and computer_list == user_battle_location2 or round > 25 and computer_list == user_battle_location3 or round > 25 and computer_list == user_battle_location4 or round > 25 and computer_list == user_carrier_location or round > 25 and computer_list == user_carrier_location2 or round > 25 and computer_list == user_carrier_location3 or round > 25 and computer_list == user_carrier_location4 or round > 25 and computer_list == user_carrier_location5:
                    print(Fore.WHITE + "Wow you lost to the computer the last round. Good Game")
                    continue
                    
                break


battleship()
