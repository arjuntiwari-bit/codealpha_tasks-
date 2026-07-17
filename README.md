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


# 📈 Stock Portfolio Tracker

A beginner-friendly Python application that helps users calculate the total investment value of their stock portfolio using predefined stock prices. The program accepts stock symbols and quantities from the user, calculates the total investment, displays a portfolio summary, and saves the results to a text file.

This project was developed as part of my **CodeAlpha Python Programming Internship**.

---

## 🚀 Features

* 📊 Track investments in multiple stocks
* 💹 Calculate the total investment value
* 📝 Uses a predefined stock price dictionary
* 💾 Saves the portfolio summary to a `portfolio.txt` file
* 🖥️ Easy-to-use command-line interface
* 🐍 Beginner-friendly Python implementation

---

## 🛠️ Built With

* Python 3
* Dictionaries
* Loops
* Conditional Statements
* User Input
* Arithmetic Operations
* File Handling

---

## 📂 Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_portfolio_tracker.py
├── portfolio.txt
└── README.md
```

---

## 📌 Predefined Stock Prices

| Stock Symbol | Company                   | Price (₹) |
| ------------ | ------------------------- | --------: |
| TCS          | Tata Consultancy Services |      2182 |
| REL          | Reliance Industries       |      1297 |
| VEDL         | Vedanta Ltd.              |       270 |
| INFY         | Infosys Ltd.              |      1102 |
| JINDALSTEL   | Jindal Steel & Power      |      1029 |

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Stock-Portfolio-Tracker.git
```

### 2. Navigate to the Project Folder

```bash
cd Stock-Portfolio-Tracker
```

### 3. Run the Program

```bash
python stock_portfolio_tracker.py
```

---

## 💻 Sample Output

```text
Available Stocks:
TCS : ₹2182
REL : ₹1297
VEDL : ₹270
INFY : ₹1102
JINDALSTEL : ₹1029

Enter the number of stocks you want to buy: 2

Enter stock symbol: TCS
Enter quantity of TCS: 5

Enter stock symbol: INFY
Enter quantity of INFY: 3

----- Portfolio Summary -----

TCS: 5 shares × ₹2182 = ₹10910
INFY: 3 shares × ₹1102 = ₹3306

Total Investment Value = ₹14216

Portfolio saved successfully in 'portfolio.txt'
```

---

## 📁 Output File (`portfolio.txt`)

```text
Stock Portfolio Summary
-----------------------
TCS: 5 shares = ₹10910
INFY: 3 shares = ₹3306

Total Investment Value = ₹14216
```

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Work with Python dictionaries
* Accept and validate user input
* Use loops and conditional statements
* Perform arithmetic calculations
* Read from and write to text files
* Build a simple command-line application

---

## 🔮 Future Improvements

* 📡 Fetch live stock prices using financial APIs
* 📊 Export portfolio data to CSV or Excel
* 💹 Calculate profit and loss
* 🖥️ Develop a graphical user interface (GUI)
* 🗄️ Store portfolio data in a database
* 🌐 Support additional Indian and international stocks

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📜 License

This project is licensed for educational and learning purposes.

---

## 👨‍💻 Author

**Arjun Tiwari**

* 🎓 B.Tech Computer Science & Engineering Student
* 🐍 Python Developer
* 🤖 AI & Machine Learning Enthusiast


