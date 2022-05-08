from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bf
def movieScraper():
    req = Request("http://www.xiaopian.com/html/gndy/dyzz/index.html", headers={'User-Agent': 'Mozilla/5.0'})
    print(req)
    html = urlopen(req)
    print("html is", html)
    obj = bf(html.read().decode('gbk'),'html.parser')
    print("obj is", obj)
    tables = obj.find_all("a", class_="ulink")
    print("tables are",tables)
    for i,table in enumerate(tables):
        title = table["title"]
        if i == 6:
            break
        print(title)

if __name__ == '__main__':
    movieScraper()
