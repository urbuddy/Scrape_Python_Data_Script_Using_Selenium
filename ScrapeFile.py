import json
from selenium import webdriver
from selenium.webdriver.common.by import By

websites = [
    "https://www.alfred.tech/",
    "https://www.align.com/",
    "https://www.alinatechnology.com/",
    "https://www.aliviaanalytics.com/",
    "https://www.allbusinesstechnologies.com/",
    "https://www.aatsg.com/",
    "https://www.allcomputercenter.com/",
    "https://www.allinonetechnology.com/",
    "https://www.all-lines-tech.com/",
    "https://www.allmtntech.com/",
]

output_data = []

for website in websites:
    # Initialize Selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Navigate to the website
    driver.get(website)

    # Scrape Meta title & description
    meta_title = driver.title
    meta_description = driver.find_element(By.CSS_SELECTOR, "meta[name='description']").get_attribute("content")

    # Scrape Total Number of Links on the page
    total_links = len(driver.find_elements(By.TAG_NAME, "a"))

    # Scrape Social Media links - Twitter & Linkedin
    social_links = {
        "twitter": None,
        "linkedin": None
    }
    for link in driver.find_elements(By.TAG_NAME, "a"):
        href = link.get_attribute("href")
        if "twitter.com" in href:
            social_links["twitter"] = href
        elif "linkedin.com" in href:
            social_links["linkedin"] = href

    # Scrape Number of times "technology" word is present on the website
    page_text = driver.find_element(By.TAG_NAME, "body").text
    technology_count = page_text.lower().count("technology")

    # Close the webdriver
    driver.quit()

    # Store data in dictionary
    website_data = {
        "meta_title": meta_title,
        "meta_description": meta_description,
        "total_links": total_links,
        "social_links": social_links,
        "technology_word_count": technology_count
    }

    output_data.append(website_data)

# Save data to JSON file
with open("website_details.json", "w") as json_file:
    json.dump(output_data, json_file, indent=4)
