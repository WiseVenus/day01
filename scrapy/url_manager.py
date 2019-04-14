class Url_Manager(object):
    'URL管理器 主要是两个集合 一个已爬 一个待爬'
    def __init__(self):
        self.new_url = set()
        self.old_url = set()


    def add_url(self,url):
        '如果地址不在解析过的集合 也不在待爬集合 那就添加'
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    def add_urls(self,urls):
        '封装add_url方法的方法 循环添加url'
        for url in urls:
            self.add_url(url)

    def get_url(self):
        '从集合pop出一个地址 该地址会被添加到已爬集合中'
        url = self.new_url.pop()
        self.old_url.add(url)
        return url

    def has_url(self):
        '判断待爬集合是否还有数据'
        return len(self.new_url) > 0

if __name__ == "__main__":
    '这里写模块的单元测试'
    um = Url_Manager()
    urls = ["http://www.baidu.com"]
    um.add_urls(urls)
    print(um.new_url,um.old_url)
    um.get_url()
    print(um.new_url,um.old_url)
    print(um.has_url())
