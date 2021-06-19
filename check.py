import requests
from bs4 import BeautifulSoup

def isAccess():
    url = 'https://drive.google.com/open?id=1Ab29PPkzm53DloQKHmYe5PRkxFXCchSj'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    title = str(soup.find('title'))
    if 'access_BanManager' in title:
        return True
    else:
        return False
