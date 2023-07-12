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
        
    row = input("Please guess a row :(0/1/2/3/4) ")
    if row in ('0', '1', '2', '3', '4'):
        print("Please continue")
    else:
        if row != ('0', '1', '2', '3', '4'):
            print("Good try sucker now enter either 0/1/2/3/4")
            row = input("Please guess a row :(0/1/2/3/4) ")
    
    colm = input("Please guess a column :(0/1/2/3/4) ")
    if colm in ('0', '1', '2', '3', '4'):
        print("Please continue")
    else:
        if colm != ('0', '1', '2', '3', '4'):
            print("Good try sucker now enter either 0/1/2/3/4")
            colm = input("Please guess a column :(0/1/2/3/4) ")


battleship()


