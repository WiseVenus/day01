from urllib3.poolmanager import PoolManager #从urllib3.poolmanager模块导入PoolManager类

def down_html(url:str,encoding = "utf-8",method = "get"):
    pm = PoolManager()
    result = pm .request(method,url)
    if(result.status == 200):
        return result.data.decode(encoding=encoding)
    else:
        return None


from urllib.parse import urljoin #导入urlib.parse模块的urljoin函数

