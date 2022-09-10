# Made by TH1RDKEYBLADE
# Imports - BuiltIn
from os import path
from random import choice as ranchoice
from time import sleep 

# Random word script
def random_word(word_list):
    word = ranchoice(word_list).lower()
    # Make sure to make words lowercase
    ignored_words = ["", " ", "-", "_", "i", "am", "and", "that", "them", "want", "because", "be", "me", "to", "by", "the", "of", "my", "you", "do", "is", "or"]

    # Gets a word that isn't boring
    if word in ignored_words:
        random_word(word_list)
    else:
        print(word)

# Main Function
def main():
    # Start
    print("Word randomizer from the Shrek Script.")
    print("--------------------------------------")
    input("Enter to start!")
    print()

    # Opens the script file (must be in same directory as Python file)
    with open(path.join(path.dirname(__file__), 'shrek_transcript.txt'), encoding='utf-8') as f:
        
        all_text = f.read()
        word_list = all_text.split()

        # Prints randomized word every second
        while True:
            random_word(word_list)

            # Edit number below. (in seconds)
            sleep(1)
            
if __name__ == "__main__":
    main()
