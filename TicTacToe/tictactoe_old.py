# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def game_on():
    from IPython.display import clear_output
    reply= 'a'
    while reply not in ('Y','N'):
        reply= input("Do you want to start the game? (Y or N)\n")
        
        if reply not in ('Y', 'N'):
            clear_output()
            print("Sorry didn't understand you. Please type Y or N.")
    if reply=='Y':
        clear_output()
        return True
    else:
        clear_output()
        return False          
def display_board(row1, row2, row3):
    print("TIC TAC TOE !!!")
    print('     |     |     ')
    print(f'  {row1[0]}  |  {row1[1]}  |  {row1[2]}  ')
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print(f'  {row2[0]}  |  {row2[1]}  |  {row2[2]}  ')
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print(f'  {row3[0]}  |  {row3[1]}  |  {row3[2]}  ')
    print('     |     |     ')
def Player_xo():
    from IPython.display import clear_output
    global P_one
    global P_two
    xo= 'a'
    while xo not in ('X','O'):
        xo= input("Do you wanna play as X or O? ")
        
        if xo not in ('X', 'O'):
            clear_output()
            print("Sorry didn't understand you. Please type X or O.")
    if xo=='X':
        P_one='X'
        P_two='O'
        print("You're player 1! Start playing:")
        return True
        
    else:
        P_one='O'
        P_two='X'
        print("You're player 1! Start playing:")
        return True
def position(P, row1, row2, row3, Map):
    position= 'a'
    
    while not position.isdigit() or int(position) not in range(1,10) or Map[int(position)] in ('X', 'O'):
        position= input(f'Where do you wanna put your {P}? (1-9)')
        if position.isdigit():
            if int(position) not in range(1,11):
                
                print('Out of range! Please put a value within 1-9.')
            elif Map[int(position)] in ('X', 'O'):
                
                print(f'The position already holds an {Map[int(position)]}. Please try again:')
        else:
            
            print("Invalid input. Please enter a value (1-9).")
    if position.isdigit() and int(position) in range(1,10) and Map[int(position)] not in ('X','O'):
        Map[int(position)]=P
        if 0<int(position)<4:
            row1[row1.index(position)]= P
        elif 3<int(position)<7:
            row2[row2.index(position)]= P
        else: 
            row3[row3.index(position)]= P
        return Map
def winning_move(Map, P):
    d=Map
    if [P,P,P] == [d[1],d[2],d[3]] or [P,P,P] == [d[4],d[5],d[6]] or [P,P,P] == [d[7],d[8],d[9]] or [P,P,P] == [d[1],d[4],d[7]] or [P,P,P] == [d[2],d[5],d[8]] or [P,P,P] == [d[3],d[6],d[9]] or [P,P,P] == [d[1],d[5],d[9]] or [P,P,P] == [d[3],d[5],d[7]]:
        print('------YOU WON!------')
        return True
    elif list(Map.values()).count(P)==5:
        print('------DRAW!------')
        return True
    else:
        return False


print("TIC TAC TOE !!!")
from IPython.display import clear_output
while game_on():
    row1= ['1','2','3']
    row2= ['4','5','6']
    row3= ['7','8','9']
    moves=[]
    Map= {1:row1[0], 2:row1[1], 3:row1[2], 4:row2[0], 5:row2[1], 6:row2[2], 7:row3[0], 8:row3[1], 9:row3[2]}
    Player_xo()
    while True:
        if moves!=[]:
            clear_output()
            
        display_board(row1, row2, row3)
        if len(moves)%2==0:
            P=P_one
            Map= position(P, row1, row2, row3, Map)
            
            if not winning_move(Map ,P):
                moves.append(0)
                continue
            else:
                break
        else:
            P=P_two
            position(P, row1, row2, row3, Map)
            if not winning_move(Map,P):
                moves.append(0)
                continue
            else:
                break   
else:
    print('Have a nice day!')
        
            
            
            


    