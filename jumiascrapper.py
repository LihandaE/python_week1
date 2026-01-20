import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import re



JUMIA_URL = "https://www.jumia.co.ke/catalog/?q=phone"
RATE_API = "https://open.er-api.com/v6/latest/KES"
TARGET_CURRENCY = "USD"
PRODUCT_LIMIT = 15

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

print("Starting Jumia product scraper...")

try:
   
    response = requests.get(JUMIA_URL, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    product_cards = soup.select("article.prd")[:PRODUCT_LIMIT]

    products = []

    for product in product_cards:
        name_tag = product.select_one("h3.name")
        price_tag = product.select_one("div.prc")

        if not name_tag or not price_tag:
            continue

        name = name_tag.text.strip()

        price_text = price_tag.text.strip()     
        clean_price = re.sub(r"[^\d]", "", price_text)

        if not clean_price:
            continue

        price_kes = float(clean_price)

        products.append({
            "product": name,
            "price_kes": price_kes
        })

    if len(products) < PRODUCT_LIMIT:
        print(f"Only {len(products)} products scraped (Jumia may limit requests).")

    
    rate_response = requests.get(RATE_API, timeout=10)
    rate_response.raise_for_status()
    rate_data = rate_response.json()

    rate = rate_data["rates"][TARGET_CURRENCY]

   
    for product in products:
        product[f"price_{TARGET_CURRENCY.lower()}"] = round(
            product["price_kes"] * rate, 2
        )

   
    df = pd.DataFrame(products)

    print("\nConverted Prices:\n")
    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

    
    df.to_csv("jumia.csv", index=False)
    df.to_json("jumia.json", orient="records", indent=4)

    print("\nSaved to jumia.csv and jumia.json")

except requests.exceptions.RequestException as e:
    print("[ERROR] Network error:", e)

except Exception as e:
    print("[ERROR] Something went wrong:", e)
