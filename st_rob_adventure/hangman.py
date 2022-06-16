# my code
import random
import os
def run():
    result_0 = """
                    ======[]
                           |
                           |
                           |
                           |
                           |
                           |
                           |
                   ---------
                            """
    result_1 = """
                    ======[]
                    |      |
                    O      |
                           |
                           |
                           |
                           |
                           |
                   ---------
                            """
    result_2 = """
                    ======[]
                    |      |
                    O      |
                    |      |
                    |      |
                           |
                           |
                           |
                   ---------
                            """
    result_3 = """
                    ======[]
                    |      |
                    O      |
                   /|      |
                    |      |
                           |
                           |
                           |
                   ---------
                            """
    result_4 = """
                    ======[]
                    |      |
                    O      |
                   /|\     |
                    |      |
                           |
                           |
                           |
                   ---------
                            """
    result_5 = """
                    ======[]
                    |      |
                    O      |
                   /|\     |
                    |      |
                   /       |
                           |
                           |
                   ---------
                            """
    word_bank = ["baby", "salmon", "wood", "book", "create", "hello", "alias", "cake", "green", "duck", "dog", "savour", "clue", "reap", "remember", "leap", "steak", "reading", "flower"]
    word = word_bank[random.randrange(len(word_bank))]
    word_split = []
    wrong_guesses = 0
    guessing = []
    for i in range(len(word)):
        guessing.append("_")
    letters_guessed = []
    for letter in word:
        word_split.append(letter)
    while wrong_guesses < 6:
        os.system("cls")
        print("Your Word: ", end="")
        for i in range(len(word)):
            print(guessing[i], end=" ")
        print()
        if wrong_guesses == 0:
            print(result_0)
        elif wrong_guesses == 1:
            print(result_1)
        elif wrong_guesses == 2:
            print(result_2)
        elif wrong_guesses == 3:
            print(result_3)
        elif wrong_guesses == 4:
            print(result_4)
        elif wrong_guesses == 5:
            print(result_5)
        if guessing == word_split:
            print("You guessed the word! The hangman survives and you will too!")
            return True
        guess = input("Guess a Letter: ").lower()
        if len(guess) > 1:
            print("You must only guess ONE letter.")
            input()
            continue
        if guess not in "abcdefghijklmnopqrstuvwxyz":
            print("You must only guess LETTERS.")
            input()
            continue
        if guess == "":
            print("Are you playing or not?? Guess a letter already!")
            input()
            continue
        if guess in letters_guessed:
            print(f"You already guessed {guess} before.")
            input()
            continue
        letters_guessed.append(guess)
        for i, letter in enumerate(word_split):
            if letter == guess:
                guessing[i] = guess
        if guess not in word_split:
            wrong_guesses += 1
    print(f"You did not guess the word, which was {word}!")
    print("""
             ======[]
             |      |
             O      |
            /|\     |
             |      |
            / \     |
                    |
                    |
            ---------
                            """)
    return False

if __name__ == "__main__":
    win = run()
