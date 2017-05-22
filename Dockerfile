FROM python:3

WORKDIR /srv/app

COPY . .
RUN pip install --editable .

ENV FLASK_APP kegermon
ENV FLASK_DEBUG true
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
