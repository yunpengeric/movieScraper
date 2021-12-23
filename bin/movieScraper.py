from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bf
def movieScraper():
    req = Request("http://www.xiaopian.com/html/gndy/dyzz/index.html", headers={'User-Agent': 'Mozilla/5.0'})   
    req.encoding = 'gb18030'
    html = urlopen(req)
    obj = bf(html.read(),'html.parser')
    tables = obj.find_all("a", class_="ulink")
    for i,table in enumerate(tables):
        title = table["title"]
        if i == 6:
            break
        print(title)

if __name__ == '__main__':
    movieScraper()