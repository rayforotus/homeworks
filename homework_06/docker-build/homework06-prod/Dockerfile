FROM tiangolo/uwsgi-nginx:python3.9

ENV PYTHONBUFFERED=1

COPY requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

COPY . .