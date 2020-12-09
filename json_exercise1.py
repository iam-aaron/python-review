import urllib.request, urllib.parse, urllib.error
import json

url = str(input('Enter URL: '))
print("Retrieving:",url)
data = urllib.request.urlopen(url).read().decode()

try:
    comments = json.loads(data)['comments']
except:
    print('==== Failure To Retrieve ====')
    quit()

#comments = js['comments']
num_list = list()
for comment in comments:
    num_list.append(comment['count'])

Count = len(num_list)
Sum = sum(num_list)
print("COUNT:",Count)
print("SUM:",Sum)
