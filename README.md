# Console Hangman

## Introduction
Console hangman is the classic game of hangman but it is played in the console.
The aim is to guess the word in six tries. If the user guesses the word is less than 6 tries, they win the game. If the user does not guess the word, it is game over. The user is then asked if they would like to play again.
Each failed guess more and more features of a stick figure would appear on the gallows until it is complete.

The game can be found [here](https://console-hangman.herokuapp.com/)

## Planning Stage 
### Target Audience 
- This game is for people any age
- English speakers
- English students
- Users who want to kill a little time by completing a word game instead of being on social media.

### User Stories
- As a user, I would like to know how to play the game.
- As a user, I would like to know the answer at the end of the game if i get it incorrect.
- As a user, I would like to know how many letters there are in the word I have to guess.
- As a user, I would like to play the game as many times as I want.

### Site Aims
- To provide a game thay runs smoohtly with no errors
- To provide a game that has clear instructions for the user to understand.
- To encourage people to spend less time on social media and to train their brain more.
- To provide quick but challenging gaming.

### Page Layout
The game is layed out on a mock terminal on a webpage deployed on [Heroku](https://www.heroku.com/) and is connected through [GitHub](https://github.com)
The user types in their inputs in the console and presses enter to submit them. 

## Float Chart
![image](assets/images/flow-diagram-2.png)
## Game Walkthrough

- The start image title is from the Ascii graffiti generator [PatorJK](http://patorjk.com/software/taag/#p=testall&f=Stop&t=Console%20Hangman). I made sure the style was readable as some types of graffiti are difficult to read.
![image](assets/images/start.png)

- The games asks the user to select a difficulty. The user selects the difficulty by entering E (Easy), M (Medium) or H (Hard).
The difficulties have the same words to guess but with a different number of tries, 8, 6, 4 respectively.
Our user picked easy, because she is not very good at playing hangman...
If the user enters a letter that is not a difficulty, the game tell them this.
![image](assets/images/select_difficulty.png)
![image](assets/images/wrong_difficulty.png)

- The player starts by picking the letter 'A'.
When she enters the letter, the game tells her that 'A' is in the word and adds it to the mystery word.
It also tells the user that in this word, there are seven letters.
![image](assets/images/first-correct-answer.png)

- The player then inputs her next chosen letter, 'E'. It's not in the word.
The game tells them this and adds the first part on the hangman's gallows, that also change colour for visual effect and to make it obvious that something has been added to it. The user has lost a try.
![image](assets/images/first-wrong-answer.png)

- The player then guesses two correct answers, 'I' and 'S'. These are added to the word and no tries are lost.
![image](assets/images/second-correct-answer.png)
![image](assets/images/third-correct-answer.png)

- The player got the next 3 letters incorrect . The letters 'P', 'B' and 'L'are not in the word and three more tries are lost, adding more parts to the hangman and changing it's colour each time.
![image](assets/images/secoond-wrong-answer.png)
![image](assets/images/third-wrong-answer.png)
![image](assets/images/forth-wrong-answer.png)


- The user tried entering 'S' again, but forgot that they already inputed in this letter. They player does not lose a life, but the game tells them that they have repeated the letter.
![image](assets/images/repeated-letter.png)

- The user guessed the letter 'W but it was wrong! They are running out of lives? Will they win?
![image](assets/images/fifth-wrong-letter.png)

- The player has the option to cheat! But it costs one try each time they do this. To enter cheat as a word, a random unchosen letter appears in the mystery word and the a try is taken. The game tells the player that they are a cheater! 
![image](assets/images/cheater.png)

- The player adds the letter 'N' it is correct.
![image](assets/images/fifth-correct-letter.png)

- The player, now panicking she has two wrong tries left, uses all her brain to guess the mystery word from the shown letters! She thought she was so clever guessing the word 'basking' (forgetting she was told earlier that the letter 'B' was not in the word but we will let her off.. she was on her work lunch break enjoying a large vanilla latte). It obviously was not the correct word, so she lost a try. She has only one wrong answer left before game over. If she was silly enough to enter the same word again, she would not have lost a life. The game would have told her she already guessed that word.
![image](assets/images/wrong-word.png)

- The player guessed the word 'masking'. It was the correct word!! (Wahoo!) The game shows the completed word and tells the player well done in a graffiti font. The game asks if the player would like to play again. The player can enter 'Y' for yes and the game starts all over again with aanother random word and 'N' for No which ends the game.
![image](assets/images/correct-word.png)
![image](assets/images/game-won.png)

- The user played the game again. But this time, they did not manage to guess the word and ran out of tries.
All of the stick figure's limbs were added and a bloody graffiti text appears that says 'Game Over'. The game also tells the user what the mystery word was, then asks the user if they wish to play again.
![image](assets/images/game-over.png)

## Testing
### Pep8 Testing
- I tested my code using a package called [Pycodestyle](https://pypi.org/project/pycodestyle/) as [pep8online](http://pep8online.com/) was down. I only had a few minor things that needed sorting out.

- I had some lines were too long. The validator thought my lines of Python were too long. To fix this, I just added the excess code to another line.
![image](assets/images/line-too-long.png)
![image](assets/images/line-too-long-fix.png)

- Next, I saw that some red squiggles under a function. It was not spaced properly and it had be clear of the code above it by two spaces. I corrected this.
![image](assets/images/function-error.png)
![image](assets/images/function-error-fix.png)

### Manual Testing
- Implemention: At the start of the game, the user selects the difficulty by entering 'E' for easy, 'M' for medium or 'H' for Hard. These three letters should be the only letters that allows the user to carry on with the game has it tells the game how many tries the user would like.
- Test: To test this, I input the 'E', 'M' and 'H' individually. I then tried to input other letters and words. I then added numbers and puncuation marks to see if it stopped the user from continuting.
![image](assets/images/difficulty-test.png)
![image](assets/images/mayonaise.jpg)
- Result: Adding anything but 'E', 'M' or 'H' did not continue the game. It tells the user that whatever they inputted is not a difficulty.
- Verdict: Only the letters 'E', 'M' or 'H' selected the difficulty and continued with the game. So it was a success.

### Bugs
The only issue I had with my game was that the graffiti title was too long for the game area, so half of it was hidden.
To solve this, I moved the word 'Hangman' it was below the word 'Console'.

## Techologies 
### Languages
- [Python](https://www.python.org/): Everythong for this project is in Python.
- [Markdown](https://www.markdownguide.org/basic-syntax/): This read me is in Markdown

### Developer Environment
- [GitHub](https://github.com/): Code hosting platform 
- [Visual Studio Code](https://code.visualstudio.com/): This project was written in VS Code
- [Heroku](heroku.com): Cloud platform, deploys the app

### Packages
- [PypiColored](https://pypi.org/project/colored/) To create the colours for the gallows and graffiti text 
- [PypiPep8](https://pypi.org/project/pep8/) To test the Python code I wrote for any errors / imperfections.

### Other
- [Graffiti](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) For the 'Well Done' and 'Game Over' text, I used Patorjk.
## Deployment
- I had commited and pushed everything required for the game to work to GitHub.
- I then went to [Heroku]((heroku.com)) and created an account.
- I click on 'New' on the top left of the site and clicked 'Create New App'.
- I chose the Europe region and created a name for the app. I chose Console-Hangman
- I went to the settings page and sorted out Buildpacks for everythong to work. I inouted the Python and Node buildpacks like so:
![image](assets/images/buildpack.png)
- I also input a config var for PORT = 8000.
![image](assets/images/buildpack.png) 
- I clicked on the deploy page and link my GitHub repository with the Heroku app.
- I scrolled tpo the bottom of the page and deployed the branch, looking at all the steps the computer went through to see iof any errors occured.
- I then enabled automatic deploys so every time edited the code and pushed to GitHub, Heroku redeployed the updates automatically.
- I then opened the game on Heroku to check for any errors that may have occured.

## Credits and References
- I watched this YouTube video from a channel called [Kite](https://www.youtube.com/watch?v=m4nEnsavl6w) to help me get the basics of what I needed for the game of hangman to work, pausing it every so often and printing things to understand more of what what happening and why.
- [Hangman Steps and Words](https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py) I used Kites repository to use their hangman steps because I know nothing about making a drawing out of symbols and adapted it to make it look better more like a stick figure. I also used their words as I felt they had a good mixture of easy, difficult, long and short words.
- Rich my mentor. He is cool.
- My partner [Ashleigh](https://github.com/bashleigh) for putting up with me and doing her very best to answer all my questions.