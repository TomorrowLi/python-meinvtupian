import urllib.request
from bs4 import BeautifulSoup
import requests
import re

def fand(url,j,path,mkpath):
    we_date=requests.get(url)
    we_date.encoding='gbk'
    soup=BeautifulSoup(we_date.text,'lxml')
    images=soup.select('#big-pic > p > a > img')
    image=images[0].get('src')
    urllib.request.urlretrieve(image, mkpath+path+'\\%s.jpg' % j)
    print(image)

def main(coun,url1,path,mkpath):
    for i in range(1,int(coun)):
        if i==1:
            url = url1
            j=i
        elif i>=2:
            url=url1[:-5]+'_%s.html' % i
            j=i
        fand(url,j,path,mkpath)
def counts(url1,path,mkpath):
    we_date = requests.get(url1)
    we_date.encoding = 'gbk'
    soup = BeautifulSoup(we_date.text, 'lxml')
    couns = soup.select('div.pages > ul > li:nth-of-type(1) > a')
    coun = couns[0].get_text()
    coun = re.sub('\D', '', coun)
    print("共%s页"% coun)
    main(coun,url1,path,mkpath)


