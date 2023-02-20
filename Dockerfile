
FROM python:3.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN python3 -m spacy download en_core_web_md

COPY . /app

CMD [ "python", "watch_next.py"]