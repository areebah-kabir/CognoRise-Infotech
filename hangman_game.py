import random

def hangman():
    words = ["python", "hangman", "programming", "developer", "computer"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    guessed_word = ['_'] * len(word)

    print("Welcome to Hangman!")

    while attempts > 0 and '_' in guessed_word:
        print(f"Word: {' '.join(guessed_word)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            guessed_letters.append(guess)
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f"Wrong guess. {attempts} attempts left.")
    
    if '_' not in guessed_word:
        print(f"Congratulations! You guessed the word: {''.join(guessed_word)}")
    else:
        print(f"Game over. The word was: {word}")

hangman()
