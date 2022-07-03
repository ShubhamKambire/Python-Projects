import requests
from bs4 import BeautifulSoup

Url = "http://www.values.com/inspirational-quotes"
r = requests.get(Url)
soup = BeautifulSoup(r.content, 'html5lib')
quotes = []

table = soup.find('div', attrs={'id': 'all_quotes'})


for row in table.findAll('div', attrs = {'class':'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    
    
    quotes.append(quote)

    