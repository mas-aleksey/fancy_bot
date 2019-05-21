import requests
import random

url = 'https://api.vk.com/method/wall.get'

def getjson(url, data):
    response = requests.get(url, params = data)
    response = response.json()
    return response

def getTotalCount():
    response = getjson(url, getData(1))
    return response['response']['count'] - 1

def getData(offset):
    return { 'domain' : 'yxa.xaxa',
        'count' : '100',
        'offset' : offset,
        'access_token' : '82f2bb033f38de4e89cb2766475a45d684afc9577f3ad0c67032c9ac9ca60f1645522a55a2a3a8187b9f6',
        'v' : '5.68' }

def getRndYxa():
    #rnd = random.randint(0, getTotalCount())
    totalcount = getTotalCount()
    offset = 0
    f = open("yxa.txt", "w+")
    count =0
    while totalcount > offset:
        data = getData(offset)
        response = getjson(url, data)
        for item in response['response']['items']:
            try:
                f.write(item['text'] + "\n#\n")
                count +=1
            except:
                print(offset)
                continue
        offset += 100
    print(count)
    #return response['response']['items'][0]['text']

#load

def getRnd():
    t = len(rzhaka)-1
    return(rzhaka[random.randint(0, t)])


y = open("yxa.txt")
rzhaka = y.read().split('\n#\n')
#getRnd()

#print(getRndYxa())