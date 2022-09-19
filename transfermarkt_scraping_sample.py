from turtle import title
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import urlretrieve
from os import makedirs

# LeagueInforArr
from LeagueInfoArr import arr

# constants 
CountryNameInArr = 0
TierInArr = 1
LeagueURLInArr = 2
Title = 'title'
logfile = 'logfile.txt'

logfile = open(logfile, 'a', encoding='UTF-8')

# get the League Info from arr
i = 0
res = requests.get(arr[i][LeagueURLInArr])

print(arr[i][LeagueURLInArr])
print(res.content)

# create BeautifulSoup object
soup = BeautifulSoup(res.text, 'html.parser')

elems = soup.find_all(Title)

for elem in elems:
    # debug
    print(elem.contents[0])
    # Write to file
    logfile.write(elems.contents[0])
