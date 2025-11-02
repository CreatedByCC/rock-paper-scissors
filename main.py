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

hand_signs = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
computer = random.randint(0, 2)

if player < 0 or player > 2:
    print("Invalid choice. You lose!")
else:
    print(hand_signs[player])
    print("Computer choose:")
    print(hand_signs[computer])

    if player == computer:
        print("It's a draw")
    elif (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
        print("You lose")
    else:
        print("You win")
