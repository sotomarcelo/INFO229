FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1425337209188-1417229608375-vWOOtpVebm3mLRBxu932Limv"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
