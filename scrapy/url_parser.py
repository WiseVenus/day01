from bs4 import BeautifulSoup
from urllib.parse import urljoin
class UrlParser(object):
    def __init__(self):
        self.url = set()
        self.img = set()

    def __get_url(self,baseUrl:str,soup:BeautifulSoup):
        '解析出url 添加进url集合'
        for a in soup.find_all("a"):
            src = a.get("src")
            target_url = urljoin(baseUrl,src)
            self.url.add( target_url)
        pass

    def __get_img(self,baseUrl:str,soup:BeautifulSoup):
        '解析出img'
        for img in soup.find_all("img"):
            href = img.get("src")
            target_url = urljoin(baseUrl,href)
            self.url.add( target_url)
        pass

    def html_parse(self,baseUrl,html_source):
        soup = BeautifulSoup(html_source,"html_parser")
        self.__get_url(baseUrl,soup)
        self.__get_img(baseUrl,soup)

        #返回多个 默认封装成一个元组
        return self.url,self.img

if __name__ == "__main__":
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    
    <p class="story">...</p>
    """
    soup = BeautifulSoup(html_doc,"html.parser")
    for link in soup.find_all('a'):
        print(link.get('href'))


