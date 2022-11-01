'''
The trick is to not think outside the box but to think there is no box
'''

from bs4 import BeautifulSoup
import requests
import json

# Link to pull answers
link = "https://github.com/jayantkhanna1/leetcode-solutions"

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

# Getting answers link
answers = []
answer_anchor = s.find_all('a',text = "c++")
for x in answer_anchor:
    answers.append(x['href'])

for x in range(0 , len(answers)):
    temp = str(answers[x])
    temp = temp.replace('blob/','')
    answers[x] = temp
    
# Making json file
final_json = []
flag = 1       
for x in range(0,len(names)):
    temp = {
        "question_number" : flag,
        "question_title" : names[x],
        "answer_link" : "https://raw.githubusercontent.com"+answers[x]
    }
    flag+=1
    final_json.append(temp)

# Writing to sample.json 
json_object = json.dumps(final_json, indent=4)
with open("answers.json", "w") as outfile:
    outfile.write(json_object)
