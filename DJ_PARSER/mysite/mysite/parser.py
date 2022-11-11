import requests


class Parser(object):
    def setSession(self):
        self.session = requests.session()

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