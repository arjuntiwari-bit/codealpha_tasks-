import random

words = ["python", "apple", "cricket", "computer", "college"]
word = random.choice(words)

guessed_word = ["_"] * len(word)
guessed_letters = []

wrong_guesses = 0
max_wrong = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")

while wrong_guesses < max_wrong and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Wrong guesses left:", max_wrong - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")

        # Reveal all occurrences
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1


if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The correct word was:", word)