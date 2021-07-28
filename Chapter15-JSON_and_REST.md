# JSON and the REST Architecture
- JavaScript Object Notation
- json represents data as nested lists and dictionaries.

- json as dictionary
```
    import json
    data = '''{
        "name":"vidya",
        "phone":{
            "type":"int",
            "number":"956479"
        },
        "email": {
            "hide":"yes"
        }
    }'''

    info = json.loads(data)
    print('Name',info["name"])
    print('Hide:',info["email"]["hide"])

    output:
    Name vidya
    Hide: yes
```

- json as list of dictionaries
```
    import json
    data = '''[
        { 
            "id":"001",
            "name":"vidya"
        },
        {
            "id":"002",
            "name":"kunal"
        }
    ]'''

    infolst = json.loads(data)
    print("user count:",len(infolst))
    for item in infolst:
        print("Id:",item['id'])
        print("Name:",item['name'])

    output:
    user count: 2
    Id: 001
    Name: vidya
    Id: 002
    Name: kunal
```

**Service oriented architecture**
- Service-Oriented Architecture (SOA) is a style of software design where services are provided to the other components by application components, through a communication protocol over a network. Its principles are independent of vendors and other technologies.
- https://medium.com/@SoftwareDevelopmentCommunity/what-is-service-oriented-architecture-fa894d11a7ec


**API - Application programming Interfaces**
- to communicate between 2 different applications.
