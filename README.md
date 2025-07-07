# Web-Scraping

This repository contains a basic Python script designed to scrape quotes from a publicly accessible website, quotes.toscrape.com. It demonstrates fundamental web scraping concepts using the requests and BeautifulSoup libraries.

Project Structure
scrape_quotes.py: The main Python script that handles fetching the web page and extracting quotes.

scrape_quotes.py - Code Overview
The scrape_quotes.py script is a straightforward implementation for extracting specific content from a web page.

**Key Components:**
Import Libraries:

requests: Used to make HTTP requests to download the web page content.

BeautifulSoup: A library for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping.

**Define Target URL:**

url: Specifies the target website (https://quotes.toscrape.com) from which the quotes will be scraped.

**Fetch Web Page Content:**

response = requests.get(url): Sends an HTTP GET request to the specified URL and stores the server's response.

response.text: Accesses the HTML content of the web page as a string.

**Parse HTML with BeautifulSoup:**

soup = BeautifulSoup(response.text, 'html.parser'): Initializes a BeautifulSoup object, parsing the HTML content obtained from the response. 'html.parser' is specified as the parser to use.

**Extract Quotes:**

quotes = soup.find_all('span', class_='text'): This is the core scraping logic. It uses BeautifulSoup's find_all method to locate all <span> HTML tags that have a class attribute set to 'text'. On quotes.toscrape.com, these <span> elements contain the actual quote text.

**Print Extracted Quotes:**

A for loop iterates through each quote element found.

print(quote.text): Extracts the visible text content from each <span> element and prints it to the console.

**Dependencies**
The scrape_quotes.py script relies on the following external Python libraries:

requests: For making HTTP requests.

BeautifulSoup4 (bs4): For parsing HTML and extracting data.

You can install them using pip:

pip install requests beautifulsoup4

**How to Run**
Save the script: Save the provided code as scrape_quotes.py (or any other .py file name you prefer).

Install Dependencies: Ensure you have the required libraries installed (as shown in the Dependencies section above).

Execute: Run the script from your terminal:

python scrape_quotes.py

The script will then fetch the quotes from quotes.toscrape.com and print them directly to your console.

**OUTPUT**

![WhatsApp Image 2025-07-05 at 20 12 22_966c9f46](https://github.com/user-attachments/assets/f81a29f5-8bb2-4059-9604-45dac356683f)
![WhatsApp Image 2025-07-05 at 20 12 22_ce233d05](https://github.com/user-attachments/assets/5c19b13e-d90e-48b2-8533-98633ce03f85)
![WhatsApp Image 2025-07-05 at 20 12 22_a2f24e97](https://github.com/user-attachments/assets/6a493d75-2f85-4936-a489-d58bc90648e1)

