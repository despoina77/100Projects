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

#Write your code below this line 👇
start = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors ").lower()

if start == 0:
    print(rock)
elif start == 1:
    print(paper)
else:
    print(scissors)

start_rand = str(random.randint(0, 2))
print(f"Computer choose: {start_rand}")

if start_rand == 0:
    print(rock)
elif start_rand == 1:
    print(paper)
else:
    print(scissors)
  

if start == 0 and start_rand == 1:
  print("You lose!")
elif start == 0 and start_rand == 2:
  print("You win!!")
elif start == 0 and start_rand == 0:
  print("Draw!")

