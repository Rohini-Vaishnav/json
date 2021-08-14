import json
l1=["neelam","programmer","24","2400",]
l2=["komal","trainer","24","20000"]
l3=["anuradha","HR","25","40000"]
l4=["Abhisheck","manage","29","63000"]
l5=["name","designation","age","salary"]
dic1={}
dic2={}
dic3={}
dic4={}
dic={}
i=0
while i<len(l1):
    j=0
    while j<len(l1):
        dic1[l5[i]]=l1[j]
        dic2[l5[i]]=l2[j]
        dic3[l5[i]]=l3[j]
        dic4[l5[i]]=l4[j]
        j=j+1
    dic["emp1"]=dic1
    dic["emp2"]=dic2
    dic["emp3"]=dic3
    dic["emp4"]=dic4
    i=i+1
print(dic)
f=open("saral8.json","w")
json.dump(dic,f,indent=4)

