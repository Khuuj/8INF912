import pyautogui as ptg
import math

def move(x=None, y=None):

    screenWidth, screenHeight = ptg.size()
    screenWidthMiddle = screenWidth / 2
    screenHeightMiddle = screenHeight / 2

    print(screenWidthMiddle)
    print(screenHeightMiddle)

    if not x:
        ptg.moveTo(screenWidthMiddle, screenHeightMiddle, 0.7)


import numpy as np

#Q =[45,456,47,123,4]
#Q.insert(0,14)
#del Q[0]
#print (Q)

import json

data = {}  
data['people'] = []  
data['people'].append({  
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({  
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({  
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.json', 'w') as outfile:  
    json.dump(data, outfile, indent=4)


with open('test.json') as json_file:  
    data = json.load(json_file)
    data['hero0'].append({
        '2':"ba,a"
    })
#    a= data['hero0']
#    b= a[0]
#    c = b['0']
#    d=c[0]
#    e=d['endturn']
#    f=e['etats suivant']

with open('test.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)