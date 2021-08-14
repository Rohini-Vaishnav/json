# import json
# file_name="saral7.text"
# dict={}
# with open(file_name) as file:
#     for line in file:
#         key,value=line.strip().split(None,1)
#         dict[key]=value.strip()
# print(dict)

import json
dic={}
file=open("Text.txt","r")
for line in file:
    key,value=line.strip().split(None,1)
    dic[key]=value.strip()
print(dic)