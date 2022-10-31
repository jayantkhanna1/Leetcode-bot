'''
The trick is to not think outside the box but to think there is no box
'''

from bs4 import BeautifulSoup
import requests
import json

# Link to pull answers
link = "https://github.com/jayantkhanna1/leetcode_solutions"

#  Getting whole page 
r = requests.get(link)
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('table')
# Getting links
anchors = s.find_all('a',rel = "nofollow")

# Getting question titles
names = []
flag = 0
anchors = list(anchors)
for x in anchors:
    names.append(x.text)

# Making json file
final_json = []
flag = 1       
for x in names:
    temp = {
        "question_number" : flag,
        "question_title" : x,
        "answer_link" : "https://raw.githubusercontent.com/jayantkhanna1/leetcode_solutions/master/solutions/python3/"+str(flag)+".py"
    }
    flag+=1
    final_json.append(temp)

# Writing to sample.json 
json_object = json.dumps(final_json, indent=4)
with open("answers.json", "w") as outfile:
    outfile.write(json_object)
