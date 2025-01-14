#Day 4
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
import random

print("Welcome to Rock, Paper, Scissors")
user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))

choices = [rock, paper, scissors]
comp_choice = random.choice(choices)

if user_choice == 0 :

    if comp_choice == rock :
        print(f"You choose Rock\n{rock}")
        print(f"Computer also choose Rock\n{rock}")
        print("It' a Draw !")

    elif comp_choice == paper :
        print(f"You choose Rock\n{rock}")
        print(f"Computer choose Paper\n{paper}")
        print("You Loose !")

    elif comp_choice == scissors :
        print(f"You choose Rock\n{rock}")
        print(f"Computer choose Scissors\n{scissors}")
        print("You Won !")

elif user_choice == 1 :

    if comp_choice == rock :
        print(f"You choose Paper\n{paper}")
        print(f"Computer choose Rock\n{rock}")
        print("You Won !")

    elif comp_choice == paper :
        print(f"You choose Paper\n{paper}")
        print(f"Computer also choose Paper\n{paper}")
        print("It' a Draw !")

    elif comp_choice == scissors :
        print(f"You choose Paper\n{paper}")
        print(f"Computer choose Scissors\n{scissors}")
        print("You Loose !")

elif user_choice == 2 :

    if comp_choice == rock :
        print(f"You choose Scissors\n{scissors}")
        print(f"Computer choose Rock\n{rock}")
        print("You Lose !")

    elif comp_choice == paper :
        print(f"You choose Scissors\n{scissors}")
        print(f"Computer choose Paper\n{paper}")
        print("You Won !")

    elif comp_choice == scissors :
        print(f"You choose Scissors\n{scissors}")
        print(f"Computer choose Scissors\n{scissors}")
        print("It's a Draw ")

else:
    print("Invalid Choice !")







