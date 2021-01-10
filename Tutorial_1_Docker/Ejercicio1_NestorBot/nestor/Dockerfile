FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1425337209188-1417229608375-Syo4KfGxQ7u4g9N31Lb9iIsD"
ENV SIGNING_SECRET="b3ef202f9e244069c0b6abe87df8b3ac"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor

COPY ./nestorbot.py /nestorbot.py
COPY ./nestorbot_app.py /nestorbot_app.py

USER    ngrok:ngrok
EXPOSE 80/tcp 443/tcp 8081/tcp 8082/tcp

CMD [ "python", "/nestorbot_app.py" ]
