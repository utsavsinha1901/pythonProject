#This is the program for Treasure Island.
# Come and try your Luck.
print("Left or Right\n")
dchoice = str (input())
if dchoice == "Left" :
  print("Swim or Wait\n")
  schoice = str(input())
  if schoice == "Swim" :
    print("Game Over")
  elif schoice == "Wait" :
    print("Which Door you want to choose Red,Yellow or Blue?\n")
    tchoice = str(input())
    if tchoice == "Red" :
      print("Game Over")
    elif tchoice == "Blue" :
      print("Game Over")
    elif tchoice == "Yellow" :
      print("You Won")
else :
  print("Game Over")

