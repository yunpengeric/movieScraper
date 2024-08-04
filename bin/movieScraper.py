import requests
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
    url = "http://www.etdown.net"
    
    session = requests.Session()
    
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://www.google.com",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive"
    }
    
    try:
        # First, make a GET request to the homepage
        session.get("http://www.etdown.net", headers=headers, timeout=10)
        time.sleep(random.uniform(2, 5))

        # Now request the actual page we want
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # if "/_guard/auto.js" in response.text:
        #     print("Anti-bot protection still detected. Trying another approach...")
        #     time.sleep(random.uniform(5, 10))  # Wait longer
            
        #     # Try to fetch the JavaScript file
        #     js_response = session.get("http://m.xiaopian.com/_guard/auto.js", headers=headers)
        #     print(f"JavaScript response status: {js_response.status_code}")
            
        #     # Make the main request again
        #     response = session.get(url, headers=headers, timeout=10)
        
        soup = BeautifulSoup(response.content, "html.parser")
        movie_links = soup.select("td.list2 > span.ys_3 > a[target='_blank']:nth-of-type(2)")
        
        if not movie_links:
            print("No movie links found. Printing full response content:")
            print(response.text)
        else:
           # Extract only the text content that are likely to be Chinese movie names
           movie_names = [link.text for link in movie_links if link.text and not link.find('img') and link.text != '网站导航']

        # Print the results
           for name in movie_names:
            print(name) 
                        
    except requests.RequestException as e:
        print(f"An error occurred while fetching the page: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    movie_scraper()