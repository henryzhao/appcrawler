# coding:utf-8

import urllib2
from bs4 import BeautifulSoup

url = "http://www.wandoujia.com/apps"
url2 = "http://www.wandoujia.com/category/5029/2"

print '1'
response = urllib2.urlopen(url2)
print response.getcode()
html_doc = response.read()
print html_doc


soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
links = soup.find_all('a')
for link in links:
    print link['href'], link.get_text()