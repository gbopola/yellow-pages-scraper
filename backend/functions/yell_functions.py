import requests
from bs4 import BeautifulSoup
import re 

# Get single listing url
def extract_single_listing_url_yell(listing):
    business_url = listing.find('a', {'class': 'businessCapsule--title'})
    full_url = "https://www.yell.com" + business_url['href']
    return full_url if business_url else None

# Get company name
def extract_company_name_yell(listing):
    company_name_element = listing.find("h2", {"class": "businessCapsule--name text-h2"})
    return company_name_element.text if company_name_element else None

# Get Full Address
def extract_full_address_yell(listing):
    # Extract the address components
    street_address_tag = listing.find('span', itemprop='streetAddress')
    locality_tag = listing.find('span', itemprop='addressLocality')
    postal_code_tag = listing.find('span', itemprop='postalCode')

    # Check if any of the tags is None
    if street_address_tag is None or locality_tag is None or postal_code_tag is None:
        return None

    street_address = street_address_tag.text.strip()
    locality = locality_tag.text.strip()
    postal_code = postal_code_tag.text.strip()

    # Combine the components to get the full address
    full_address = f"{street_address} {locality}, {postal_code}"
    return full_address


# Get email
def extract_email_yell(listing):
    return "See Website"

# Get phone 
def extract_phone_yell(listing):
    phone_element = listing.find("span", {"class": "business--telephoneNumber"})
    return phone_element.text.replace(" ", "").strip() if phone_element else None

     
# Get website 
def extract_website_yell(listing):
    website_url = listing.find("a", {"class": "btn btn-yellow businessCapsule--ctaItem"})
    return website_url.get("href") if website_url else None

# Scrape website for email
def scrape_website_for_email_yell(website):
    if website:
        resp = requests.get(website)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')

            # Find all email addresses using a regular expression
            email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resp.text)

            return email_addresses

    return None
