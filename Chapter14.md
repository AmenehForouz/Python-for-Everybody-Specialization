# Web Services and XML

**Data on the Web**
- with the http request/response well understood and well supported, there was a natural move toward exchanging data between programs using these protocols
- we needed to come up with an **agreed way to represent data going between applications and across networks.**
- there are two commonly used formats (Wire Formats or serialization formats): XML and JSON

- Python application ----> serialize ----> Wire Format (XML/JSON) ----> de-serialize -----> java application

**XML**
- eXtensible Markup Language
- primary purpose is to help information systems **share structured data**
- It started as simplified subset of the SGML- Standat Generalized Markup Language, and is designed to be relatively human-legible.
- whitespaces - we indent only for readability
- What is a complex element? A complex element is an XML element that have at least one attribute, or at least one sub (child) element.
- A simple element is an XML element that does not have any attributes or any sub (child) elements. A simple element can be declared with a simple datatype. 

```
    <people>  #start tag
        <person>
            <name>vidya</name> #vidya is text content
            <phone>956478</phone>
        </person>
        <person>
            <name>vidya</name>
            <phone type='int'>956478</phone> #type='int' is attribute
            <email hide='yes'/> #self closing tag
        </person>
    </people>   #end tag
```
- tags indicate the beginning and end of elements.
- Attributes - key/value pairs on opening tags of xml
- serialize/de-serialize - convert data in one program into a common format that can be stored and transmitted between systems in a programming language-independent manner.
- XML as a tree
    - tags are parent or intermediate nodes
    - texts and attributes are always child nodes
- XML as path
    - if a is parent node or tag and b is intermediate node then path will be /a/b

**XML Schema**
- describing a 'contract' as to what is acceptable XML
- if perticular piece of XML meets the specification of schems - it is said to 'validate'
- We give XML document and XML Schema to Validator as inputs.
- https://www.w3schools.com/xml/schema_example.asp

- Many XML Schema Languages
    - Document type definition - DTD
    - Standard Generalized Markup Language
    - **XML Schema from W3C - XSD**
        - xs:element
        - xs:complexType
        - xs:sequence
        - type="xs.string"
        - example of xml schema:
        ```
        <xs:element name="shipto">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="name" type="xs:string"/>
                    <xs:element name="address" type="xs:string"/>
                    <xs:element name="city" type="xs:string"/>
                    <xs:element name="country" type="xs:string"/>
                </xs:sequence>
            </xs:complexType>
            </xs:element>
        ```

**Parsing XML in python**

```
    import xml.etree.ElementTree as ET

    data = '''<person>
    <name>vidya</name>
    <phone>67348</phone>
    <email hide = "yes"/>
    </person>'''

    tree = ET.fromstring(data)
    print('Name:',tree.find('name').text)
    print('Attribute',tree.find('email').get('hide'))

    output:
    Name: vidya
    Attribute yes
```

```
    import xml.etree.ElementTree as ET

    data = '''
    <people>
    <person>
    <name>vidya</name>
    <phone>67348</phone>
    <email hide = "yes"/>
    </person>
    <person>
    <name>kunal</name>
    <phone>34356</phone>
    <email hide = "yes"/>
    </person>
    </people>
    '''

    tree = ET.fromstring(data)
    lst = tree.findall('person') #list of trees
    # print(lst)
    print('person count', len(lst))

    for item in lst:
        print('Name:',item.find('name').text)
        print('Phone:',item.find('phone').text)
        print('Attribute:',item.get('email'))

    output:
    person count 2
    Name: vidya
    Phone: 67348
    Attribute: None
    Name: kunal
    Phone: 34356
    Attribute: None
```



