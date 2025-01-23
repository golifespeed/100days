import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list=["aardvark", "baboon", "camel" ,"elephant", "tiger", "giraffe", "crocodile"]
chosen_word=random.choice(word_list)

print(chosen_word)

letter_len = len(chosen_word)

placeholder=""
for position in range (letter_len):
    placeholder+="_"

print(placeholder)

correct_letters=[]

game_over=False
error_count=0

while not game_over and error_count<6:
    guess=input("Guess a letter: ").lower()
    display=""
    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
    print(stages[error_count])
    if guess not in chosen_word:
        error_count+=1
        print(display)
        print(stages[error_count])

    if "_" not in display:
        game_over=True
        print("You Win!")

if error_count>=6:
    print("You Lose!")
        

