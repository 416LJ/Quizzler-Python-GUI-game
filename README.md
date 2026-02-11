# Quizzler App

Quizzler is a graphical user interface (GUI) quiz application built with Python and Tkinter. It fetches trivia questions from the [Open Trivia Database](https://opentdb.com/) and provides an interactive way to test your knowledge.

## Features

- **Dynamic Question Fetching**: Automatically pulls 20 random "True/False" distinct questions from the Open Trivia Database API.
- **Graphical Interface**: Clean and user-friendly GUI built using Tkinter.
- **Instant Feedback**: Visual cues (green for correct, red for incorrect) immediately after answering.
- **Score Tracking**: Keeps track of your score as you progress through the quiz.
- **HTML Entity Handling**: Correctly decodes HTML entities in question text (e.g., `&quot;` becomes `"`).

## Requirements

- Python 3.x
- `requests` library

## Installation

1.  Clone the repository or download the source code.
2.  Install the required Python packages:

    ```bash
    pip install requests
    ```

3.  Ensure you have the `images` folder with `true.png` and `false.png` in the same directory as the scripts.

## Usage

Run the main application script:

```bash
python main.py
```

The application window will open, displaying a question.

- Click the **Green Checkmark** button if you think the answer is _True_.
- Click the **Red Cross** button if you think the answer is _False_.

The interface will flash green for a correct answer and red for a wrong one, then automatically proceed to the next question.

## Project Structure

- `main.py`: The entry point of the application. Orchestrates the flow between data, the quiz model, and the UI.
- `ui.py`: Handles the Tkinter GUI setup, event handling, and visual updates.
- `quiz_brain.py`: Contains the `QuizBrain` class, which manages the quiz logic (score, question progression, answer checking).
- `data.py`: Fetches question data from the Open Trivia Database API.
- `question_model.py`: Defines the `Question` class to structure question data.
- `images/`: Directory containing the assets for the UI buttons (`true.png` and `false.png`).

## Configuration

You can modify `data.py` to change the quiz parameters (e.g., number of questions, difficulty, category):

```python
parameters = {
    "amount": 20,
    "difficulty": "hard",
    "type": "boolean",
}
```
