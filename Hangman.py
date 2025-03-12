import random

def hangman_drawing(nb):
    tab = [
        """
        +-------+
        |
        |
        |
        |
        ==============
        """,
        """
        +-------+
        |  |
        |  O
        |
        |
        ==============
        """,
        """
        +-------+
        |  |
        |  O
        |  |
        |
        ==============
        """,
        """
        +-------+
        |  |
        |  O
        | -|
        |
        ==============
        """,
        """
        +-------+
        |  |
        |  O
        | -|-
        |
        ==============
        """,
        """
        +-------+
        |  |
        |  O
        | -|-
        | |
        ==============
        """,
        """
        +-------+
        |  |
        |  O
        | -|-
        | | |
        ==============
        """
    ]
    return tab[nb]

def load_words(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()
    return words

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman_game():
    words = load_words('words.txt')

    while True:  # Main loop to replay
        word_to_guess = random.choice(words).upper()
        guessed_letters = set()
        remaining_attempts = 6

        print("\nWelcome to the Hangman game!")
        
        while remaining_attempts > 0:
            hidden_word = display_word(word_to_guess, guessed_letters)
            print(f"\nWord to guess: {hidden_word}")
            print(f"Remaining attempts: {remaining_attempts}")
            print(hangman_drawing(6 - remaining_attempts))  

            guessed_letter = input("Guess a letter: ").upper()
            
            if len(guessed_letter) != 1 or not guessed_letter.isalpha():
                print("Please enter a valid single letter.")
                continue
            
            if guessed_letter in guessed_letters:
                print("You have already guessed this letter.")
                continue
            
            guessed_letters.add(guessed_letter)
            
            if guessed_letter in word_to_guess:
                print(f"Good job! The letter {guessed_letter} is in the word.")
            else:
                remaining_attempts -= 1
                print(f"Wrong guess! The letter {guessed_letter} is not in the word.")
            
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nCongratulations, you found the word: {word_to_guess} 🎉")
                break
        
        if remaining_attempts == 0:
            print(f"\nYou lost! The word was: {word_to_guess} 😞")

        replay = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("Thank you for playing! See you soon. 😊")
            break  # Exit the loop and end the program

hangman_game()
