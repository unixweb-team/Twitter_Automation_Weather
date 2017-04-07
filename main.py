import socket  #required
import os
import json

def httpGet(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            #request = str(data)
            temp.write(data)
        else:
            break
    s.close()
    
def parse():
    temp = open('temp.txt', 'r').readlines()
    os.remove('temp.txt')  #removes file after its been copied
    
    temp = str(temp)
    word = ''
    i=0
    
    while i < len(temp):
        word = word + str(temp[i])
        i += 1
    parsedata = word    
    parsedata = '{' + parsedata.split(", '{")[1]  #gets the json section of the socket connection
    parsedata = parsedata[:len(parsedata)-10]   #removes uneeded junk at the end of the file
    jsonfile = open('data.json', 'w')
    jsonfile.write(parsedata)  #writes to a json file
    jsonfile.close()
    
temp = open('temp.txt', 'wb')  #writes socket info to file
httpGet('http://localhost/example.json')  #url data here
temp.close()
parse()

jsonfile = open('data.json', 'r')
data = json.load(jsonfile)
temp = data["sensordatavalues"][0]  #gets the temp values from the json
hum = data["sensordatavalues"][1]  #gets humidity from the file

print(temp['value'])  #prints the temp value
print(hum['value'])  #prints humidity value




