import requests
from bs4 import BeautifulSoup as bf
def movieScraper():
    page = requests.get("http://www.xiaopian.com/html/gndy/dyzz/index.html", headers={'User-Agent': 'Mozilla/5.0'})
    html = bf(page.content.decode("gbk"), "html.parser")  
    tables = html.find_all("a", class_="ulink")
    for i,table in enumerate(tables):
        title = table["title"]
        if i == 6:
            break
        print(title)

if __name__ == '__main__':
    movieScraper()
