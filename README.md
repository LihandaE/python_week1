# 📊 Web Scraping Project: Books & Jumia Products (Python)
##  Project Overview

This project demonstrates web scraping, data cleaning, currency conversion, and data storage using Python.
It involves scraping product data from:

 * Books to Scrape (static website)

* Jumia Kenya (dynamic e-commerce website)

The project uses requests, BeautifulSoup, pandas, and tabulate, with real-time currency conversion APIs and robust error handling.

### Objectives

- Scrape at least 10–15 products

- Extract product name and price

- Clean and structure raw data

- Convert prices using a free currency API

- Save output to CSV and JSON

- Display results in readable tabular format

- Handle network and scraping errors gracefully

##  Technologies Used

1. Python 3

2. requests

3. beautifulsoup4

4. pandas

5. tabulate

6. re (regular expressions)

7. Currency API: open.er-api.com

### Project Structure
web-scraping-project/
│
├── books_scraper.py
├── jumia_scraper.py
├── books.csv
├── books.json
├── jumia.csv
├── jumia.json
├── requirements.txt
└── README.md

### Environment Setup
1️⃣ Create a Virtual Environment
`python -m venv venv`

2️⃣ Activate the Environment

Windows

`venv\Scripts\activate`


macOS / Linux

`source venv/bin/activate`

3️⃣ Install Dependencies
`pip install requests beautifulsoup4 pandas tabulate`


(Optional)

`pip freeze > requirements.tx`t

## Part 1: Books to Scrape
🔗 Website

https://books.toscrape.com/

### Data Collected

- Book title

- Price in GBP (£)

### Currency Conversion

-GBP → KES using:

https://open.er-api.com/v6/latest/GBP

### Outputs

1. books.csv

2. books.json

### Why Books to Scrape?

- Static HTML

- Scraping-friendly

- Ideal for learning and exams

## Part 2: Jumia Kenya Scraper
### Website

https://www.jumia.co.ke/

### Data Collected

- Product name

- Price in KES

### Currency Conversion

- KES → USD (or any supported currency)

API used:

https://open.er-api.com/v6/latest/KES

### Anti-Bot Considerations

Jumia uses basic bot protection, therefore:

Custom User-Agent headers are used

Scraping is done via search/category pages

Results may vary depending on request frequency

This behavior is normal and expected in real-world scraping.

## Features Implemented

✔ Data scraping with BeautifulSoup
✔ Data cleaning using regex
✔ Currency conversion using live API
✔ CSV and JSON storage
✔ Table display with pandas/tabulate
✔ Network and runtime error handling

 ## Sample Console Output
+---------------------------+-------------+------------+
| Product / Title           | Price_KES   | Price_USD |
+---------------------------+-------------+------------+
| Samsung Galaxy A14        | 14999       | 115.83    |
| Infinix Smart 7           | 10999       | 84.95     |
+---------------------------+-------------+------------+

## Error Handling

The scripts handle:

- Network timeouts

- API failures

- Missing HTML elements

- Empty results

Example:

except requests.exceptions.RequestException as e:
    print("Network error:", e)

## Learning Outcomes

- Practical web scraping

- Real-world data cleaning

- API consumption

- Structured data storage

- Understanding scraping limitations on e-commerce platforms

## Possible Enhancements

- Multi-page scraping

- Proxy rotation

- Retry/backoff logic

- Database storage (SQLite/PostgreSQL)

- Scheduler (cron / task scheduler)


## Author

- Emmanuel Lihanda
- +254 796285410
- Pharmacy & Technology Enthusiast
