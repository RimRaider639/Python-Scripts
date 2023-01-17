def hangman():
  
  #Functions
  def display():
    print('\n   HANGMAN GAME')
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
      return(1)
    else:
      return(0)
    
  #Variables
  win_stat=0
  hang={1:'/', 2:"\\", 3:"/", 4:"\\", 5:"|", 6:"O"}
  x=1

  #Hangman game
  word=shuffle()
  out=word[0]+'_'*(len(word)-2)+word[-1]

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

if __name__=='__main__':
  hangman()