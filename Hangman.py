import random

# Function to draw the hangman state
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

# Load words from a file
def load_words(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()
    return words

# Function to display the hidden word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Function to manage the hangman game
def hangman_game():
    words = load_words('words.txt')

    while True:  # Main loop to replay
        word_to_guess = random.choice(words).upper()  # Choose a random word
        guessed_letters = set()
        remaining_attempts = 6

        print("\nWelcome to the Hangman game!")
        
        while remaining_attempts > 0:
            # Display the word and remaining attempts
            hidden_word = display_word(word_to_guess, guessed_letters)
            print(f"\nWord to guess: {hidden_word}")
            print(f"Remaining attempts: {remaining_attempts}")
            print(hangman_drawing(6 - remaining_attempts))  

            # Ask for a letter
            guessed_letter = input("Guess a letter: ").upper()
            
            # Check if the input is valid
            if len(guessed_letter) != 1 or not guessed_letter.isalpha():
                print("Please enter a valid single letter.")
                continue
            
            # Check if the letter has already been guessed
            if guessed_letter in guessed_letters:
                print("You have already guessed this letter.")
                continue
            
            # Add the letter to the guessed letters
            guessed_letters.add(guessed_letter)
            
            # Check if the letter is in the word
            if guessed_letter in word_to_guess:
                print(f"Good job! The letter {guessed_letter} is in the word.")
            else:
                remaining_attempts -= 1
                print(f"Wrong guess! The letter {guessed_letter} is not in the word.")
            
            # Check if the player has won
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nCongratulations, you found the word: {word_to_guess} 🎉")
                break
        
        # If attempts are exhausted, show a losing message
        if remaining_attempts == 0:
            print(f"\nYou lost! The word was: {word_to_guess} 😞")

        # Ask if the player wants to play again
        replay = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("Thank you for playing! See you soon. 😊")
            break  # Exit the loop and end the program

# Start the game
hangman_game()
