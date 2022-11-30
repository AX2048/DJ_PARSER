# pip install fake-useragent
# pip install selenium
# pip install pandas
# pip install bs4
# CloudFlare https://www.vindecoderz.com/

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from fake_useragent import UserAgent


ua = UserAgent()
fua = ua.Chrome
url = 'https://mail.ru/'
#headers = {'User-Agent': fua} # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36


options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={fua}') #"user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
options.add_argument("--disable-blink-features=AutomationControlled")

# driver = webdriver.Chrome(
#     executable_path="/path/chromedriver",
#     options=options
# )

s = Service(executable_path="/path/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    #driver.get("https://www.vindecoderz.com/")
    #driver.get(url)

    print(fua)

    time.sleep(20)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
