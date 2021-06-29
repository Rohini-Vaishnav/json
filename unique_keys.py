import json
dic={'a':1,'b':3,'a':3}
dict1={}
for i in dic:
    if i in dic:
        dict1[i]=dic[i]
print(dict1)
file=open("unique_keys.json","w")
json.dump(dic,file,indent=4)
file.close()