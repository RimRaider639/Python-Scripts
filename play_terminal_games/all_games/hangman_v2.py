def hangman_code():
  
  #Functions
  def display():
    print('\n###### HANGMAN GAME ######\n')
    print(f"       _____ \n      |    ||\n      {hang[6]}    ||\n     {hang[3]}{hang[5]}{hang[4]}   ||\n     {hang[1]} {hang[2]}   ||")

  def shuffle():
    import random
    words=['word', 'love', 'mail', 'sun', 'moon', 'tree', 'beauty', 'sick', 'normal', 'deal', 'bill', 'smile', 'sail', 'delight', 'weird', 'warrior', 'barrier', 'single', 'enthusiasm', 'rain', 'mystery']
    random.shuffle(words)
    return(words[0])

  def check(inp, word, out, similar):
    if inp in word:
      out=list(out)
      for i in range(len(word)):
        if inp==word[i]:
          out[i]=word[i]
          similar=1
    return(''.join(out), similar)

  def win(out):
    if '_' not in out:
      print(f'YOU WON! THE WORD WAS {out}.')
      print('\n#####################\n')
      return(1)
    else:
      return(0)

  def dash(word):
    from random import randint
    num_of_dashes=randint(2,len(word)-1)
    word=list(word)
    for i in range(num_of_dashes):
      word[randint(0,len(word)-1)]='_'
    return(word)
    
  #Variables
  win_stat=0
  hang={1:'/', 2:"\\", 3:"/", 4:"\\", 5:"|", 6:"O"}
  x=1

  #Hangman game
  word=shuffle()
  out=dash(word)

  while x<7:
    similar=0
    if win_stat==0:
      display()
      print(f"\n{' '.join(list(out))}\n")

      #The interactive part
      win_stat=win(out)
      if win_stat!=1:
        inp=input('Guess a letter: ')
        out, similar=check(inp, word, out, similar)
        
        if similar==0:
          hang[x]=' '
          x+=1

      else:
        break

  else:
    print(f'\nGAME OVER! THE WORD WAS {word}.')   
    print('\n#####################\n') 
  
  return(win_stat)

def hangman():
  c=1
  w=hangman_code()
  while True:
    ask=input('Do you want to play again? (y/n) ').lower()
    if ask not in ['y','n']:
      print("Invalid value, try again!")
      continue
    elif ask=='n':
      print('\n#####################\n')
      print(f'Wins: {w}/{c}\n\nHave a nice day!')
      break
    else:
      w+=hangman_code()
      c+=1
          
if __name__=='__main__':
  hangman()
              

