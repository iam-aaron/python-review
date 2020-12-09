# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getNameAndURL(count,pos,URL):
    if(count > -1):
        print("Retrieving:",URL)
        html = urlopen(URL, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup('a')
        tag = tags[pos]
        nexturl = str(tag.get('href', None))
        count = count-1
        getNameAndURL(count,pos,nexturl)
    else:
        count = 0
    return count

#url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html" #input('Enter - ')
#count = 4
#pos = 3
url = str(input('Enter URL: '))
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

getNameAndURL(count,pos-1,url)
