import json
dict ='{"name": "David", "age": 6, "class": "I"}'
list ='["Red", "Green", "Black"]'
string ='"Python Json"'
int ='1234'
float ='21.34'
a=json.loads(dict)
b=json.loads(list)
c=json.loads(string)
d=json.loads(int)
e=json.loads(float)
print(a)
print(b)
print(c)
print(d)
print(e)
print(type(a))