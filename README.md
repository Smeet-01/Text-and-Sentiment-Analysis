# Text and Sentiment Analysis

A Python toolkit for analyzing text polarity, subjectivity, word complexity, average syllable count, and the Gunning Fog Index.

## Features
- **Polarity & Subjectivity Scores** using customizable positive/negative word lists (`List_of_words.py`).
- **Readability & Complexity Metrics** (`Metrics_for_Analysis.py`):
  - Average sentence length
  - Percentage of complex words (3+ syllables)
  - Average syllable count
  - Gunning Fog Index (GFI)

## Usage
```python
from List_of_words import Words
from Metrics_for_Analysis import Metrics

m = Metrics("Your sample text goes here.")
pos = m.positivity_score(Words.positive())
neg = m.negativity_score(Words.negative())
print("Polarity:", m.polarity_score(pos, neg))
print("GFI:", m.GFI(m.text_complexity()))
```

## Tests
```bash
python -m unittest discover -s tests -v
```
