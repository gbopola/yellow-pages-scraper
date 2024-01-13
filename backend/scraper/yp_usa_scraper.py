from bs4 import BeautifulSoup
import requests
from functions.yp_usa_functions import extract_company_name_yp_usa, extract_city_yp_usa, extract_single_listing_url_yp_usa, extract_categories_yp_usa, extract_full_address_yp_usa, extract_email_yp_usa, extract_phone_yp_usa, extract_website_yp_usa, extract_state_yp_usa, extract_zip_yp_usa, extract_social_links_yp_usa, extract_years_in_business_yp_usa

def scrape_page_yp_usa(soup):
    data = []
    # Find all HTML elements with class 'result' (each represents a listing)
    allListing = soup.find_all("div", {"class": "result"})

    for listing in allListing:

        listing_url = extract_single_listing_url_yp_usa(listing)

         # Send a GET request to the specific listing's page and parse the HTML content
        resp = requests.get(listing_url) 
        soup = BeautifulSoup(resp.text, 'html.parser')

        company_name = extract_company_name_yp_usa(soup)
        full_address = extract_full_address_yp_usa(soup)
        profile_url = extract_single_listing_url_yp_usa(soup)
        categories = extract_categories_yp_usa(soup)
        email = extract_email_yp_usa(soup)
        phone = extract_phone_yp_usa(soup)
        website = extract_website_yp_usa(soup)
        instagram = extract_social_links_yp_usa(soup, 'instagram')
        facebook = extract_social_links_yp_usa(soup, 'facebook')
        twitter = extract_social_links_yp_usa(soup, 'twitter')
        years_in_business = extract_years_in_business_yp_usa(soup)
        years_with_yp = ""

        dataObj = {
            "Company name": company_name,
            "Full Address": full_address,
            "Profile URL": profile_url,
            "Categories": categories,
            "Email": email,
            "Phone": phone,
            "Website": website,
            "Instagram": instagram,
            "Facebook": facebook,
            "Twitter": twitter,
            "Years In Business": years_in_business,
        }
        data.append(dataObj)
         
    return data

def find_next_link_yp_usa(soup):
    next_link = soup.find('a', {"class": 'next ajax-page'})
    
    if next_link:
        return next_link['href']
    else:
        return None

def scrape_all_pages_yp_usa(base_url):
    all_data = []
    current_page = 1

    while True:
        url = f"{base_url}&page={current_page}"
        print(f"Scraping page {current_page} - URL: {url}")

        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')

        page_data = scrape_page_yp_usa(soup)
        all_data.extend(page_data)

        next_link = find_next_link_yp_usa(soup)
        if next_link:
            current_page += 1
        else:
            break

    return all_data