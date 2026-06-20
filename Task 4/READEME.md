
TASK 4: SENTIMENT ANALYSIS PROJECT

PROJECT OVERVIEW
This project performs sentiment analysis on a books dataset by generating text-based reviews and classifying them into Positive, Negative, or Neutral sentiment using NLP techniques.

DATASET
- Source: books_dataset.csv
- Columns: Title, Price
- Synthetic "Review" column is generated from book titles for sentiment analysis

OBJECTIVE
- Analyze text data using NLP
- Classify sentiment as Positive, Negative, or Neutral
- Visualize sentiment distribution

APPROACH
- Loaded books dataset
- Created synthetic reviews from book titles
- Applied TextBlob for sentiment detection
- Converted text into polarity scores
- Classified sentiment based on polarity

SENTIMENT RULES
- Polarity > 0  → Positive
- Polarity < 0  → Negative
- Polarity = 0  → Neutral

OUTPUTS
- Sentiment classification for each book
- Sentiment distribution chart (bar graph)
- Saved results in CSV file

TOOLS USED
Python, Pandas, TextBlob, Matplotlib, Seaborn

HOW TO RUN
pip install pandas textblob matplotlib seaborn
python sentiment.py

AUTHOR
Muhammad Zeeshan Sabir
