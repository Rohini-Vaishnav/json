import json
complex_data={"list":[1,2,3,4,5],"int":123,"boolean":True,"float":5.9}
a=json.dumps(complex_data,indent=4)
print(a)
print(type(a))