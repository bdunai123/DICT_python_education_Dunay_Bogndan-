import random

def choose_word():
    words = ['python', 'java', 'javascript', 'php']
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    displayed_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '-'
    return displayed_word

def hangman():
    while True:
        print("HANGMAN")
        print('Type "play" to play the game, "exit" to quit: >', end=" ")
        user_input = input()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "play":
            play_game()
        else:
            print("Invalid input. Please enter 'play' or 'exit'.")

def play_game():
    secret_word = choose_word()
    guessed_letters = set()
    lives = 8

    while lives > 0:
        current_display = display_word(secret_word, guessed_letters)
        print(current_display)
        print("Input a letter: >", end=" ")
        guess = input()

        if not guess.isalpha() or not guess.islower() or len(guess) != 1:
            print("Please enter a lowercase English letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            current_display = display_word(secret_word, guessed_letters)
            print(current_display)

            if '-' not in current_display:
                print(f"You guessed the word {secret_word}!\nYou survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            lives -= 1

        print("Lives left:", lives)

    if lives == 0:
        print(f"You ran out of lives. The word was: {secret_word}")
        print("Thanks for playing!")

if __name__ == "__main__":
    hangman()
