import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/comments_42.xml' #TEST URL
url = 'http://py4e-data.dr-chuck.net/comments_1076112.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
comments = tree.findall('comments/comment')
print('Count: ', len(comments))

count_list = list()
for comment in comments:
    #print('NAME: ', comment.find('name').text)
    #print('COUNT: ', comment.find('count').text)
    count_list.append(int(comment.find('count').text))

Sum = sum(count_list)
print("Sum:",Sum)
