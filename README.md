# Quiz Practice App

> Built out of spite for Anthropic's token limits. When Claude runs out of credits mid-study session, you learn to help yourself.

## What This Is

A Streamlit-based quiz app for practicing MCQs with intelligent question weighting. Got tired of begging Claude for help every time I needed to review material, so I built this instead.

## Features

- **Adaptive Question Selection**: Questions you struggle with appear more frequently
- **Performance Tracking**: Stores your accuracy stats locally between sessions
- **Smart Weighting Algorithm**: 
  - New questions get priority (weight = 3)
  - Struggled questions weighted as `1 + (1 - accuracy) * 4`
- **Multi-Worksheet Support**: Organize questions by topic/worksheet
- **Multiple Question Types**: Single-choice and multi-select MCQs
- **Focused Review**: Only shows incorrect answers at the end (no clutter)
- **Clean Answer Display**: Bullet-pointed formatting for better readability

## How It Works

1. **Question Weighting**: Questions are weighted based on your historical accuracy
2. **Adaptive Sampling**: Lower accuracy = higher weight = more likely to appear
3. **Local Progress**: All stats saved to `progress.json` between sessions
4. **Review Mode**: After completion, review only what you got wrong

No AI required. No token limits. No Drama. Claude can go kick rocks.

## Setup

```bash
# Install dependencies
pip install streamlit

# Run the app
streamlit run final_app.py
```

## Usage

1. Select a worksheet from the sidebar (or choose "All")
2. Choose number of questions (10, 20, 100, or All)
3. Start the quiz
4. Review your mistakes and improve


**Lesson learned**: If you want something done right (and without arbitrary usage limits), build it yourself.

## How the Weighting Works

```python
# New questions
weight = 3

# Previously attempted questions
accuracy = correct_attempts / total_attempts
weight = 1 + (1 - accuracy) * 4

# Example:
# 100% accuracy → weight = 1 (rarely appears)
# 50% accuracy → weight = 3 (moderate frequency)
# 0% accuracy → weight = 5 (appears very frequently)
```

## Tech Stack

- **Python 3.x**: Because it works
- **Streamlit**: Fast prototyping without React nonsense
- **JSON**: Local storage, no database overhead

## How it Looks
<img width="2559" height="928" alt="image" src="https://github.com/user-attachments/assets/fbdfbde7-da5a-4c19-9e13-5c48dedd99d5" />

## Contributing

Feel free to fork and improve. If you add features, cool. If you don't, also cool.

## License

MIT License

