import requests, sys
from bs4 import BeautifulSoup


url = 'https://habr.com/ru/all/'


page = requests.get(url)

print(f'File :: {__file__} | SYS :: {sys.version}')
print(f'\nPAGE STATUS :: {page.status_code}')


filteredNews = []
allNews = []
hrefs = []

soup = BeautifulSoup(page.text, "html.parser")

print('')
#print(soup) #выведет html страницы

allNews = soup.findAll('a', class_='tm-article-snippet__title-link')
print(allNews)

for data in allNews:
    if data.find('span') is not None:
        filteredNews.append(data.text)


print('')
i=0
for data in filteredNews:
    i = i + 1
    print(f'{i} {data}')
    #print(f'{data}')
