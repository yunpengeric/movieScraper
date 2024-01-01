import requests
from bs4 import BeautifulSoup as bf
def movieScraper():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "en-US,en;q=0.9",  
        "Referer": "http://www.google.com", 
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1"
    }
    page = requests.get("http://m.xiaopian.com/html/gndy/dyzz/index.html", headers=headers)
    html = bf(page.content.decode("utf-8"), "html.parser")  
    print(html)
    tables = html.find_all("a", class_="ulink")
    for i,table in enumerate(tables):
        title = table["title"]
        if i == 6:
            break
        print(title)

if __name__ == '__main__':
    movieScraper()
