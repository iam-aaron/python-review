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

url = "http://py4e-data.dr-chuck.net/comments_1076110.html" #input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

num_list = list()
spans = soup('span')
for span in spans:
    print(span.contents[0])
    num_list.append(int(span.contents[0]))

Count = len(num_list)
Sum = sum(num_list)
print("COUNT:",Count)
print("SUM:",Sum)
