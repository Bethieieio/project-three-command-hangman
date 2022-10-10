from cgitb import reset
from curses.ascii import isalpha
from doctest import COMPARISON_FLAGS
import random
from words import word_list
import colored


def get_word():
    """
    Fetches random word from words.py and returns it in capital letters
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    displaying word for each turn, will run until
    user guesses word or runs out of tries
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 8
    print(f"""{colored.fg(124)} Welcome to
    __   ___   ____   _____  ___   _        ___
   /  ] /   \ |    \ / ___/ /   \ | |      /  _]
  /  / |     ||  _  (   \_ |     || |     /  [_
 /  /  |  O  ||  |  |\__  ||  O  || |___ |    _]
/   \_ |     ||  |  |/  \ ||     ||     ||   [_
\     ||     ||  |  |\    ||     ||     ||     |
 \____| \___/ |__|__| \___| \___/ |_____||_____|
 __ __   ____  ____    ____  ___ ___   ____  ____
|  |  | /    ||    \  /    ||   |   | /    ||    \\
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|

{colored.attr('reset')}""")

    difficulty_selected = False
    while difficulty_selected is False:
        difficulty = input("""Please select difficulty:
E = Easy, M = Medium, H = Hard: """).upper()
        if difficulty == "E":
            tries = 8
            print("You chose Easy difficulty. You have ", tries, "tries.")
            difficulty_selected = True
        elif difficulty == "M":
            tries = 6
            print("You chose Medium difficulty. You have ", tries, "tries")
            difficulty_selected = True
        elif difficulty == "H":
            tries = 4
            print("You chose Hard difficulty have ", tries, "tries")
            difficulty_selected = True
        else:
            print(difficulty, "is not a difficulty")

    print(display_hangman(tries))
    print(word_completion)
    print(" \n ")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Whoops! You have already guessed this letter")
            elif guess not in word:
                print(guess, "is not in the word! Try again!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Great Job!", guess, "is a correct letter!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word)
                    if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif guess.isalpha():
            if guess in guessed_words:
                print("Oh Dear! You have already guessed the word", guess)
            elif guess == "CHEAT":
                print("YOU'RE CHEATER! SAY GOODBYE TO A TRY!")
                cheat_letters = []
                for letter in list(word):
                    if letter not in guessed_letters:
                        cheat_letters.append(letter)
                random_letter = random.choice(cheat_letters)

                guessed_letters.append(random_letter)
                word_as_list = list(word_completion)
                indices = [
                    i for i, letter in enumerate(word)
                    if letter == random_letter]
                for index in indices:
                    word_as_list[index] = random_letter
                word_completion = "".join(word_as_list)
                tries -= 1
                if "_" not in word_completion:
                    guessed = True

            elif guess != word:
                print(guess, " is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Woops! Please enter a letter or word! :)")
        print(display_hangman(tries))
        print(word_completion)
        print(f"There are {len(word)} letters in this word!")
        print("\n")
    if guessed:
        print(f"""{colored.fg(6)}Wahoo! You guessed the word! You Win!

██     ██ ███████ ██      ██
██     ██ ██      ██      ██
██  █  ██ █████   ██      ██
██ ███ ██ ██      ██      ██
 ███ ███  ███████ ███████ ███████


██████   ██████  ███    ██ ███████ ██
██   ██ ██    ██ ████   ██ ██      ██
██   ██ ██    ██ ██ ██  ██ █████   ██
██   ██ ██    ██ ██  ██ ██ ██
██████   ██████  ██   ████ ███████ ██

""")
    else:
        print(
            "I'm sorry, you ran our of tries. The correct word was " + word +
            "\n Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                f"""{colored.bg(15)}{colored.fg(88)}

                    --------
                    |      |
                    |      O
                    |     \|/
                    |      |
                    |     / \.
                    -
    ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███
   ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
  ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
  ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄
  ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
   ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
   ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░
    ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░
                                                      ░


                {colored.attr('reset')}""",
                # head, torso, both arms, and one leg
                f"""{colored.fg(213)}
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                {colored.attr('reset')}""",
                # head, torso, and both arms
                f"""{colored.fg(91)}
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                {colored.attr('reset')}""",
                # head, torso, and one arm
                f"""{colored.fg(4)}
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                {colored.attr('reset')}""",
                # head, neck and torso
                f"""{colored.fg(80)}
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                {colored.attr('reset')}""",
                # head and neck
                f"""{colored.fg(2)}
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   |
                   -
                {colored.attr('reset')}""",
                # head
                f"""{colored.fg(226)}
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                {colored.attr('reset')}""",
                # rope added
                f"""{colored.fg(202)}
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                {colored.attr('reset')}""",
                # initial empty state
                f"""{colored.fg(210)}
                   --------
                   |
                   |
                   |
                   |
                   |
                   -
                {colored.attr('reset')}""",
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? Y/N ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
