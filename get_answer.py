import requests
from bs4 import BeautifulSoup

data= requests.get("https://raw.githubusercontent.com/jayantkhanna1/Leetcode-solutions/master/src/0029-Divide-Two-Integers/0029.cpp")

soup = BeautifulSoup(data.content, 'html.parser')

print(soup)
