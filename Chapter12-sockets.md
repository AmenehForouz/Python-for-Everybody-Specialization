# Networked Technology

**TCP - Transport Control protocol**
- built on top of IP (internet protocol)
- assumes IP might lose some data-stores and retransmits data if it seems to be lost
- Handles "Flow control" using a transmit window
- provides a nice reliable pipe

**TCP Connections / Sockets**
- In computer networking, an internet socket or network socket is an endpoint of bidirectional inter-process communication flow across an internet protocol based computer network, such as Internet.
- Process <--------> Internet <---------> Process

**TCP Port Numbers**
- port is an application specific or process specific software communication endpoint
- it allows multiple networked applications to coexixt on the same server.
- there is list of well known tcp port numbers
- port 80 - http
- port 443 - https

**Common TCP Ports**
- Telnet (23) - login
- SSH (22) - Secure Login
- HTTP (80)
- HTTPS(443) - SECURE
- SMTP (25) -Mail
- IMAP (143/220/993) - Mail retrival
- POP (109/110) - Mail retrival
- DNS (53) - Domain name
- FTP (21) - File transfer

**Sockets in Python**
- python has built in support for TCP sockets
- connect method takes hostname and port number

- to make the connection (dialing the phone):
```
    import socket
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect(('data.pr4e.org',80))  # host and port must be tuple.
```

**What is Protocol?**
-  a set of rules that all parties follow so we can predict each other's behavior.

**HTTP - Hypertext transfer protocol**
- the dominant application layer protocol on the internet
- invented for the web - to retrive HTML, Images, Documents, etc.
- extended to be data in addition to documents - RSS, Web services. etc.
- Basic concept - Make a connection - Request a document - retrive the document - close the connection
- HTTP is the set of rules to allow browsers to retrive web documents from server over the internet.

**uniform resource locator : URL**
- http://www.google.com/page.html
- url = protocal + host + documet
- url is concatenation of above three

**Getting data from the Server**
- when user clicks on anchor tag with href= value to switch to a new page, browser makes a connection to the web server and issues 'GET' request - to get the content of the page at specified URL.
- the server returns the html document to browser which formats and displays the document to user.

**Internet Standards**
- standards for all of the internet protocols are developed by an organization
- Internet Engineering Task Force (IETF)
- www.ietf.org
- standards are called - "RFSs" - Request for Comments

**HTTP request in python**

```
    import socket
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect(('data.pr4e.org',80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(512)
        if (len(data) < 1):
            break
        print(data.decode())
    mysocket.close()
```
- **Socket programming** is a way of connecting two nodes on a network to communicate with each other. 
- One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket (accept the request) while client reaches out to the server.(send the request)
- **AF_INET** is an address family that is used to designate the type of addresses that your socket can communicate with
- **SOCK_STREAM** - socket type which is implemented on the Transmission Control Protocol/Internet Protocol (TCP/IP) protocol. A stream socket provides for the bidirectional, reliable, sequenced, and unduplicated flow of data without record boundaries.
- connect method accept only one argument,hence host and port must be tuple.
- **send()**
    - The send()method of Python's socket class is used to send data from one socket to another socket.
    - The send()method can only be used with a connected socket. That is, send() can be used only with a TCP based socket and it can not be used with UDP socket.
    - The send() method can be used to send data from a TCP based client socket to a TCP based client-connected socket at the server side and vice versa.
    - The data sent should be in bytes format. String data can be converted to bytes by using the encode() method of string class.
- In case the data is in string format, the **encode()** method of str can be called to convert it into bytes.
- **recv()**
    - receives up to buffersize bytes from the socket.
    - Unlike send(), the recv() function of Python's socket module can be used to receive data from both TCP and UDP sockets.
    - Returns the received data as bytes object. hence we use decode() function to convert it to bytes.
- encode() function belongs to str class, str.encode()
- decode() function belongs to bytes class, bytes.decode()


