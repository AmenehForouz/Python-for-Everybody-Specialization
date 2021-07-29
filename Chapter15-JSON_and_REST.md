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

**API Security and Rate Limiting**
- the compute resources to run these APIs are not free
- data provided by these APIs is usually valuable
- data providers might limit the number of requests per day, demand API key, or even charge for usage.

**Authentication vs. Authorization**
- Authentication confirms that users are who they say they are. Authorization gives those users permission to access a resource.
- In simple terms, authentication is the process of verifying who a user is, while authorization is the process of verifying what they have access to. 
- Comparing these processes to a real-world example, when you go through security in an airport, you show your ID to authenticate your identity.

