import requests
import json
import os

from secrets import api_key

def getProjects():
    url = "https://api.timechimp.com/v1/projects"
    payload = {}
    headers = { 
    'Authorization' : api_key
    }
    response = requests.request("GET", url, headers=headers, data = payload)

    result = json.loads(response.text)

    return result

def getAll():
    result = getProjects()
    code = []
    prname = []
    csname = []
    for i in range(len(result)):
        code.append(result[i]['code'])
        prname.append(result[i]['name'])
        csname.append(result[i]['customerName'])
    return code, csname, prname

def getLatest():
    code, csname, prname = getAll()
    latest = 0
    index = 0
    for i in range(len(code)):
        if ((int(code[i])) > int(latest)):
            latest = code[i]
            index = i
    mapstring = "{} {} {}".format(latest, csname[index], prname[index])
    return mapstring

def makeFolder():
    folder = getLatest()
    os.mkdir('../{}'.format(folder))
    os.mkdir('../{}/projectfiles'.format(folder))
    os.mkdir('../{}/projectfiles/footage'.format(folder))
    os.mkdir('../{}/projectfiles/graphics'.format(folder))
    os.mkdir('../{}/projectfiles/img'.format(folder))
    os.mkdir('../{}/projectfiles/render'.format(folder))
    os.mkdir('../{}/documenten'.format(folder))
    os.mkdir('../{}/aangeleverd'.format(folder))
    os.mkdir('../{}/audio'.format(folder))
    os.mkdir('../{}/audio/cubase'.format(folder))
    os.mkdir('../{}/finals'.format(folder))
