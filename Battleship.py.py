#BattleShip

def battleship() :

    decision = input("Are you ready to play Battle ship? :(y/n) ")
    if decision == "y":
        print("Now we shall begin with this glorious exercise testing ones strengh and wit")
    elif decision == "n":
        print("OK, goodbye you bum piece of poopoo crap now GTFO")
        exit()
    else: 
        print("Hell to daw naw, to daw naw naw naw- no please enter either y or n")
        decision = input("Are you ready to play Battle ship? :(y/n) ")



    arr = [["O", "O", "O", "O", "O"],
           ["O", "O", "O", "O", "O"], 
           ["O", "O", "O", "O", "O"], 
           ["O", "O", "O", "O", "O"],
           ["O", "O", "O", "O", "O"]]

    def printboard():
        for r in range(len(arr)):
            print(arr[r])
            print()

    printboard()


    
        
    row = input("Please guess a row :(0/1/2/3/4) ")
    if row in ('0', '1', '2', '3', '4'):
        print("Thank you, now please continue to the next section")
    else:
        if row != ('0', '1', '2', '3', '4'):
            print("Good try sucker now enter either 0/1/2/3/4")
            row = input("Please guess a row :(0/1/2/3/4) ")
    
    colm = input("Please guess a column :(0/1/2/3/4) ")
    if colm in ('0', '1', '2', '3', '4'):
        print("Thank you")
    else:
        if colm != ('0', '1', '2', '3', '4'):
            print("Good try sucker now enter either 0/1/2/3/4")
            colm = input("Please guess a column :(0/1/2/3/4) ")
    print("You guessed row", row, "and column", colm)
    
            
            
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
            
        


battleship()


