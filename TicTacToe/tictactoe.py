def tictactoe():
  ###### Imports #############

  from colorama import Fore, init
  init()

  ##### Variables ############

  dis={1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
  p1_wins=p2_wins=0
  draws=0
  times=0
  prev_winner=0 #previous winner
  x='Do you want to play'
  y='Invalid value, try again!\n'
  p_1='' #choose the symbol
  p_2=''

  ########## Functions ###########

  def turn(player,position,symbol):
    while True:
      try:
        position=int(input(f'{player}, make your move: ')) 
      except ValueError:
        print(y)
        continue
      if position not in dis.values():
        print(y)
        continue
      else:
        replace(position,symbol)
        break

  #display
  def display(dis):
    print(f'{Fore.BLUE}___________________  \n|     |     |     |\n|  {dis[1]}  |  {dis[2]}  |  {dis[3]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {dis[4]}  |  {dis[5]}  |  {dis[6]}  |\n|_____|_____|_____|\n|     |     |     |\n|  {dis[7]}  |  {dis[8]}  |  {dis[9]}  |\n|_____|_____|_____|\n{Fore.WHITE}')

  #replacing with xo
  def replace(inp, xo):
    print('')
    dis[inp]=Fore.WHITE+ xo +Fore.BLUE
    display(dis)

  #check win
  def win(p):
    if dis[1]==dis[2]==dis[3] or dis[4]==dis[5]==dis[6] or dis[7]==dis[8]==dis[9] or dis[1]==dis[4]==dis[7] or dis[2]==dis[5]==dis[8] or dis[3]==dis[6]==dis[9] or dis[1]==dis[5]==dis[9] or dis[3]==dis[5]==dis[7]:
      print(f'{p} WON!')
      print('\n#########################\n')
      return(1)

  #order maker
  def order():
    if prev_winner in [0,'Player 1', 'draw_Player 2']:
      print('Player 1 goes first!\n\n#########################\n')
      return([['Player 1', pos_1, p_1], ['Player 2', pos_2, p_2]])
    else:
      print('Player 2 goes first!\n\n#########################\n')
      return([['Player 2', pos_2, p_2], ['Player 1', pos_1, p_1]])

  #####################################

  #Display
  print(f'\n###### {Fore.YELLOW}TICTACTOE!{Fore.WHITE} ######\n')
  display(dis)
  print(f'######### {Fore.GREEN}RULES{Fore.WHITE} #########\n\n>{Fore.GREEN}Enter the number where you want to input your symbol.\n{Fore.WHITE}>{Fore.GREEN}The first to line up their symbol wins.{Fore.WHITE}\n\n#########################\n')

  while True:
    times=p1_wins+p2_wins+draws
    dis={1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
    count=0 #counts the number of moves

    #ask to play
    if times>0:
      x+=' again'
    ask=input(x+'? (y/n) ').lower()
    if ask=='n':
      print('\n#########################\n')
      print(f'Player 1 wins: {p1_wins}\nPlayer 2 wins: {p2_wins}\nDraws: {draws}\n')
      print('Have a nice day!')
      break
      
    elif ask not in ['y','n']:
      print(y)
      continue

    else:
      if times>0:
        print('\n#########################\n')
        display(dis)

      #game

      #ask to choose
      print('\n#########################\n')
      while True:
        p_1=input('Player 1 choose a symbol (X/O): ').upper()
        if p_1 not in ['X','O']:
          print(y)
          continue
        else:
          p_2=[i for i in ['X','O'] if i!=p_1]
          p_2=p_2[0]
          print('Player 2 will play as %s.'%(p_2))
          print('\n#########################\n')

        #players taking turns
          pos_1=pos_2=0
          ord=order()
          
          for i in range(5):
            for o in ord:
              turn(o[0], o[1], o[2])
              count+=1
              w=win(o[0])
              prev_winner=o[0]
              if w==1:
                if o[0]=='Player 1':
                  p1_wins+=1
                else:
                  p2_wins+=1
                break
              elif count==9:
                break
            if w==1:
              break
          
          else:
            print('The match ended in a draw!')    
            print('\n#########################\n')
            draws+=1
            prev_winner='draw_'+ord[0][0]

          break

if __name__=='__main__':
  tictactoe()