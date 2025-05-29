# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 16:53:31 2025

@author: Debodip Chowdhury
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up Selenium options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver_path = r"C:\Users\Debodip Chowdhury\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)
# Install and use the latest ChromeDriver

driver = webdriver.Chrome(service=service, options=chrome_options)
print(driver.title)  # Confirm page load

# Trustpilot Flipkart review page URL
url = 'https://www.trustpilot.com/review/www.flipkart.com'
driver.get(url)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'styles_reviewContentwrapper__Tzamw'))
    )
except Exception as e:
    print(f"Error loading reviews: {e}")
    driver.quit()
    exit()

# Extract reviews
data = []
reviews = driver.find_elements(By.CLASS_NAME, 'styles_reviewContentwrapper__Tzamw')  # Update class name if needed
reviews1 = driver.find_elements(By.CLASS_NAME, 'styles_reviewContent__SCYfD')
print(f"Number of reviews found: {len(reviews)}")
page_number = 1

while True:
 print(f"Scraping page {page_number}...")
 reviews = driver.find_elements(By.CLASS_NAME, 'styles_reviewContentwrapper__Tzamw')
 # Wait for reviews to be visible on each page
 try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'styles_reviewContentwrapper__Tzamw'))
        )
 except Exception as e:
        print(f"Error loading reviews on page {page_number}: {e}")
        break
 for review in reviews:
        try:
            # Always re-fetch the container element to avoid stale references
            container = review.find_element(By.CLASS_NAME, 'styles_reviewContent__SCYfD')

            try:
                anchor_el = container.find_element(By.TAG_NAME, 'a')
                title = anchor_el.find_element(By.TAG_NAME, 'h2').text.strip()
            except:
                title = ''

            try:
                content = container.find_element(By.TAG_NAME, 'p').text.strip()
            except:
                content = ''

            try:
                rating = review.find_element(By.CLASS_NAME, 'styles_reviewHeader__PuHBd').get_attribute('data-service-review-rating')
            except:
                rating = ''

            data.append([title, content, rating])

        except Exception as e:
            print(f"Skipping a review due to error: {e}")
            continue  # Skip to the next review

    #clicking the "Next" button to go to the next page
 try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'nav[aria-label="Pagination"] a[aria-label="Next page"]')
        driver.execute_script("arguments[0].click();", next_button)  # Click the "Next" button
        time.sleep(3)  # Wait for page load
        page_number += 1
 except:
        print("No more pages to scrape.")
        break  # Exit loop if no "Next" button is found
# Close WebDriver
driver.quit()

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Title', 'Content', 'Rating'])
print(df.head())
df.to_csv('trustpilotFlipkartReviews.csv', index=False, encoding='utf-8')
#print(df["Content"].iloc[0])
#print(df["Rating"])