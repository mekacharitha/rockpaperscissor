def rockpaperscissor(user,sys,rules):
  if rules[sys] == user: 
      return('yay you win!')
  elif rules[user] == sys: 
      return('the computer beat you... :(')
  else: 
      return("it's a tie!")
 
  
