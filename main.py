import random

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    return(guess in guesses)

def evaluate_guess(guess, word):
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]   # if in right place - color the letter green
        elif guess[i] in word:
            str += "\033[33m" + guess[i]   # if in wrong place, but in word - color the letter yellow
        else:
            str += "\033[0m" + guess[i]     # if is not in word - don't color the letter 
    return str + "\033[0m"

def main():
    answers = load_dictionary("answers.txt")
    guesses = load_dictionary("guesses.txt")

    print("Welcome to the Wordle! \nYou have 6 attempts to guess the 5-letter word.")
    answer = random.choice(answers)

    attempts = 1

    while attempts <= 6:
        guess = input("Type your guess: ").lower()
        if not is_valid_guess(guess, guesses):
            print("Not valid format or word.")
            continue
        if guess == answer:
            print("Congratulations! You guessed the word in " + str(attempts) + " attempt(s)") 
            break
            
        print(str(attempts) + ") " + evaluate_guess(guess, answer))
        attempts+=1
    
    if attempts > 6:
        print("You lost. The secret word was: " + str(answer))

if __name__ == "__main__":
    main()
