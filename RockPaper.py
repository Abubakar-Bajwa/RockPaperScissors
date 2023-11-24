rock = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
 """
paper = """ 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""
scissors = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
#player_choice = int(
#   input("please choose 0 for rock, 1 for paper and 2 for scissors: "))
player_choice = 0
import random


map_text = [rock, paper, scissors]
while player_choice <= 2:
    player_choice = int(
        input("please choose 0 for rock, 1 for paper and 2 for scissors: "))
    computer_choice = random.randint(0, 2)
    if computer_choice == player_choice:

        print(
            f"\nThe player chose {map_text[player_choice]}\n and computer chose {map_text[computer_choice]}\nit's a draw."
        )

    elif player_choice == 0 and computer_choice == 2:
        print(
            f"\nThe player chose {map_text[player_choice]}\n and computer chose {map_text[computer_choice]}\n you win!"
        )

    elif player_choice == 2 and computer_choice == 0:
        print(
            f"\nThe player chose {map_text[player_choice]}\n and computer chose {map_text[computer_choice]}\nyou Lose."
        )

    elif player_choice > computer_choice and player_choice < 3 :
        print(
            f"\nThe player chose {map_text[player_choice]}\n and computer chose {map_text[computer_choice]}\n you win!"
        )

    elif player_choice < computer_choice and player_choice < 3 :
        print(
            f"\nThe player chose {map_text[player_choice]}\n and computer chose {map_text[computer_choice]}\n you lose."
        )

print("Thanks for playing the game")
