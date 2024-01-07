"""Zerak Hassan
This is a tic_tac_toe program
Start: 16:30 08/24/2021
End:18:00 08/24/2021"""
#at some point may need to create an ai that doesn't pick random positions
import random
positions=[["_","_","_"],["_","_","_"],["_","_","_"]]

def check_win(array):#this function checks if anyone has met the winning conditions
    for n in range(3):
        if array[n][0] == array[n][1] == array[n][2] != "_":#checks for vertical matches
            return(str(array[n][1])+" wins!")
        else:
            pass
        if array[0][n] == array[1][n] == array[2][n] != "_":#checks for diaginal matches
            return(str(array[0][n])+" wins!")
        else:
            pass
    if array[0][0] == array[1][1] == array[2][2] != "_":#checks for diagnal match 1
        return(str(array[1][1])+" wins!")
    elif array[0][2] == array[1][1] == array[2][0] != "_":#checks for diagnal match 2
        return(str(array[1][1])+" wins!")
    else:
        pass
    return(False)#if nothing is found then False is returned

def check_full(array):#checks to see if the bord is full
    for n in array:
        for i in n:
            if i=="_":
                full=False
                return(full)
            else:
                full=True
    return(full)

def draw(state):#draws the current state of the board
    print(" ¦ 1 ¦ 2 ¦ 3")
    print("1¦ "+str(state[0][0])+" ¦ "+str(state[0][1])+" ¦ "+str(state[0][2]))
    print("2¦ "+str(state[1][0])+" ¦ "+str(state[1][1])+" ¦ "+str(state[1][2]))
    print("3¦ "+str(state[2][0])+" ¦ "+str(state[2][1])+" ¦ "+str(state[2][2]))

def ai_pick(array):#stupid robot picks randomly
    picked=False
    while picked == False:
        var1=random.randint(0,2)
        var2=random.randint(0,2)
        if array[var1][var2]=="_":#makes sure that spot isnt taken
            array[var1][var2]="O"
            picked=True
            return(array)
        else:
            pass

while check_win(positions) == False and check_full(positions) == False:#program will run as long as the bord isn't full & no one has won
    draw(positions)
    try:
        row=int(input("Row: "))
        column=int(input("Column: "))
        if positions[row-1][column-1]=="_":#checks to see if spot is taken
            positions[row-1][column-1]="X"
            if check_full(positions) == False:#checks if board is full
                pass
            else:
                break
            if check_win(positions)== False:#checks if player has won
                positions = ai_pick(positions)
            else:
                break
        else:
            print("position is already taken")
    except:
        print("Invalid input")

draw(positions)#draws the final positions of the board1
if check_win(positions)==False:
    print("Tie")#if nobody has won then is tie
else:
    print(check_win(positions))#displays the winner
