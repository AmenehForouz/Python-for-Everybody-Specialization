import json
data = '''
[
    { 
        "id":"001",
        "name":"vidya"
    },
    {
        "id":"002",
        "name":"kunal"
    }
]
'''

infolst = json.loads(data)
print("user count:",len(infolst))
for item in infolst:
    print("Id:",item['id'])
    print("Name:",item['name'])

