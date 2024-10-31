#Importing random and two other modules that stores the hangman graphics and the multiple amount of words that can be chosen to guess
import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list) #choosing a word from the word_list that is stored in the module: hangman_words

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length): #printing out _ in the amount: length of the chosen word
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over: #RUNS WHILE GAME_OVER IS STILL FALSE OR STILL NOT OVER

    print(f"****************************{lives}/6 LIVES LEFT****************************") #PRINTS OUT THE AMOUNT OF LIVES OUT OF 6
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word: #CHECKS IF THE GUESSED LETTER IS CORRECT (check: letter by letter/one by one)
        if letter == guess: #IF GUESSED LETTER IS A LETTER IN THE CHOSEN WORD THEN THE LETTER IS ADDED TO DISPLAY AND APPENDED TO THE LIST correct_letters
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters: #THIS WILL ALLOW ALL OF THE PREVIOUS CORRECT LETTERS TO STILL BE PRINTED OUT AS THE LOOP RESETS DISPLAY WILL ALSO RESET
            display += letter
        else: #IF THE GUESSED LETTER IS NOT IN THE CHOSEN WORD ANOTHER BLANK IS PRINTED (THIS MEANS THAT THE LETTER IN THIS BLANK OR INDEX HAS STILL NOT BEEN GUESSED
            display += "_"

    if guess in guessed_letters: #THIS WILL LET THE USER KNOW IF THE LETTER THEY INPUT HAS ALREADY BEEN GUESSED PREVIOUSLY
        print(f"You have already guessed this letter: {guess}")

    guessed_letters.append(guess)
    print("Word to guess: " + display)

    if guess not in chosen_word: #IF THE USER GUESSED WRONG THIS WILL REDUCE THE LIFE BY 1
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.") 

        if lives == 0: #IF THE LIVES ARE ALL USED THIS WILL LET THE USER KNOW THEY LOSE
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display: #IF THE WORD HAS BEEN COMPLETELY GUESSED THIS WILL LET THE USER KNOW THEY WIN
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
