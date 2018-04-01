import urllib.request
from bs4 import BeautifulSoup
import requests

def fand_mei(url,j):

    wb_date = requests.get(url)
    wb_date.encoding = 'gbk'
    soup = BeautifulSoup(wb_date.text, 'lxml')
    images = soup.select('img[width="234"]')
    titles = soup.select('div.title > span > a')
    cates = soup.select('div.items_comment > a:nth-of-type(2)')
    wenjians=soup.select('div.item_t > div > div.ABox > a')
    # 定义要创建的目录
    mkpath = "h:\\image\\"
    # 调用函数

    for i in range(24):
        mkdir(mkpath + titles[i].get_text() + '\\')
        path=titles[i].get_text()
        url1=wenjians[i].get('href')
        fand_wenjian(url1,path,mkpath)
        #urllib.request.urlretrieve(images[i].get('src'),'H:\image\%d_%s.jpg'%(j,i))
    for image,title,cate,wenjian in zip(images,titles,cates,wenjians):
        date={
            'image':image.get('src'),
            'title':title.get_text(),
            'cate':cate.get_text(),
            'wenjian_url':wenjian.get('href'),
        }
        print(date)

def fand_wenjian(url1,path,mkpath):
    import text
    text.counts(url1,path,mkpath)


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


for i in range(1,2):
        url = "http://www.mmonly.cc/mmtp/list_9_%s.html" % i
        j=i
        print('第%s页'% i)
        fand_mei(url,j)


