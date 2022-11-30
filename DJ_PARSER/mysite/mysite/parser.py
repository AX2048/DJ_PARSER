import requests
from fake_useragent import UserAgent

class Parser(object):
    def setSession(self):
        self.session = requests.session()
        # instance of fake user agent
        ua = UserAgent()
        print(ua.chrome)
        # create header var in self oto store new fake useragent
        self.fakeHeader = {'User-Agent':str(ua.chrome)}
        print(self.fakeHeader)

        self.session.headers.update(self.fakeHeader)
        
    def setUrl(self,url):
        if not isinstance(url,str) and (url < 10):
            return None
        self.url = url

    def doRequest(self):
        try:
            if not self.url:
                print('not nonzero string is url -> ', self.url)
            self.response = self.session.get(self.url)
            self.response.encoding = self.response.apparent_encoding
            print('======request=====')
            print('url:',self.url)
            print('headers:',self.session.headers)
            print('status:',self.session.cookies)
        except Exception as e:
            raise e
            return None
        print('===response=====')
        print('headers:',self.response.headers)
        print('status:',self.response.status_code)

    def parseUrl(self):
        import bs4
        # print(self.response.text)
        self.bs=bs4.BeautifulSoup(self.response.text, "html.parser")

    def getLinkA(self, classStr=None):
        if classStr is None:
            atag=self.bs.find_all('a')
            for a in atag:
                yield a
        elif isinstance(classStr, str):
            atag = self.bs.find_all('a', {"class": classStr})
            for a in atag:
                yield a
            pass #  {"class": "tm-article-snippet__title-link"}
        
    def initSelenium(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        self.browser = webdriver.Firefox()
        self.browser.get(self.url)
        self.browser.implicitly_wait(300)
        elements = self.browser.find_elements(By.TAG_NAME, 'a')

        for e in elements:
            print(e.text)
            yield e.text

    def parseSeleniumUrl(self):
        import bs4
        # print(self.response.text)
        self.bs=bs4.BeautifulSoup(self.seleniumHtml, "html.parser")

    def runSelenium(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.common.by import By
        
        import time

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
            driver.get(url)
            #driver.get("https://www.vindecoderz.com/")
            #driver.get(url)
            
            # return html

            # wait = WebDriverWait(driver, 0)
            #element= wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="news-item-link"]')))
            # print(element.text)
            # time.sleep(0.2)
            # elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='news-item-link']")))
            a_elements =  driver.find_elements(By.CLASS_NAME, "news__list__item__link__text")
            # elems = driver.find_elements(By., "//*[@class='news__list__item__link__text']")
            for elem in a_elements:
                print("----a-------",len(a_elements))
                print(elem.text)
                if not elem.text:
                    break
                print(elem.get_attribute("class"))
                print(elem.get_attribute("href"))
                
                
            # self.seleniumHtml = ' '.join(a_elements)
            # print(a_elements)
            # print(fua)
            # print(self.seleniumHtml)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()