import random
words = 'words.txt'

class Pyrdle:
    """Run the game pydrle, where the user must guess the five letter secret word"""
    
    def __init__(self):
        """init the game, give instructions for user inputs"""
        print("Hello, and welcome to pyrdle! This is a coding excercise based on wordle.")
        print("The rules are simple, you will be prompted for a guess, each guess is a word with five letters")
        print("You will then get an indicator if each letter from your guess is in the secret word")
        print("you will also get an indicator if the letter is in the same location")
        self.word_list = []
        self.last_guess = ''
        self.the_word= ''

    def run_game(self):
        """run the game"""
        self.choose_the_word()
        while True:
            self.user_guess()
            print(self.last_guess)
            break
    def user_guess(self):
        """takes user input for guess, makes sure it is a word"""
        guess = input("Type your guess, it must be a five letter word: ")
        guess = guess.lower()
        if guess.lower() in self.word_list:
            self.last_guess = guess
        else:
            print("That guess won't work!")
            self.user_guess()

    def choose_the_word(self):
        with open(words) as f:
            for line in f:
                stripped_line = line.strip("\n")
                self.word_list.append(stripped_line)
        self.the_word = random.choice(self.word_list)
        print(self.the_word)
if __name__ == '__main__': 
    pd = Pyrdle()
    pd.run_game()

