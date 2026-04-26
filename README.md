# Quiz Practice App

Quiz app born from spite and token scarcity. Anthropic made me independent, one credit limit at a time.
A Streamlit quiz app for practicing MCQs with weighted question selection based on performance for CSE519, Spring 2026 (or any other course, just update the questions.py with your mirrored dataset)

## Features
- Multiple topics
- Tracks which questions you get wrong and shows them more often
- Progress saved between sessions
- Multi-select support for questions with multiple answers

## Setup
```bash
pip install streamlit
python -m streamlit run app.py
```

## Usage
1. Select a topic from the sidebar
2. Choose number of questions
3. Start the quiz
4. Ace that midterm
5. Show Anthropic who's the boss.

## How it works

- Questions are weighted based on past performance
- Incorrectly answered questions are more likely to reappear
- Progress is stored locally between sessions

## How it looks
<img width="2559" height="916" alt="image" src="https://github.com/user-attachments/assets/0ddd7bc2-9723-44b0-b3cb-ba7d0eae70de" />




