import requests
from fake_useragent import UserAgent


class Parser(object):
    def setSession(self):
        self.session = requests.session()
        # instance of fake user ag
        ua = UserAgent(verify_ssl=False)
        print(ua.chrome)
        # create header var in self oto store new fake useragent
        self.fakeHeader = {"User-Agent": str(ua.chrome)}
        print(self.fakeHeader)

        self.session.headers.update(self.fakeHeader)

    def setUrl(self, url):
        if not isinstance(url, str) and (url < 10):
            return None
        self.url = url

    def doRequest(self):
        try:
            if not self.url:
                print("not nonzero string is url -> ", self.url)
            self.response = self.session.get(self.url)
            self.response.encoding = self.response.apparent_encoding
            print("======request=====")
            print("url:", self.url)
            print("headers:", self.session.headers)
            print("status:", self.session.cookies)
        except Exception as e:
            raise e
            return None
        print("===response=====")
        print("headers:", self.response.headers)
        print("status:", self.response.status_code)

    def parseUrl(self):
        import bs4

        # print(self.response.text)
        self.bs = bs4.BeautifulSoup(self.response.text, "html.parser")

    def getLinkA(self, classStr=None):
        if classStr is None:
            atag = self.bs.find_all("a")
            for a in atag:
                yield a
        elif isinstance(classStr, str):
            atag = self.bs.find_all("a", {"class": classStr})
            for a in atag:
                yield a
            pass  #  {"class": "tm-article-snippet__title-link"}

    def initSelenium(self):
        import chromedriver_autoinstaller
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait

        chromedriver_autoinstaller.install()

        self.browser = webdriver.Firefox()
        self.browser.get(self.url)
        self.browser.implicitly_wait(30)
        elements = self.browser.find_elements(By.TAG_NAME, "a")

        for e in elements:
            print(e.text)
            yield e.text

    def parseSeleniumUrl(self):
        import bs4

        # print(self.response.text)
        self.bs = bs4.BeautifulSoup(self.seleniumHtml, "html.parser")

    def runSelenium(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.wait import WebDriverWait
        from webdriver_manager.chrome import ChromeDriverManager

        chrome_path = "chrome_drv/chromedriver"  # ChromeDriverManager().install() # chrome_drv/chromedriver
        print(chrome_path)

        ua = UserAgent()
        fua = ua.Chrome
        url = "https://mail.ru/"
        # headers = {'User-Agent': fua} # Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36

        options = webdriver.ChromeOptions()
        options.add_argument(
            f"user-agent={fua}"
        )  # "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0"
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--log-level=3")

        s = Service(
            executable_path=chrome_path
        )  # executable_path = chromedriver_autoinstaller.install() /code/chrome_drv/chromedriver

        driver = webdriver.Chrome(service=s, options=options)  # Собираем драйвер

        try:
            driver.get(url)
            driver.implicitly_wait(1)

            # elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='news-item-link']")))
            a_text_els = driver.find_elements(By.CLASS_NAME, "news__list__item__link__text")
            a_href_els = driver.find_elements(By.CLASS_NAME, "news__list__item__link")

            # a_elements =  driver.find_element_by_xpath("//span[@class=\"news__list__item__link\"]") #news__list__item__link news__list__item__link_simple
            # elems = driver.find_elements(By., "//*[@class='news__list__item__link__text']")
            data = dict()
            for text, href in zip(a_text_els, a_href_els):
                print("----a-------", len(a_text_els), len(a_href_els))
                print(f"text :: {text.text}")
                print(f"hreh :: {href.get_attribute('href')}")
                if not text.text:
                    print("text out")
                    break
                data.update({"href": href.get_attribute("href")})
                data.update({"text": text.text})
                yield data
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
