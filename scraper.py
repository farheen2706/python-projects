import re
import requests
from bs4 import BeautifulSoup

# Regular expression patterns for email and phone numbers
EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_REGEX = r'\+?\d{1,4}?[-.\s]?\(?\d{2,4}?\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}'

def extract_data_from_website(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the website's content
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        # Extract emails and phone numbers using regex
        emails = re.findall(EMAIL_REGEX, text)
        phone_numbers = re.findall(PHONE_REGEX, text)

        # Remove duplicates by converting to sets
        emails = list(set(emails))
        phone_numbers = list(set(phone_numbers))

        return emails, phone_numbers

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return [], []

# Test the function with a sample website
url = input("Enter the website URL: ").strip()
emails, phones = extract_data_from_website(url)

print("\nExtracted Emails:")
for email in emails:
    print(email)

print("\nExtracted Phone Numbers:")
for phone in phones:
    print(phone)
