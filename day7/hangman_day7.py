import random
import hangman_art
import hangman_words

print(hangman_art.welcome)
print(hangman_art.logo)

chosen_word=random.choice(hangman_words.word_list)

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
    if guess in correct_letters:
        print(f"You've already guessed {guess}!")
    display=""
    for letter in chosen_word:
        if guess==letter:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"

    if guess not in chosen_word:
        error_count+=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print("**** "+str(6-error_count)+" lives left! ****")
    
    print(display)
    print(hangman_art.stages[error_count])

    if "_" not in display:
        game_over=True
        print("******************** YOU WIN! ********************")

if error_count>=6:
    print("******************** YOU LOSE! ********************")
    print("The correct word is: " + chosen_word)
