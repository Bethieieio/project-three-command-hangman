from curses.ascii import isalpha
import random
from words import word_list

#fetches random word from words.py and returns it in capital letters
def get_word():
    word = random.choice(word_list)
    return word.upper()


#displaying word for each turn, will run until user guesses word or runs out of tries
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Whoops! You have already guessed this letter! Try again!")
            elif guess not in word:
                print(guess, "is not the word! Try again!")
                tries -= 1
                guessed_letters.append(guess)
            else: 
                print("Great Job!", guess, "is the correct word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                
        elif len(guess) == len(word) and guess.isalpha():
        else:
            print("Woops! Please enter a letter or word! :)")
        print(display_hangman(tries)
        print(word_completion)
        print("/n")