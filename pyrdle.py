import random
words = 'words.txt'

class Pydrle:
    """Run the game pydrle, where the user must guess the five letter secret word"""
    
    def __init__(self):
        """init the game, create the word"""
        word_list = []
        with open(words) as f:
            for line in f:
                word_list.append(line)
        the_word = random.choice(word_list)
        print(the_word)
Pydrle()
