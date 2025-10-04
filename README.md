# Bablu's Quiz App

Welcome to **Bablu's Quiz App**! 🎉  
This is a Python-based quiz game where users can select categories and difficulty levels and test their knowledge with fun multiple-choice questions.

---

## Features

- Multiple categories to choose from:
  - Computers
  - Gadgets
  - Video Games
  - Films
  - Science & Nature
  - General Knowledge
  - Politics
  - Maths
  - Sports
  - Books
- Three difficulty levels:
  - Easy
  - Medium
  - Hard
- Randomized options for each question.
- Automatic scoring after 10 questions.
- Proper input validation to prevent errors.
- Handles HTML special characters in questions and answers.

---

## How to Run

### Prerequisites
- Python 3.x installed
- Required Python libraries:
  ```bash
  pip install requests
  ```

### Running the Quiz
1. Clone this repository:
   ```bash
   git clone https://github.com/Bablu2010/Bablu-s-Quiz-App
   ```
2. Navigate to the project folder:
   ```bash
   cd "Quiz App"
   ```
3. Run the quiz:
   ```bash
   python quiz.py
   ```
4. Follow on-screen instructions to select a category, difficulty, and answer questions.

---

## How to Build a Standalone App (Optional)
If you want to share this quiz as a single executable file (.exe) for Windows:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Generate the exe:
   ```bash
   pyinstaller --onefile --icon=quiz_icon.ico quiz.py
   ```
3. The exe will appear in the `dist` folder.

---

## Screenshot

*(Optional: add a screenshot of the quiz here)*

---

## License
This project is for learning and personal use. Feel free to share, but please give credit if you use the code.

---

Made with ❤️ by Bablu
