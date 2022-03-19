from random import randint

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
answer = randint(1, 100)
guess = 0
easy = 10
hard = 5
def difficulty():
    start = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if start == "easy":
        return easy
    else:
        return hard
turn = difficulty()
def guess_answer(guess, answer, turn):
    if guess > answer:
        print("Too high")
        return turn - 1
    elif guess < answer:
        print("Too low")
        return turn - 1
    else:
        print("You got it!")
while guess!= answer:
    print(f"You have {turn} attempts remaining!")
    guess = int(input("Make a guess: "))
    turn = guess_answer(guess, answer, turn)

    if turn == 0:
        print("You have no tries! You lose")
        break
    elif guess!= answer:
        print("Guess again")




















