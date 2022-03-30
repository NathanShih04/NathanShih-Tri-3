from random import randint

options = ["rock", "paper", "scissors"]
cpuchoice = options[randint(0,2)]

userchoice = input("rock, paper, scissors? ")

if userchoice == cpuchoice:
  print("tie, yall suck")

elif userchoice == "rock":
  if cpuchoice == "paper":
    print("u lost lmao L + bozo + ratio + nerd")
    
  else:
    print("u won! thank god ur not that bad")

elif userchoice == "paper":
  if cpuchoice == "scissors":
    print("u lost lmao L + bozo + ratio + nerd")
    
  else:
    print("u won! thank god ur not that bad")

elif userchoice == "scissors":
  if cpuchoice == "rock":
    print("u lost lmao L + bozo + ratio + nerd")
    
  else:
    print("u won! thank god ur not that bad")

else:
  print("thats not the right input")