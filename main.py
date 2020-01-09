import functions
from random import choice
rules={
  'rock':'paper',
  'paper':'scissor',
  'scissor':'rock'
}
options=['rock','paper','scissor']

while True:
  user=input("Enter your choice ")
  sys=rules[choice(options)]

  if user in ('quit', 'exit'): 
    break 
  elif user in rules:
    options.append(user)
    print('Systems choice ', sys)
  else: 
    print(" not a valid choice")  
  print(functions.rockpaperscissor(user,sys,rules))