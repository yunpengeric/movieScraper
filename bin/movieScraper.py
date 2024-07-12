from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import random

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    ]
    return random.choice(user_agents)

def movie_scraper():
    url = "http://m.xiaopian.com/html/gndy/dyzz/index.html"
    
    options = Options()
    options.add_argument(f"user-agent={get_random_user_agent()}")
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        
        # Wait for the page to load (adjust the timeout and condition as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ulink"))
        )
        
        # Parse the page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, "html.parser")
        movie_links = soup.find_all("a", class_="ulink")
        
        for i, link in enumerate(movie_links[:6], 1):
            title = link.get("title", "No title found")
            print(f"{i}. {title}")
            time.sleep(random.uniform(1, 3))  # Random delay between processing each item
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    movie_scraper()