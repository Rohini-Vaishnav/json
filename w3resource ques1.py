import json
data='{"name":"muski","age":"21","class":"I"}'
a=json.loads(data)
print(a)
print(a["name"])
print(a["age"])
print(a["class"])