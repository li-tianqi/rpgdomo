#!/usr/bin/env python3
# coding=utf-8


import json
import pickle

dic = {'age':23, 'job': 'student'}

# to str with 'dumps(obj)'
dic_str = json.dumps(dic)
print(type(dic_str), dic_str)

# from str to obj with 'loads(str)'
dic_obj = json.loads(dic_str)
print(type(dic_obj), dic_obj)


# to json file
with open('test2.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f)
    
with open('test2.json', encoding='utf-8') as f:
    obj = json.load(f)
    print(type(obj), obj)
    
    
    
class Character:
    def __init__(self, name, coordinate, speed):
        self.name = name
        self.coordinate = coordinate
        self.speed = speed
        
    def move(self, distance):
        sour = self.coordinate
        dest = []
        dest.append(sour[0]+distance[0])
        dest.append(sour[1]+distance[1])
        self.coordinate = tuple(dest)
        print(self.name, "from ", sour, " move to ", self.coordinate, " with speed ", self.speed)
        
ch01 = Character('初一', (5,10), 2)
print(ch01.coordinate)
print(ch01.__dict__)
#ch01.move((3,4))

with open('test1.json', 'w', encoding='utf-8') as f:
    json.dump(ch01, f, default=lambda obj: obj.__dict__)
    
def dict2Character(dic):
    return Character(dic['name'], dic['coordinate'], dic['speed'])
    
with open('test.json', encoding='utf-8') as f:
    obj = json.load(f, object_hook=dict2Character)
    print(type(obj))
    obj.move((3,4))
    
with open ('test_p', 'wb') as f:
    pickle.dump(ch01, f)
    
with open('test_p', 'rb') as f:
    aaa = pickle.load(f)
    aaa.move((2,3))
    