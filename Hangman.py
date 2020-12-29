#Build a hangman game
import random
import HangmanArt
import HangmanWords



#print ASCII art from "stages"
print(HangmanArt.logo)


end_of_game = False

#List of words
word_list = HangmanWords.word_list

#Let the computer generate random word
chosen_word = random.choice(word_list)

#to count the number of letter in the word
word_length = len(chosen_word)


#set lives to equal 6
lives = 6


#for test only
#print(f'Pssst, the solution is {chosen_word}.')



#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    

    #if user typed in the same letter before, we will let him know
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    #get a track record of lives. If lives goes down to "zero", you lose.
    if guess not in chosen_word:

        print(f"You've guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    

    print(f"{' '.join(display)}")
    

    if "_" not in display:
        end_of_game = True
        print("You win!")


    #print ASCII art from "stages"
    print(HangmanArt.stages[lives])

"""
#A loop to guess each letter at every position
    for char in chosen_word:
        if char == guess:
            display.append(guess)
            

        else:
            display.append("_")



    print(display)
"""