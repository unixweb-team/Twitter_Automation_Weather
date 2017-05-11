import socket  #required
import os
import json
import tweepy

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
    
def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)
    
def main():
    #fill in the info with correct values
    cfg = {
        "consumer_key":"VALUE", 
        "consumer_secret":"VALUE", 
        "access_token":"VALUE", 
        "access_token_secret":"VALUE"
        }
    
    api = get_api(cfg)
    tweet = "Hello World"
    api.update_status(tweet)
    
while True:  #runs the bot constantly
    temp = open('temp.txt', 'wb')  #writes socket info to file
    httpGet('http://192.168.10.40/data.json')  #url data here
    temp.close()
    parse()

    jsonfile = open('data.json', 'r')
    data = json.load(jsonfile)
    temp = data["sensordatavalues"][0]  #gets the temp values from the json
    hum = data["sensordatavalues"][1]  #gets humidity from the file

    temp = "Temperature  = " + temp['value']  #prints the temp value
    hum = "Humidity = " + hum['value']  #prints humidity value  
    main()


