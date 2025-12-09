import random

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    print("")

def evaluate_guess(guess, word):
    print("")

def wordle(guesses, answers):
    print("")

def main():
    answers = load_dictionary("answers.txt")
    guesses = load_dictionary("guesses.txt")

    print(random.choice(answers))
    print(random.choice(guesses))

if __name__ == "__main__":
    main()
