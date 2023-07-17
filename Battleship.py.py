#BattleShip

def battleship() :
    
    
    round = 1
    import random
    row2 = random.randrange(0,5)
    colm2= random.randrange(0,5)


    ship_location = (row2, colm2)
    #print(ship_location)

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
        
        
        
    ask()



    arr = [["O", "O", "O", "O", "O"],
           ["O", "O", "O", "O", "O"], 
           ["O", "O", "O", "O", "O"], 
           ["O", "O", "O", "O", "O"],
           ["O", "O", "O", "O", "O"]]

    def printboard():
        for r in range(len(arr)):
            print(arr[r])
            print()

    row = 0
    colm = 0
        
    while True:
        while round < 6 :
            print ("Round", round)
            printboard()
            while True:
                try:
                    row = int(input("Please guess a row :(0/1/2/3/4): "))
                except ValueError:
                    print("Please type only 0, 1, 2, 3, or 4")
                    continue
                if row in (0, 1, 2, 3, 4):
                    print("Thank you, now please continue to the next section")
                else:
                    if row != (0, 1, 2, 3, 4):
                        print("Good try sucker now enter either 0/1/2/3/4")
                        row = int(input("Please guess a row :(0/1/2/3/4): "))
                break
    
            while True:
                try:
                    colm = int(input("Please guess a column :(0/1/2/3/4): "))
                except ValueError:
                    print("Please type only 0, 1, 2, 3, or 4")
                    continue
                if colm in (0, 1, 2, 3, 4):
                    print("Thank you")
                else:
                    if colm != (0, 1, 2, 3, 4):
                        print("Good try sucker now enter either 0/1/2/3/4")
                        colm = int(input("Please guess a column :(0/1/2/3/4): "))
                break
        
            list= (row, colm)
            guess_list = []
            guess_list.append(list)
            
            
            print(guess_list)
        
            if arr[row][colm] == "O":
                print("**********")
            else:
                print("You already chose that coordinate!")
        

            if list == ship_location:
                print("You hit the battleship!")
                arr[row][colm] = "X"
                printboard()
                print("Congraulations, you have beaten my very hard game of Battle Ship")
                try_again = input("Would you like to play again? :(y/n): ")
                if try_again == "y":
                    battleship()
                elif try_again == "n":
                    print("Ok loser, now GTFO of my code")
                    exit()
                else:
                    print("Please type y or n you dumdum poopoo head")
                    try_again = input("Would you like to play again? :(y/n): ")

            else:
                print("You missed! Try again!")
                arr[row][colm] = "M"
            round +=1
        if round > 6 and list == ship_location:
            print("Dang you lucky son of a gun you got it. COngrats you win")
            continue
        else:
            print("You lose sucker MUAH HA HA HA HA HA HA HA HA")
            break


battleship()

        
    
            
            
#use for loop for row and colm guessing- needs to cycle through three times

#if guess = correct row and colm
    #print("Congraulations, you have won BattleShip")
#elif guess != correct row and colm and not all 3 guesses have been used
    #print("You missed my BattleShip, please guess a row and column again")
    #row = input("Please guess a row :(0/1/2/3/4) ")
    #if row in ('0', '1', '2', '3', '4'):
        #print("Thank you, now please continue to the next section")
    #else:
        #if row != ('0', '1', '2', '3', '4'):
            #print("Good try sucker now enter either 0/1/2/3/4")
            #row = input("Please guess a row :(0/1/2/3/4) ")
    
    #colm = input("Please guess a column :(0/1/2/3/4) ")
    #if colm in ('0', '1', '2', '3', '4'):
        #print("Thank you")
    #else:
        #if colm != ('0', '1', '2', '3', '4'):
            #print("Good try sucker now enter either 0/1/2/3/4")
            #colm = input("Please guess a column :(0/1/2/3/4) ")
#else guess != correct row and colm and all 3 guesses have been used
    #print("You missed my BattleShip, and you lose hahahahahaha")
    

