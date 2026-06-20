import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===================== LOAD DATASET =====================
file_path = "Task 2/books_dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("=" * 60)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 60)
except FileNotFoundError:
    print("ERROR: File not found. Check your file path.")
    exit()


# ===================== DATA PREVIEW =====================
print(df.head())


# ===================== BASIC INFO =====================
print("\n" + "=" * 60)
print("DATASET SHAPE:", df.shape)

print("\nCOLUMN NAMES:\n", df.columns)

print("\nDATA TYPES:\n", df.dtypes)

print("\nDATASET INFO:")
print(df.info())


# ===================== MISSING VALUES =====================
print("\n" + "=" * 60)
print("MISSING VALUES")
print(df.isnull().sum())


# ===================== DUPLICATES =====================
print("\n" + "=" * 60)
print("DUPLICATE RECORDS:", df.duplicated().sum())


# ===================== FIX ENCODING + CLEAN PRICE =====================

df["Price"] = df["Price"].astype(str)

# Fix broken encoding + remove currency symbols
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)   # fix corrupted pound sign
    .str.replace("£", "", regex=False)    # normal pound sign fallback
    .str.replace(",", "", regex=False)
    .str.strip()
)

# convert to numeric
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# check valid values
print("\nVALID PRICE VALUES:", df["Price"].notna().sum())

# remove bad rows
df = df.dropna(subset=["Price"])

# safety check
if df.empty:
    print("ERROR: Still no valid price data. Check dataset encoding.")
    exit()

# ===================== REMOVE MISSING PRICE ROWS =====================
df = df.dropna(subset=["Price"])


# ===================== STATISTICS =====================
print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print(df.describe())


# ===================== MOST EXPENSIVE / CHEAPEST =====================
most_expensive = df.loc[df["Price"].idxmax()]
cheapest = df.loc[df["Price"].idxmin()]

print("\nMOST EXPENSIVE BOOK:\n", most_expensive)

print("\nCHEAPEST BOOK:\n", cheapest)


# ===================== PRICE METRICS =====================
print("\nAVERAGE PRICE:", round(df["Price"].mean(), 2))
print("MEDIAN PRICE:", df["Price"].median())
print("MAX PRICE:", df["Price"].max())
print("MIN PRICE:", df["Price"].min())


# ===================== TOP / BOTTOM 10 BOOKS =====================
print("\nTOP 10 MOST EXPENSIVE BOOKS")
print(df.sort_values(by="Price", ascending=False).head(10))

print("\nTOP 10 CHEAPEST BOOKS")
print(df.sort_values(by="Price", ascending=True).head(10))


# ===================== VISUALIZATIONS =====================
sns.set_style("whitegrid")

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Boxplot
plt.figure(figsize=(6, 5))
sns.boxplot(y=df["Price"])
plt.title("Book Price Boxplot")
plt.tight_layout()
plt.savefig("price_boxplot.png")
plt.show()

# Top 10 expensive books barplot
top_books = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(data=top_books, x="Price", y="Title")
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("top10_expensive_books.png")
plt.show()


print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)