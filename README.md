
# 🎮 Number Guessing Game & Word Counter

A beginner-friendly Python project created as part of my internship tasks.

The application combines a number guessing game with a text file word counter and frequency analyzer.


Demo Link: https://number-guessing-word-counter-t6nuokhbmkzmaeb4zs7int.streamlit.app/

## ✨ Features

### Number Guessing Game
- Generates a random number between 1 and 100.
- Allows up to 7 attempts.
- Provides hints when a guess is too high or too low.
- Tracks attempts and awards points.
- Maintains a total score during the session.

### Word Counter
- Reads text files using Python file handling.
- Counts total words and unique words.
- Displays the 10 most frequent words.
- Ignores capitalization when counting.
- Saves a complete frequency report to `word_report.txt`.
- Handles missing files and invalid input.

## 🛠️ Technologies Used

- Python 3
- random module
- collections.Counter
- pathlib
- Regular expressions
- File handling and exception handling

## 📁 Project Structure

```text
number-guessing-word-counter/
├── main.py
├── sample.txt
├── README.md
└── .gitignore
```

The file `word_report.txt` is generated when you analyze a text file.

## 🚀 How to Run

1. Install Python 3 from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## 📖 How to Use

1. Select option 1 to play the guessing game.
2. Select option 2 to analyze a text file.
3. Enter `sample.txt` or the path to another text file.
4. Check the displayed statistics and generated word report.
5. Select option 3 to view your total game score.
6. Select option 4 to exit.

## 🎯 Learning Objectives

- Python loops and conditionals
- Functions and return values
- Random number generation
- Input validation
- Strings and regular expressions
- File reading and writing
- Dictionaries and word frequency analysis
- Exception handling

## 👤 Author

Dipak Mengal

GitHub: https://github.com/Dipakmengal

## 📄 License

This project is available for educational use.
