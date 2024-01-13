# Get fake browser headers from ScrapeOps
# def get_fake_browser_headers(requests, scrapeops_url, api_key):
#     response = requests.get(scrapeops_url, params={'api_key': api_key, 'num_results': '1'})
#     browser_headers = response.json()['result'][0]
#     return browser_headers

# Get single listing url
def extract_single_listing_url_yp_usa(result):
    element = result.find("a", {"class": "business-name"})
    lateral_string = element.get('href') if element else None
    
    # Construct the URL for the specific listing page 
    listing_url = 'https://www.yellowpages.com{}'.format(lateral_string)
    return listing_url

# Get company name
def extract_company_name_yp_usa(soup):
    company_name_element = soup.find("h1", {"class": "dockable business-name"})
    return company_name_element.text if company_name_element else None

# Get city 
def extract_city_yp_usa(soup):
    # Find the link element with 'href' containing 'state-'
    state_link_element = soup.find('a', href=lambda href: href and 'state-' in href)

    # Find the next 'a' tag (assuming city information is in the next 'a' tag)
    city_link_element = state_link_element.find_next('a') if state_link_element else None
    city_span_element = city_link_element.find('span').text if city_link_element else None
    return city_span_element


# Get state
def extract_state_yp_usa(soup):
    # Find the link element with 'href' containing 'state-'
    link_element = soup.find('a', href=lambda href: href and 'state-' in href)

    span_element = link_element.find('span').text if link_element else None

    return span_element

# Get zip
def extract_zip_yp_usa(soup):
    address_element = soup.find("span", {"class": "address"})
    return address_element.text.split(" ")[-1] if address_element else None

# Get Full Address
def extract_full_address_yp_usa(soup):
    address_span = soup.find("span", {"class": "address"})
    
    if address_span:
        street_address_span = address_span.find("span")
        street_address = street_address_span.text.strip() if street_address_span else None

        city_state_zip = address_span.contents[-1].strip() if address_span.contents else None

        if street_address and city_state_zip:
            full_address = f"{street_address}, {city_state_zip}"
            return full_address

    return None

# Get categories 
def extract_categories_yp_usa(soup):
    categories_element = soup.find('dd', {"class": 'categories'})
    categories = [a.text for a in categories_element.find_all('a')] if categories_element else None
    return categories

# Get email
def extract_email_yp_usa(soup):
    return soup.find("a", {"class": "email-business"}).get('href').replace("mailto:", "") if soup.find("a", {"class": "email-business"}) else None

# Get phone
def extract_phone_yp_usa(soup):
    phone_paragraph = soup.find('p', {"class": 'phone'})

    # Get the text content of the <span> element within the <p> element
    phone_number = phone_paragraph.find('span').next_sibling.strip() if phone_paragraph else None

    return phone_number  

# Get website
def extract_website_yp_usa(soup):
    website_paragraph = soup.find('p', {"class": 'website'})

    website_url = website_paragraph.find('a')['href'] if website_paragraph else None

    return website_url  

# Get social links
def extract_social_links_yp_usa(soup, social_media):
    socials = soup.find('dd', {"class": 'social-links'})
    
    social_links = socials.find_all('a', href=True) if socials else None

    if social_links:
        for link in social_links:
            href = link['href']
        if social_media in href:
            return href
    else:
        return None

     
# Get years in business
def extract_years_in_business_yp_usa(soup):
    years_in_business_div = soup.find('div', {"class": "years-in-business"})
    years_in_business_text = years_in_business_div.find('div', {"class": "count"}).strong.get_text(strip=True) if years_in_business_div else None
    years_in_business = int(years_in_business_text.split()[0]) if years_in_business_text else None
    return years_in_business
    
       
