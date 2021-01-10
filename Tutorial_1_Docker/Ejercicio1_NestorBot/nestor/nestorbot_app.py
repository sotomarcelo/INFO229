import slack
import os
import pymongo
from flask import Flask
from slackeventsapi import SlackEventAdapter

#MONGO
#DATABASE="nestor"
#COLLECTION="mensajes"

#myclient = pymongo.MongoClient(host=os.environ['MONGO_HOST'], port=int(os.environ['MONGO_PORT']))
#db = myclient[DATABASE]
#col = db[COLLECTION]


#BOT SLACK
app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    os.environ.get("SIGNING_SECRET"),'/slack/events',app)

client = slack.WebClient(token=os.environ.get("SLACK_TOKEN"))
BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if (BOT_ID != user_id):
        client.chat_postMessage(channel=channel_id, text=text)


if (__name__ == "__main__"):
    app.run(debug=True, port=80)