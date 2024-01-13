from bs4 import BeautifulSoup
import requests
from functions.yell_functions import extract_company_name_yell, extract_single_listing_url_yell, extract_full_address_yell, extract_email_yell, extract_phone_yell, extract_website_yell

def scrape_page_yell(soup):
    data = []
    allListing = soup.find_all("article", {"class": lambda x: x and "businessCapsule" in x})

    for listing in allListing:
        company_name = extract_company_name_yell(listing)
        full_address = extract_full_address_yell(listing)
        profile_url = extract_single_listing_url_yell(listing)
        email = extract_email_yell(listing)
        phone = extract_phone_yell(listing)
        website = extract_website_yell(listing)

        dataObj = {
            "Company name": company_name,
            "Full Address": full_address,
            "Profile URL": profile_url,
            "Email": email,
            "Phone": phone,
            "Website": website,
        }
        data.append(dataObj)
    return data

def find_next_link_yell(soup):
    next_link = soup.find('a', {"class": 'btn btn-blue btn-fullWidth pagination--next'})
    if next_link:
        return next_link['href']
    else:
        return None

def scrape_all_pages_yell(base_url, api_url, api_key):
    all_data = []
    current_page = 1

    while True:
        url = f"{base_url}&pageNum={current_page}"
        print(f"Scraping page {current_page} - URL: {url}")

        params = {
            'url': url,
            'apikey': api_key,
            'js_render': 'true',
        }
        resp = requests.get(api_url, params=params)
        soup = BeautifulSoup(resp.text, 'html.parser')

        page_data = scrape_page_yell(soup)
        all_data.extend(page_data)

        next_link = find_next_link_yell(soup)
        if next_link:
            current_page += 1
        else:
            break

    return all_data