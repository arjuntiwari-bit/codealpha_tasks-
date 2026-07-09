# Hangman Game (Python)

A simple text-based **Hangman Game** built using Python. The player guesses a hidden word one letter at a time. The game ends when the player successfully guesses the word or reaches the maximum number of incorrect guesses.

## Features

* Randomly selects a word from a predefined list of 5 words.
* Player guesses one letter at a time.
* Displays the current progress using underscores (`_`).
* Allows a maximum of **6 incorrect guesses**.
* Prevents duplicate letter guesses.
* Validates user input.
* Simple console-based interface.

## Technologies Used

* Python 3
* `random` module

## Project Structure

```
Hangman-Game/
│
├── hangman.py      # Main Python program
└── README.md       # Project documentation
```

##How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/Hangman-Game.git
```

2. Navigate to the project folder:

```bash
cd Hangman-Game
```

3. Run the program:

```bash
python hangman.py
```

> Make sure Python 3 is installed on your system.

## How to Play

1. The game randomly selects a secret word.
2. Guess one letter at a time.
3. If the letter is correct, it is revealed in the word.
4. If the letter is incorrect, you lose one of your six attempts.
5. Win by guessing the entire word before using all six incorrect guesses.

## Concepts Used

* Python Variables
* Lists
* Strings
* `random` Module
* `while` Loop
* `if-else` Statements
* User Input (`input()`)
* Basic Game Logic

## Sample Output

```
===== HANGMAN GAME =====

Word: _ _ _ _ _ _
Wrong guesses left: 6

Enter a letter: a
Correct!

Word: _ a _ _ _ _
Wrong guesses left: 6

Enter a letter: z
Wrong guess!

Wrong guesses left: 5
```

## Future Improvements

* Difficulty Levels
* Score Tracking
* Hint System
* Multiplayer Mode
* ASCII Hangman Graphics
* Load words from a text file
* GUI version using Tkinter or Pygame

##Author

**Arjun Tiwari**

B.Tech CSE Student

##License

This project is created for learning purposes and is free to use and modify.
