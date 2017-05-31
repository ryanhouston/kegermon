FROM python:3

WORKDIR /srv/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENV FLASK_APP kegermon/kegermon.py
ENV FLASK_DEBUG true
CMD flask run --host=0.0.0.0
