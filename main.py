
import random
import re
from collections import Counter
from pathlib import Path


def get_integer(prompt, minimum=None, maximum=None):
    """Get a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Enter a number less than or equal to {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def number_guessing_game():
    """Play a random number guessing game."""
    print("\n--- Number Guessing Game ---")
    print("Guess the secret number between 1 and 100!")
    print("You have 7 attempts.")

    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        guess = get_integer(
            f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ",
            1,
            100,
        )
        attempts += 1

        if guess == secret_number:
            points = (max_attempts - attempts + 1) * 10
            print(f"Correct! You guessed the number in {attempts} attempts.")
            print(f"You earned {points} points!")
            return points

        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        print(f"Attempts remaining: {max_attempts - attempts}")

    print(f"Game over! The secret number was {secret_number}.")
    return 0


def word_counter():
    """Read a text file and analyze word frequency."""
    print("\n--- Word Counter & Frequency Analyzer ---")

    filename = input(
        "Enter a text filename (press Enter for sample.txt): "
    ).strip()

    if not filename:
        filename = "sample.txt"

    file_path = Path(filename)

    if not file_path.is_file():
        print("File not found!")
        print("Make sure the text file exists in your project folder.")
        return

    try:
        text = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Could not read the file: {error}")
        return

    # Match words and ignore capitalization.
    words = re.findall(r"\b[\w']+\b", text.lower())
    frequencies = Counter(words)

    print("\n--- Text Analysis Results ---")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(frequencies)}")
    print(f"Total characters: {len(text)}")

    if not words:
        print("The file contains no words.")
        return

    print("\nTop 10 most frequent words:")
    for word, count in frequencies.most_common(10):
        print(f"{word}: {count}")

    # Save the frequency report to a separate file.
    report_path = file_path.with_name("word_report.txt")

    try:
        with report_path.open("w", encoding="utf-8") as report:
            report.write("WORD FREQUENCY REPORT\n")
            report.write(f"File analyzed: {file_path.name}\n")
            report.write(f"Total words: {len(words)}\n")
            report.write(f"Unique words: {len(frequencies)}\n\n")

            for word, count in frequencies.most_common():
                report.write(f"{word}: {count}\n")

        print(f"\nFull report saved to: {report_path}")

    except OSError as error:
        print(f"Could not save the report: {error}")


def main():
    """Display the main menu."""
    total_score = 0

    while True:
        print("\n====================================")
        print(" NUMBER GAME & WORD COUNTER")
        print("====================================")
        print("1. Play Number Guessing Game")
        print("2. Analyze a Text File")
        print("3. View Total Score")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            total_score += number_guessing_game()
            print(f"Your total score: {total_score}")

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print(f"Your total score: {total_score}")

        elif choice == "4":
            print(f"Final score: {total_score}")
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
