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

    def run_game(self):
        """run the game"""
        self.choose_the_word()
        while True:
            print("hi")
            break

    def choose_the_word(self):
        word_list = []
        with open(words) as f:
            for line in f:
                word_list.append(line)
        the_word = random.choice(word_list)
        print(the_word)
if __name__ == '__main__': 
    pd = Pyrdle()
    pd.run_game()

