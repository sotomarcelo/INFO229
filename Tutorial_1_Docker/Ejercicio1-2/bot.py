
'''
1) Néstor escucha los mensajes del canal y les guarda en una base de datos Mongo
2) Néstor responde a preguntas de tipo:
    a)“OK Néstor, cuál es el último mensaje enviado por [“nombre de usuario del canal”]
    b)“OK Néstor, cuántos mensajes han sidos enviados por [“nombre de usuario del canal”]

'''

import slack
import os
import pymongo
from flask import Flask
from slackeventsapi import SlackEventAdapter

client = pymongo.MongoClient('localhost', 27017)

db = client['nestor']
collection = db['mensajes']

app = Flask(__name__)


slack_event_adapter = SlackEventAdapter(
    os.environ.get("SIGNING_SECRET"),'/slack/events',app)

client = slack.WebClient(token=os.environ.get("SLACK_TOKEN"))
BOT_ID = client.api_call("auth.test")['user_id']

result = client.users_list()['members']
users = {}

for i in result:
    users[i['id']] = i['name']

def searchName(user_name):
    for key in users.keys():
        if(users[key] == user_name):
            return(key)

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if (BOT_ID != user_id and "OK Néstor, cuál es el ultimo mensaje enviado por" not in text and "OK Néstor, cuántos mensajes han sidos enviados por" not in text):
        collection.insert_one({"user_id": user_id, "text": text})
        
    if(BOT_ID != user_id and "OK Néstor, cuál es el ultimo mensaje enviado por" in text):
        user_name = text[49:]
        user = searchName(user_name)
        resp = collection.find({"user_id": user}).sort("_id", pymongo.DESCENDING).limit(1)
        for doc in resp:
            client.chat_postMessage(channel=channel_id, text="El ultimo mensaje enviado por " + user_name + " fue: " + doc['text'])

    if(BOT_ID != user_id and "OK Néstor, cuántos mensajes han sidos enviados por" in text):
        user_name = text[51:]
        user = searchName(user_name)
        resp = collection.find({"user_id": user}).count()
        client.chat_postMessage(channel=channel_id, text=user_name + " ha enviado " + str(resp) + " mensajes.")


if (__name__ == "__main__"):
    app.run(debug=True, port=3000)