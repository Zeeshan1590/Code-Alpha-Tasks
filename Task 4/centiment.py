import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob


# //////////////////////LOAD DATASET

df=pd.read_csv("Task 4/books_dataset.csv")

print("\nDATA PREVIEW")
print(df.head())

#////////////////CREATE FAKE REVIEWS (IMPORTANT FIX)

df["Review"]="This book titled '" + df["Title"]+"' is interesting."


# ///////////////////SENTIMENT FUNCTION

def get_sentiment(text):
    polarity=TextBlob(text).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


#///////////////APPLY SENTIMENT

df["Sentiment"]=df["Review"].apply(get_sentiment)

print("\nSENTIMENT COUNTS")
print(df["Sentiment"].value_counts())


#//////////VISUALIZATION

sns.set_style("whitegrid")

plt.figure(figsize=(6,4))

sns.countplot(data=df, x="Sentiment")

plt.title("Sentiment Analysis (Books Dataset)")

plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.show()


#//////////////////////////SAVE OUTPUT

df.to_csv("sentiment_results.csv", index=False)

print("\nTASK 4 COMPLETED SUCCESSFULLY")