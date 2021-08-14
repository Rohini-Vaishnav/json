import json
python_dict ={"name": "David", "age": 6, "class":"I"}
python_list =["Red", "Green", "Black"]
python_str = "Python Json"
python_int =(1234)
python_float =(21.34)
python_T =(True)
python_F =(False)
python_N =(None)
json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
json_n = json.dumps(python_N)
print(json_dict)
print(json_list)
print(json_str)
print(json_num1)
print(json_num2)
print(json_t)
print(json_f)
print(json_n)
print(type(json_list))

