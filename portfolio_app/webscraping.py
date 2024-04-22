import requests
from bs4 import BeautifulSoup

class getData:
    def __init__(self):
        self.url = "https://sputnikglobe.com/"
        self.links = []

    def getSourceCode(self):
        r = requests.get(self.url)
        if(r.status_code == 200):
            self.BeautifulSoupProcess(r.content)
        return self.links

    def BeautifulSoupProcess(self,context):
        soup = BeautifulSoup(context,"lxml")
        self.LatestNewsLinks(soup)
        self.otherLinks(soup)
        

    def LatestNewsLinks(self,soup):
        links = soup.find_all('a', attrs={"class":"cell-list__item m-no-image"})
        #print(links)
        for link in links:
            href = self.url + link.get('href')
            self.links.append({href,"latest_news"})
            #print(link.get('href'))

    def otherLinks(self,soup):
        #print("now for some other links")
        otherlinks = soup.find_all('a', attrs={"class":"cell-list__item"})
        #print(links)
        for link in otherlinks:
            category = (link.find_parent('div',attrs={"class":"cell-list__list"}).previous_sibling).text
            href = self.url + link.get('href')
            self.links.append({href,category})
            #print(category)
            #print(link.get('href'))

myLinks = getData().getSourceCode()

#for link,category in myLinks:
    #print(link,category)

#"https://webscraper.io/test-sites/e-commerce/allinone"

url = "https://sputnikglobe.com/20240420/us-house-votes-360-58-to-pass-bill-to-give-frozen-russian-assets-to-ukraine-compel-sale-of-tiktok-1118032226.html"

class newData:
    def __init__(self,url):
        self.url = url

    def getSourceCode(self):
        r = requests.get(url)
        #if(r.status_code == 200):
        self.BeautifulSoupProcess(r.content)

    def BeautifulSoupProcess(self,content):
        soup = BeautifulSoup(content,"lxml")
        self.GetDetails(soup)

    def GetDetails(self,soup):
        title = soup.find('h1', attrs={"class":"article__title"}).text
        news_image = soup.find('div',attrs={"class":"media__size"}).find('img').get('src')
        announcment = soup.find('div', attrs={"class":"article__announce-text"}).text
        article_body = soup.find('div',attrs={"class":"article__body"}).text
        
        print(title)
        print(news_image)
        print(announcment)
        print(article_body)

newData(url).getSourceCode()

#https://sputnikglobe.com/20240420/us-house-votes-360-58-to-pass-bill-to-give-frozen-russian-assets-to-ukraine-compel-sale-of-tiktok-1118032226.html
#url = "https://sputnikglobe.com/20240419/anonymous-hackers-allegedly-steal-over-20-gigabytes-of-idf-files-1118017661.html"
