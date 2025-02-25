import random as r 
from os import system as command   
class HangMan():
    def __init__(self):# initialize the game and sets up the variables
        self.wordList = ['aardvark','baboon','camel','cheetah','dog','elephant',
                         'giraffe','hippopotamus','kangaroo','koala','lion','monkey',
                         'ostrich','panda','python','rabbit','rat','seal','tiger','zebra']
        self.lives = 6
        self.art = ["""
                _______
                |/    
                |      
                |      
                |       
                |      
                |
            ____|___
            ""","""
                _______
                |/      |
                |      (_)
                |      
                |       
                |      
                |
            ____|___
            ""","""
                _______
                |/      |
                |      (_)
                |       |
                |       |
                |       
                |
            ____|___
            ""","""
                _______
                |/      |
                |      (_)
                |      \|
                |       |
                |      
                |
            ____|___
            ""","""
                _______
                |/      |
                |      (_)
                |      \|/
                |       |
                |      
                |
            ____|___
            ""","""
                _______
                |/      |
                |      (_)
                |      \|/
                |       |
                |      / 
                |
            ____|___
            ""","""
                _______
                |/      |
                |     (x_x)
                |      \|/
                |       |
                |      / \\
                |
            ____|___
            """,]
        self.chosenWord = r.choice(self.wordList)
        self.curWord = ['_' ]* len(self.chosenWord)

    def start(self):# starts the game
        command('cls')
        print('Welcome to Hangman')
        print(self.art[0]+'\n')
        print(f'Word: {"".join(self.curWord)}')
        self.playing = True
        while self.playing:
            if self.lives <= 0:
                print('You lost. Better luck next time')
                print(f'The word was: {self.chosenWord}')
                self.playing = False
            guess = input('Guess a letter: ').lower()
            if len(guess) == 1 and guess.isalpha():
                self.checkGuess(guess)
            else:
                print('Invalid input. Please enter a single letter.')
            

    def checkGuess(self,letter):# checks if the letter is in the word and if it is updates the current word
        if(letter in self.chosenWord):
            i=0
            for char in self.chosenWord:
                if char == letter: 
                    self.curWord[i] = letter
                i+= 1
            print('Correct guess!')
            
            if ("".join(self.curWord)) == self.chosenWord:
                print(f'Congratulations! You guessed the word: {self.chosenWord}')
                self.playing = False
        else:
            self.lives -= 1
            print('Incorrect guess.')
            print(self.art[-self.lives-1])
            print(f'lives remaining: {self.lives}')
        print(f'Word: {"".join(self.curWord)}')


def main():
    game = HangMan()
    game.start()

if __name__ == "__main__":
    main()