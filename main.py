import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# user choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# user bad choice
if user_choice > 2 or user_choice < 0:
  print("You take a wrong number or character. You lose.")
else:
  # pc choice
  pc_choice = random.randint(0, 2)
  print(pc_choice)
  # list from pictures  
  list_of_pictures = [rock, scissors, paper]
  # print certain picture from list  
  print("Your choice is \n")
  print(list_of_pictures[user_choice])
  print("Computer choose \n")
  print(list_of_pictures[pc_choice])

  # game logic
  if user_choice == pc_choice:
    print("It is a draw.")
  elif user_choice == 0 and pc_choice == 2:
    print("You lose.")
  elif user_choice == 2 and pc_choice == 0:
    print("You win!")
  elif user_choice == 1 and pc_choice == 0:
    print("You lose.")
  elif user_choice == 0 and pc_choice == 1:
    print("You win!")
  elif user_choice == 2 and pc_choice == 1:
    print("You lose.")
  elif user_choice == 1 and pc_choice == 2:
      print("You win!")

