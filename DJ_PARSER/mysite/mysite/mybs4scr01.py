from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


ua = UserAgent()
url = 'https://mail.ru/'
headers = {'User-Agent': ua.chrome} # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36


def parse():
    send = requests.get(url, headers=headers)
    soup = BeautifulSoup(send.content, 'html.parser') #.find('div', class_='grid__ccol svelte-3k1upp')
    
    
    print(ua.chrome)
    #print(send.content)
    print(soup)
    
    for item in soup.find_all('a', class_='news-item svelte-1qotzhx'):
        label = item.find('a', class_='news-item svelte-1qotzhx').text.strip()
        label = ''.join(label.split())
        
        print(label)
        
        
parse()