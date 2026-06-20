import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 11):
    if page == 1:
        url= "https://books.toscrape.com/"
    else:
        url= f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping Page {page}")
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to open Page {page}")
        continue

    soup=BeautifulSoup(response.text, "html.parser")
    books=soup.find_all("article", class_="product_pod")

    for book in books:
        title=book.h3.a["title"]
        price=book.find("p", class_="price_color").text

        data.append({
            "Title": title,
            "Price": price
        })


df = pd.DataFrame(data)
df.to_csv("books_dataset.csv",index=False)

print("\n=================================")
print("Scraping Completed Successfully!")
print(f"Total Books Scraped : {len(df)}")
print("Dataset Saved as books_dataset.csv")
print("=================================")
