FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1425337209188-1417229608375-vWOOtpVebm3mLRBxu932Limv"
ENV SIGNING_SECRET="b3ef202f9e244069c0b6abe87df8b3ac"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /bot

COPY ./proyecto.py /proyecto.py

CMD [ "python", "/proyecto.py" ]
