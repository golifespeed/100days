import random
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

while not game_over:
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

    if "_" not in display:
        game_over=True
        print("You Win!")

