FROM python:3

WORKDIR /srv/app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD DEBUG=True gunicorn --bind=0.0.0.0:5000 --access-logfile - --reload kegermon:app
