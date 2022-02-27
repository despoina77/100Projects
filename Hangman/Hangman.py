import random
import hangman_words
from hangman_art import logo
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(logo)
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6


print(f'The solution is {chosen_word}.')

display = []
for _ in range(len(chosen_word)):
    display += "_"

end_game = False
while not end_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
      print(f"You've guessed {guess}")

#Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
      print(f"You guessed {guess}! You lose a life!")
      lives -= 1
  if lives == 0:
      end_game == True
      print("You lose!")

  print(f"{' '.join(display)}")
  if "_" not in display:
    end_game = True
    print("You win!!")
  from hangman_art import stages
  print(stages[lives])