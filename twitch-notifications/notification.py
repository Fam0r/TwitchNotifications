import config
import json
import requests
from datetime import datetime

def sendNotif(channel: str, username: str, message: str):
    c = config.getConfig()

    content = c['notifContent'].replace('{channel}', channel).replace('{username}', username).replace('{time}', str(datetime.now()).split('.')[0]).replace('{message}', message)

    if c['notifType'] == 'post':
        j = json.loads(content)
        requests.post(c['notifParams'], data=j)