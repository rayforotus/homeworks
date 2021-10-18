FROM python:3.9-buster

WORKDIR /var/app

COPY app/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY app .

CMD uvicorn app:app --host 0.0.0.0 --port 8000

EXPOSE 8000/tcp