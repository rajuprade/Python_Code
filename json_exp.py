import json

x = '{"name":"Raj","age":38,"City":"Narayangaon"}'

y = json.loads(x)

print(y["name"])

